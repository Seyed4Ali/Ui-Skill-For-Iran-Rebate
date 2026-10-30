# قرارداد طراحی: [محصول / نسخه]

- منبع فعلی برند/کد/طراحی، تاریخ و وضعیت تأیید:
- زبان، جهت، پلتفرم و نیازهای مخاطب:
- اصول: [مثلاً وضوح وضعیت، تراکم مناسب وظیفه؛ نه صفت مبهم]

## توکن‌های معنایی

مقادیر از سیستم موجود استخراج شوند؛ مقدار پیشنهادی تا رندر و تست تأییدشده نیست.

| نقش | نام توکن | مقدار فعلی/پیشنهادی | کاربرد | بررسی |
| --- | --- | --- | --- | --- |
| سطح | surface.base / surface.raised | | زمینه و سطح بالاتر | تم‌ها |
| متن | text.primary / secondary / inverse | | خوانایی و سلسله‌مراتب | کنتراست |
| عمل | action.primary / hover / pressed | | اقدام اصلی | تمام وضعیت‌ها |
| بازخورد | status.error / success / warning | | همراه متن/آیکون | عدم اتکا به رنگ |
| مرز و focus | border.default / focus.ring | | مرز و کیبورد | دیده‌شدن |
| تایپ | type.body / label / heading | | فونت، وزن، اندازه، line-height | حروف فارسی |
| هندسه | space.* / radius.* / elevation.* | | ریتم و مرزبندی | انسجام |
| حرکت | motion.duration / easing / reduced | | بازخورد | reduced-motion |

## قرارداد هر کامپوننت

- نام، هدف و زمانی که نباید استفاده شود:
- anatomy و API/variantهای موجود:
- default، hover، focus، active، disabled، loading، error، success:
- label، متن کمکی، validation و recovery:
- keyboard، accessible name، semantics و focus behavior:
- موبایل، RTL، متن بلند و mixed direction:
- معیار پذیرش و نمونه داده واقعی:

## تصمیم و نگهداری

| تصمیم | دلیل / شواهد | گزینه دیگر و trade-off | مالک / تاریخ / وضعیت |
| --- | --- | --- | --- |
| [تصمیم] | [مشخص] | [هزینه] | proposed / approved |

منبع الهام مجوز استفاده از فونت/asset نیست؛ مجوز را مستقل بررسی کن. برای handoff، مسیر فایل کد/طراحی و موارد pending را مشخص کن.
