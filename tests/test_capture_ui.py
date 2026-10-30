"""Functional checks against local pages, including deliberate UI failures."""

from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import threading
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/product-ui-ux/scripts/capture_ui.py"
SPEC = importlib.util.spec_from_file_location("capture_ui", SCRIPT)
capture_ui = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(capture_ui)


class URLTests(unittest.TestCase):
    def test_rejects_non_web_url_and_embedded_credentials(self):
        import argparse
        for url in ("file:///etc/passwd", "javascript:alert(1)", "https://user:secret@example.com", "not-a-url"):
            with self.subTest(url=url), self.assertRaises(argparse.ArgumentTypeError):
                capture_ui.page_url(url)
        self.assertEqual(capture_ui.page_url("http://127.0.0.1:3000"), "http://127.0.0.1:3000")


class FixtureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        status = 404 if self.path == "/missing" else 200
        content = "<main><h1>ساخت پروژه</h1><label for='name'>نام پروژه</label><input id='name'><button>ساخت پروژه</button></main>"
        if self.path == "/broken":
            content += "<div style='width:1800px'>متن طولانی</div><script>console.error('fixture console failure');throw new Error('fixture page failure')</script>"
        body = ("<!doctype html><html lang='fa' dir='rtl'><head><meta charset='utf-8'><title>UI fixture</title>"
                "<style>body{margin:0;font-family:sans-serif}main{padding:16px}input{max-width:100%}</style></head><body>"
                + content + "</body></html>").encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class BrowserTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            raise unittest.SkipTest("Playwright is not installed")
        cls.browser_path = shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")
        if not cls.browser_path:
            with sync_playwright() as playwright:
                if not Path(playwright.chromium.executable_path).is_file():
                    raise unittest.SkipTest("Chromium is not installed")
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), FixtureHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base_url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / "capture"

    def run_capture(self, path):
        return capture_ui.capture(self.base_url + path, self.output, self.browser_path)

    def test_responsive_persian_page_produces_three_images(self):
        report = self.run_capture("/")
        self.assertFalse(report["has_issues"], report)
        self.assertEqual(len(report["viewports"]), 3)
        for row in report["viewports"]:
            self.assertEqual(row["lang"], "fa")
            self.assertEqual(row["direction"], "rtl")
            self.assertEqual(row["http_status"], 200)
            self.assertFalse(row["horizontal_overflow"])
            self.assertTrue((self.output / row["screenshot"]).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
        self.assertEqual(json.loads((self.output / "report.json").read_text())["url"], self.base_url + "/")

    def test_broken_page_reports_rtl_overflow_and_script_errors(self):
        report = self.run_capture("/broken")
        self.assertTrue(report["has_issues"])
        for row in report["viewports"]:
            self.assertTrue(row["horizontal_overflow"])
            self.assertTrue(any("fixture console failure" in message for message in row["errors"]))
            self.assertTrue(any("fixture page failure" in message for message in row["errors"]))

    def test_http_error_makes_strict_cli_fail(self):
        args = ["--url", self.base_url + "/missing", "--output", str(self.output), "--strict"]
        if self.browser_path:
            args.extend(["--browser-path", self.browser_path])
        with redirect_stdout(io.StringIO()):
            self.assertEqual(capture_ui.main(args), 1)
        report = json.loads((self.output / "report.json").read_text())
        self.assertTrue(all(row["http_status"] == 404 for row in report["viewports"]))

    def test_existing_evidence_is_never_overwritten(self):
        self.output.mkdir()
        evidence = self.output / "report.json"
        evidence.write_text("previous evidence")
        with self.assertRaises(FileExistsError):
            self.run_capture("/")
        self.assertEqual(evidence.read_text(), "previous evidence")


if __name__ == "__main__":
    unittest.main()
