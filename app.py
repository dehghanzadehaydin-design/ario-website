
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOVA | سایت حرفه‌ای</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Tahoma, Arial, sans-serif;
            background: #0b1020;
            color: #f4f6ff;
            line-height: 1.9;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        header {
            position: sticky;
            top: 0;
            z-index: 10;
            background: rgba(11, 16, 32, 0.94);
            border-bottom: 1px solid #252d45;
            backdrop-filter: blur(12px);
        }

        nav {
            max-width: 1100px;
            margin: auto;
            padding: 16px 22px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
        }

        .logo {
            color: #7c8cff;
            font-size: 27px;
            font-weight: bold;
            letter-spacing: 2px;
        }

        .links {
            display: flex;
            align-items: center;
            gap: 22px;
            flex-wrap: wrap;
        }

        .links a {
            color: #c4cbe0;
            transition: 0.2s;
        }

        .links a:hover,
        .links a.active {
            color: #8b9aff;
        }

        .container {
            width: min(1100px, 92%);
            margin: auto;
        }

        .hero {
            padding: 95px 0 80px;
            text-align: center;
            background:
                radial-gradient(ellipse at top, #252c65 0%, transparent 65%);
        }

        .tag {
            display: inline-block;
            border: 1px solid #414b85;
            background: #171d3b;
            color: #aeb8ff;
            border-radius: 30px;
            padding: 5px 17px;
            margin-bottom: 20px;
            font-size: 13px;
        }

        h1 {
            font-size: clamp(36px, 6vw, 65px);
            line-height: 1.5;
            margin-bottom: 18px;
        }

        .gradient {
            background: linear-gradient(90deg, #8b9aff, #5ee7df);
            -webkit-background-clip: text;
            color: transparent;
        }

        .description {
            max-width: 650px;
            margin: 0 auto 28px;
            color: #aeb7cf;
            font-size: 17px;
        }

        .button {
            display: inline-block;
            padding: 12px 24px;
            border-radius: 12px;
            background: #7183ff;
            color: white;
            font-weight: bold;
            border: 1px solid #7183ff;
            cursor: pointer;
            transition: 0.25s;
            font-family: inherit;
            font-size: 15px;
        }

        .button:hover {
            transform: translateY(-3px);
            background: #586cf0;
        }

        .button.secondary {
            background: transparent;
            border-color: #39435f;
            margin-right: 8px;
        }

        section {
            padding: 55px 0;
        }

        .section-title {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .section-description {
            color: #aeb7cf;
            margin-bottom: 28px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 20px;
        }

        .card {
            background: #121a2d;
            border: 1px solid #28334d;
            padding: 25px;
            border-radius: 18px;
            transition: 0.25s;
        }

        .card:hover {
            transform: translateY(-6px);
            border-color: #7183ff;
        }

        .icon {
            font-size: 32px;
            margin-bottom: 10px;
        }

        .card h3 {
            margin-bottom: 9px;
        }

        .card p {
            color: #aeb7cf;
            font-size: 14px;
        }

        .banner {
            padding: 35px;
            border-radius: 22px;
            border: 1px solid #343e68;
            background: linear-gradient(135deg, #171f40, #111a2d);
        }

        .banner p {
            color: #b8c1d9;
            margin: 10px 0 20px;
        }

        .page {
            min-height: 65vh;
            padding: 70px 0;
        }

        footer {
            margin-top: 40px;
            border-top: 1px solid #252d45;
            padding: 25px 0;
            text-align: center;
            color: #8994af;
            font-size: 13px;
        }

        @media (max-width: 700px) {
            nav {
                flex-direction: column;
            }

            .links {
                justify-content: center;
                gap: 14px;
                font-size: 14px;
            }

            .hero {
                padding: 65px 0;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .section-title {
                font-size: 25px;
            }

            .banner {
                padding: 24px;
            }
        }
    </style>
</head>

<body>

<header>
    <nav>
        <a class="logo" href="/">NOVA.</a>

        <div class="links">
            <a href="/" class="{{ 'active' if page == 'home' else '' }}">
                خانه
            </a>
            <a href="/services"
               class="{{ 'active' if page == 'services' else '' }}">
                خدمات
            </a>
            <a href="/about"
               class="{{ 'active' if page == 'about' else '' }}">
                درباره ما
            </a>
        </div>
    </nav>
</header>

{% if page == 'home' %}

    <main>
        <div class="hero">
            <div class="container">
                <span class="tag">نسل جدید طراحی وب</span>

                <h1>
                    ایده‌هایت را به
                    <span class="gradient">واقعیت</span>
                    تبدیل کن
                </h1>

                <p class="description">
                    به NOVA خوش آمدی؛ جایی برای ساخت تجربه‌های دیجیتال
                    مدرن، سریع و جذاب.
                </p>

                <a href="/services" class="button">
                    مشاهده خدمات
                </a>

                <a href="/about" class="button secondary">
                    بیشتر بدان
                </a>
            </div>
        </div>

        <section class="container">
            <h2 class="section-title">چرا NOVA؟</h2>
            <p class="section-description">
                همه چیز برای شروع یک تجربه دیجیتال بهتر آماده است.
            </p>

            <div class="grid">
                <div class="card">
                    <div class="icon">⚡</div>
                    <h3>سرعت بالا</h3>
                    <p>ساختاری سبک و ساده برای تجربه سریع‌تر کاربران.</p>
                </div>

                <div class="card">
                    <div class="icon">🎨</div>
                    <h3>طراحی مدرن</h3>
                    <p>رنگ‌بندی هماهنگ و ظاهر مناسب برای سایت حرفه‌ای.</p>
                </div>

                <div class="card">
                    <div class="icon">📱</div>
                    <h3>واکنش‌گرا</h3>
                    <p>نمایش مناسب در موبایل، تبلت و کامپیوتر.</p>
                </div>
            </div>
        </section>

        <section class="container">
            <div class="banner">
                <h2>آماده شروع هستی؟</h2>
                <p>صفحات سایتت را ببین و قدم بعدی را شروع کن.</p>
                <a href="/services" class="button">شروع کنیم</a>
            </div>
        </section>
    </main>

{% elif page == 'services' %}

    <main class="container page">
        <span class="tag">خدمات ما</span>
        <h1>چه چیزی می‌سازیم؟</h1>
        <p class="section-description">
            این بخش می‌تواند خدمات واقعی کسب‌وکار تو را معرفی کند.
        </p>

        <div class="grid">
            <div class="card">
                <div class="icon">🌐</div>
                <h3>طراحی سایت</h3>
                <p>طراحی صفحات زیبا برای معرفی کسب‌وکار و محصولات.</p>
            </div>

            <div class="card">
                <div class="icon">🛍️</div>
                <h3>فروشگاه اینترنتی</h3>
                <p>زمینه‌ای برای نمایش محصولات و توسعه فروش آنلاین.</p>
            </div>

            <div class="card">
                <div class="icon">🧩</div>
                <h3>ابزارهای اختصاصی</h3>
                <p>ساخت امکانات متناسب با نیازهای پروژه.</p>
            </div>
        </div>
    </main>

{% elif page == 'about' %}

    <main class="container page">
        <span class="tag">درباره NOVA</span>
        <h1>ایده‌ای برای ساختن بهتر</h1>

        <div class="card">
            <h2>هدف ما چیست؟</h2>
            <p>
                NOVA یک پروژه وب برای یادگیری و ساخت تجربه‌های دیجیتال
                است. این سایت با پایتون و فریم‌ورک Flask اجرا می‌شود.
                می‌توانیم در مراحل بعدی، پایگاه داده، حساب کاربری،
                فرم تماس و پنل مدیریت را به آن اضافه کنیم.
            </p>
        </div>

        <br>
        <a href="/" class="button">بازگشت به خانه</a>
    </main>

{% endif %}

<footer>
    <div class="container">
        © 2026 NOVA — ساخته‌شده با پایتون و Flask
    </div>
</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, page="home")


@app.route("/work")
def services():
    return render_template_string(HTML, page="services")


@app.route("/contact")
def about():
    return render_template_string(HTML, page="about")


if __name__ == "__main__":
    app.run(debug=True)
