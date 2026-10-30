#!/usr/bin/env python3
"""Capture UI evidence without clicking, authentication or accessibility claims."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit


VIEWPORTS = ((360, 900), (768, 1024), (1440, 1000))


def page_url(value):
    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise argparse.ArgumentTypeError("Use an http(s) page URL.")
    if parsed.username is not None or parsed.password is not None:
        raise argparse.ArgumentTypeError("Do not put credentials in the URL.")
    return value


def capture(url, output, browser_path=None, ready_selector="body", timeout_ms=15000):
    from playwright.sync_api import sync_playwright

    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    report = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "url": url,
        "motion_preference": "reduce",
        "limits": "Static captures, not interaction, accessibility or performance tests.",
        "viewports": [],
    }
    try:
        with sync_playwright() as playwright:
            options = {"headless": True}
            if browser_path:
                options["executable_path"] = browser_path
            browser = playwright.chromium.launch(**options)
            try:
                for width, height in VIEWPORTS:
                    result = {"width": width, "height": height, "errors": []}
                    report["viewports"].append(result)
                    context = browser.new_context(
                        viewport={"width": width, "height": height},
                        reduced_motion="reduce",
                        ignore_https_errors=False,
                    )
                    try:
                        page = context.new_page()
                        page.set_default_timeout(timeout_ms)
                        page.on("pageerror", lambda error, row=result: row["errors"].append(str(error)[:1500]))
                        page.on("console", lambda msg, row=result: row["errors"].append(msg.text[:1500]) if msg.type == "error" else None)
                        response = page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
                        result["http_status"] = response.status if response else None
                        page.locator(ready_selector).first.wait_for(state="visible")
                        page.wait_for_function("document.fonts.status === 'loaded'")
                        page.evaluate("() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))")
                        result.update(page.evaluate("""() => ({
                          title: document.title,
                          lang: document.documentElement.lang,
                          direction: getComputedStyle(document.documentElement).direction,
                          viewport_width: document.documentElement.clientWidth,
                          content_width: Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0)
                        })"""))
                        result["horizontal_overflow"] = result["content_width"] > result["viewport_width"] + 1
                        image_name = f"{width}.png"
                        page.screenshot(path=str(output / image_name), full_page=True, timeout=timeout_ms)
                        result["screenshot"] = image_name
                    except Exception as error:
                        result["capture_error"] = str(error)[:2000]
                    finally:
                        context.close()
            finally:
                browser.close()
    except Exception as error:
        report["capture_error"] = str(error)[:2000]

    report["has_issues"] = bool(report.get("capture_error")) or any(
        row.get("capture_error")
        or row.get("http_status") is None
        or row.get("http_status", 0) >= 400
        or row.get("horizontal_overflow")
        or row["errors"]
        for row in report["viewports"]
    )
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", type=page_url, required=True)
    parser.add_argument("--output", type=Path, required=True, help="New local directory; existing paths are never overwritten.")
    parser.add_argument("--browser-path", help="Optional system Chromium executable.")
    parser.add_argument("--ready-selector", default="body", help="Visible marker for the specific page state you need.")
    parser.add_argument("--strict", action="store_true", help="Exit 1 for HTTP/navigation errors, JS/console errors or overflow.")
    args = parser.parse_args(argv)
    try:
        report = capture(args.url, args.output, args.browser_path, args.ready_selector)
    except ImportError:
        parser.exit(2, "Playwright is missing; install requirements-browser.txt in a virtual environment.\n")
    except FileExistsError:
        parser.exit(2, "Output path exists; choose a new directory to preserve earlier evidence.\n")
    print(f"Captured {len(report['viewports'])} viewport attempts; report: {args.output / 'report.json'}")
    # An incomplete capture is an execution failure even outside strict mode.
    incomplete = report.get("capture_error") or any(row.get("capture_error") for row in report["viewports"])
    return 1 if incomplete or (args.strict and report["has_issues"]) else 0


if __name__ == "__main__":
    sys.exit(main())
