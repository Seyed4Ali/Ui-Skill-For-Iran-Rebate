# گزارش منابع و راهنمای تحقیق

تاریخ بررسی: ۲۰۲۶-۱۰-۳۰. این گزارش مرور مستندات و چند تصویر است؛ مطالعه کاربران محصولات تو، ممیزی کامل ابزارها یا تست کارایی آن‌ها نیست. آمار ستاره‌ها و مجموع 550K ارسالی تأیید نشدند و در انتخاب نقشی ندارند. متن‌های remote قابل تغییرند؛ برای نصب احتمالی آینده نسخه/commit و مجوز باید دوباره بررسی شود.

## ده مخزن پیشنهادی

README هر ده نشانی زیر از `raw.githubusercontent.com` خوانده شد. قابلیت‌ها در این جدول توصیف مستندات سازنده‌اند، نه نتیجه اجرای مستقل. هیچ ابزار ثالثی نصب یا کپی نشده است.

| منبع | کاربرد بالقوه | جایگاه در روند ما |
| --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable) · [README](https://raw.githubusercontent.com/pbakaus/impeccable/main/README.md) | نقد، audit، polish و کنترل کیفیت بصری؛ README از ۶۲ قاعده قطعی می‌گوید | نزدیک به نیاز روزانه؛ ایده تفکیک نقد از پرداخت نهایی، بدون واردکردن کد/فرمان‌های آن |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · [README](https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/README.md) | پیشنهاد سبک، رنگ، تایپوگرافی و سیستم طراحی | کمک به گزینه‌سازی؛ پیشنهاد خودکار جای شناخت کاربر و برند را نمی‌گیرد |
| [MCP for Blender](https://github.com/ahujasid/blender-mcp) · [README](https://raw.githubusercontent.com/ahujasid/blender-mcp/main/README.md) | ارتباط عامل با Blender برای ساخت سه‌بعدی | اختیاری برای asset سه‌بعدی؛ README تغییر نام بسته به `mcp-for-blender` را ذکر می‌کند؛ اینجا آزموده نشده |
| [img2threejs](https://github.com/img2threejs/img2threejs) · [README](https://raw.githubusercontent.com/img2threejs/img2threejs/main/README.md) | بازسازی مرجع با هندسه و کد Three.js | برای صحنه تعاملی خاص؛ نیازمند ارزیابی شباهت، بارگذاری و دسترس‌پذیری جایگزین |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) · [README](https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/main/README.md) | ساخت پرومو از صفحات و دستورهای حرکت با Remotion | مرحله معرفی محصول؛ معیار بهبود مسیر کاربر نیست |
| [HyperFrames](https://github.com/heygen-com/hyperframes) · [README](https://raw.githubusercontent.com/heygen-com/hyperframes/main/README.md) | ساخت و رندر محتوای ویدئویی با HTML و ابزارهای عامل | گزینه اتوماسیون ویدئو؛ اتصال Figma و مجوزها نیازمند بررسی عملی |
| [Penpot](https://github.com/penpot/penpot) · [README](https://raw.githubusercontent.com/penpot/penpot/develop/README.md) | طراحی، توکن، layout و API/MCP طبق مستندات | گزینه همکاری طراحی؛ در این محیط اتصال فعال و آزموده ندارد |
| [Remotion](https://github.com/remotion-dev/remotion) · [README](https://raw.githubusercontent.com/remotion-dev/remotion/main/README.md) | ویدئو با React و batch rendering | اختیاری؛ شرایط مجوز استفاده تیمی/تجاری جدا بررسی شود |
| [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) · [README](https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/main/README.md) | سبک‌های فیلم ساخته‌شده با کد | ایده motion؛ README فعلی ۶۶ سبک و تنظیم برای مدل مشخص را می‌گوید، نه تضمین کیفیت روی همه مدل‌ها |
| [diagram-design](https://github.com/cathrynlavery/diagram-design) · [README](https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/README.md) | نمودار HTML+SVG هماهنگ با برند | برای flow و توضیح معماری/محصول؛ کیفیت نمودار باید جدا بررسی شود |

پیشنهاد ترتیب آزمایش عملی آینده: یک فرم/مسیر واقعی با Impeccable، سپس یک بریف ثابت با UI UX Pro Max. ورودی ثابت، زمان صرف‌شده، خطاهای کیبورد/RTL و کیفیت خروجی قابل نگهداری را مقایسه کنیم؛ برنده را از روی ستاره‌ها تعیین نکنیم.

## مشاهده بصری واقعی؛ چهار تصویر

این تصاویر باز و دیده شدند؛ در بسته توزیع نمی‌شوند. بررسی تنها تصویر ثابت است، نه صفحات زنده یا نمونه نماینده تمام آثار ابزار.

| تصویر | مشاهده | برداشت قابل استفاده و محدودیت |
| --- | --- | --- |
| [Impeccable: before](https://raw.githubusercontent.com/pbakaus/impeccable/main/docs/images/readme-without.webp) | پس‌زمینه روشن، چیدمان دو ستونه، تیتر serif، دو اقدام و تصویرسازی تخت | خوانایی و آرامش بصری؛ ادعای «بد»بودن UX از تصویر ممکن نیست |
| [Impeccable: after](https://raw.githubusercontent.com/pbakaus/impeccable/main/docs/images/readme-with.webp) | تصویر سرتاسری شب، تیتر فشرده بزرگ، اقدام قرمز مرکزی و ماه‌های سال پایین صفحه | یک ایده بصری منسجم و اقدام برجسته‌تر؛ کنتراست روی تصویر، عرض موبایل و دسترس‌پذیری کنترل ماه‌ها نیازمند تست‌اند |
| [UI UX Pro Max: website](https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/screenshots/website.png) | زمینه تیره، تیتر بزرگ، دو اقدام، ردیف ابزارها و شش کارت آمار | گروه‌بندی و سلسله‌مراتب قابل مشاهده است؛ کارت‌های عددی و gradient نباید بدون دلیل به همه محصولات منتقل شوند؛ اعداد تصویر ممکن است با README امروز فرق داشته باشند |
| [diagram-design: hero](https://raw.githubusercontent.com/cathrynlavery/diagram-design/main/docs/hero/hero-light.webp) | تیتر بزرگ مشکی، فضای سفید، خطوط نمودار ظریف و accent محدود | برای ارائه و توضیح مناسب به نظر می‌رسد؛ خطوط ظریف/متن کوچک برای نمودار عملیاتی و موبایل نیازمند بازبینی‌اند |

این چهار تصویر عمدتاً تبلیغ ابزارند؛ نمونه‌برداری کامل اپلیکیشن‌ها یا تحقیق رقابتی محصول تو هنوز انجام نشده. آن مرحله به نوع محصول و مسئله‌اش وابسته است.

برای اضافه‌کردن نمونه اپلیکیشن، README رسمی [Excalidraw](https://raw.githubusercontent.com/excalidraw/excalidraw/master/README.md) و [Plane](https://raw.githubusercontent.com/makeplane/plane/master/README.md) هم خوانده شد. اما تصاویر رابط آن‌ها روی `excalidraw.nyc3.cdn.digitaloceanspaces.com` و `media.docs.plane.so` با 403 باز نشدند؛ تصاویر رابط Penpot در GitHub attachments نیز همین محدودیت را داشتند. بنابراین هیچ مشاهده بصری یا توصیه الگویی را به این سه رابط نسبت نمی‌دهیم. README قابل دسترس به معنای بررسی رابط زنده نیست.

## منابع رسمی قابل دسترس

- [W3C: Contrast Minimum، متن رسمی مخزن](https://raw.githubusercontent.com/w3c/wcag/main/understanding/20/contrast-minimum.html): متن، آستانه‌ها، تعریف متن بزرگ و نحوه محاسبه/استثناها بررسی شد. [صفحه اصلی](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- [W3C: Target Size Minimum، متن رسمی مخزن](https://raw.githubusercontent.com/w3c/wcag/main/understanding/22/target-size-minimum.html): ۲۴×۲۴ CSS px و پنج دسته استثنا بررسی شد. [صفحه اصلی](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
- [GOV.UK: Error summary، متن رسمی مخزن](https://raw.githubusercontent.com/alphagov/govuk-design-system/main/src/components/error-summary/index.md): خلاصه بالای صفحه، ارتباط با خطای کنار فیلد، focus و لینک به ورودی‌ها. قاعده «همیشه خلاصه خطا» متعلق به سیستم GOV.UK است؛ آن را الزام جهانی هر فرم کوتاه معرفی نکنیم.

این منابع برای قواعد دسترس‌پذیری و بازیابی خطا به کار رفته‌اند؛ اثبات نرخ تبدیل یا رضایت کاربران ایرانی نیستند.

## دسترسی ناموفق و ادامه تحقیق

در درخواست مستقیم HTTPS این آدرس‌ها با `Tunnel connection failed: 403 Forbidden` باز نشدند:

- [کاشی](https://kashi.sepantapouya.com/): معرفی فارسی‌بودن، رایگان‌بودن، پلاگین و قابلیت سفارشی‌سازی فعلاً نقل از کاربر است. هیچ صفحه/فایل کاشی دیده نشده است.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) و [جهت HTML](https://www.w3.org/International/questions/qa-html-dir): فقط دو متن رسمی WCAG از GitHub بررسی شدند؛ صفحه راهنمای جهت باز نشد.
- [Carbon Data table](https://carbondesignsystem.com/components/data-table/usage/) و [GOV.UK Error summary](https://design-system.service.gov.uk/components/error-summary/): متن رسمی GOV.UK از GitHub در دسترس بود، Carbon بررسی نشد.
- [Linear](https://linear.app/) و [Stripe](https://stripe.com/): هیچ رابط زنده‌ای بررسی نشد؛ از نام آن‌ها نتیجه طراحی گرفته نشده.
- [Baymard Research](https://baymard.com/research) و [NN/g heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/): محتوای این صفحات در این نوبت خوانده نشد.

برای ادامه دسترسی، دامنه‌های دقیق موردنیاز را در تنظیمات شبکه محیط اضافه و عملیات را دوباره بررسی کن؛ فهرست مجاز موجود را جایگزین یا TLS را غیرفعال نکن. این بسته تنظیم شبکه را تغییر نداده است. خروجی مجاز از فایل طراحی یا صفحه هم می‌تواند بررسی مستقل را جلو ببرد.

## الگوی تحقیق روی محصول بعدی

1. از شواهد محصول خودمان شروع کنیم؛ مسئله و نمونه کاربران/وظایف را مشخص کنیم.
2. برای همان کار، ۳ تا ۵ مرجع مرتبط انتخاب کنیم؛ زیبایی landing page جای بررسی جریان کاربردی نیست.
3. صفحه/وضعیت مشخص را ببینیم: خطا، فیلتر، ثبت‌نام، جدول یا پرداخت، نه صرف صفحه اول.
4. برای هر برداشت، URL، تاریخ، مشاهده، فرضیه انتقال، ریسک و آزمون بعدی ثبت کنیم.
5. پیشنهاد را با تست وظیفه و سنجه‌های همان محصول محک بزنیم. نبود دسترسی یا داده را صریح بنویسیم.
