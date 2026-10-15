from flask import Flask, render_template_string

app = Flask(__name__)
import sqlite3
def init_db():
    conn = sqlite3.connect("agriculture.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS farmers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AgriCare | Smart Farming</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #f5f8f2;
    color: #20352a;
}

nav {
    background: #103f2b;
    padding: 18px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
}

.logo {
    color: white;
    font-size: 25px;
    font-weight: bold;
}

.logo span {
    color: #b5ed8c;
}

.nav-links {
    display: flex;
    gap: 22px;
    flex-wrap: wrap;
}

.nav-links a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    font-size: 14px;
}

.nav-links a:hover {
    color: #b5ed8c;
}

.hero {
    min-height: 490px;
    padding: 90px 8%;
    display: flex;
    align-items: center;
    background:
    linear-gradient(90deg,
    rgba(8, 40, 25, 0.88),
    rgba(8, 40, 25, 0.35)),
    url('https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=2000&q=85');
    background-size: cover;
    background-position: center;
}

.hero-content {
    max-width: 680px;
    color: white;
}

.tag {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    padding: 10px 16px;
    border-radius: 30px;
    margin-bottom: 22px;
}

.hero h1 {
    font-size: clamp(36px, 5vw, 60px);
    line-height: 1.12;
    margin-bottom: 22px;
}

.hero h1 span {
    color: #b8f18d;
}

.hero p {
    font-size: 17px;
    line-height: 1.8;
    margin-bottom: 28px;
    max-width: 590px;
}

.search-box {
    background: white;
    padding: 8px;
    border-radius: 50px;
    display: flex;
    max-width: 580px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.18);
}

.search-box input {
    flex: 1;
    min-width: 0;
    border: none;
    outline: none;
    padding: 14px 18px;
    border-radius: 50px;
    font-size: 14px;
}

.search-box button {
    background: #14835b;
    color: white;
    border: none;
    border-radius: 40px;
    padding: 14px 23px;
    font-weight: bold;
    cursor: pointer;
}

.services {
    padding: 65px 7%;
}

.section-heading {
    text-align: center;
    margin-bottom: 38px;
}

.section-heading h2 {
    font-size: 34px;
    color: #164d34;
    margin-bottom: 12px;
}

.section-heading p {
    color: #6c7b70;
    line-height: 1.6;
}

.cards {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 24px;
}

.card {
    background: white;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 8px 28px rgba(25,65,40,0.09);
    transition: 0.3s;
    border: 1px solid #e8eee7;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 35px rgba(25,65,40,0.16);
}

.card img {
    width: 100%;
    height: 175px;
    object-fit: cover;
}

.card-content {
    padding: 23px;
}

.icon {
    font-size: 28px;
    margin-bottom: 12px;
}

.card h3 {
    color: #174c32;
    font-size: 20px;
    margin-bottom: 12px;
}

.card p {
    color: #6c7b70;
    font-size: 14px;
    line-height: 1.7;
    min-height: 70px;
}

.btn {
    display: inline-block;
    margin-top: 18px;
    padding: 12px 17px;
    border-radius: 9px;
    color: white;
    background: #147a50;
    text-decoration: none;
    font-size: 14px;
    font-weight: bold;
}

.btn:hover {
    background: #0c5435;
}

footer {
    background: #103f2b;
    color: white;
    text-align: center;
    padding: 28px 15px;
    line-height: 1.8;
}

@media (max-width: 1000px) {
    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 600px) {
    nav {
        justify-content: center;
    }

    .nav-links {
        justify-content: center;
        gap: 14px;
    }

    .hero {
        padding: 65px 6%;
    }

    .search-box {
        border-radius: 16px;
    }

    .search-box button {
        padding: 12px;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .section-heading h2 {
        font-size: 28px;
    }
}
</style>
</head>

<body>

<nav>
    <div class="logo">🌱 Agri<span>Care</span></div>

    <div class="nav-links">
        <a href="/">Home</a>
        <a href="/crops">Crop Information</a>
        <a href="/fertilizer">Fertilizer Guide</a>
        <a href="/diseases">Crop Diseases</a>
        <a href="/tips">Farming Tips</a>
    </div>
</nav>

<section class="hero">
    <div class="hero-content">
        <div class="tag">🌿 Smart Information for Better Farming</div>

        <h1>Grow Better.<br>Farm <span>Smarter.</span></h1>

        <p>
            Agriculture Help & Management System helps farmers
            explore crop information, fertilizer guidance, crop
            diseases and modern farming practices in one place.
        </p>

        <form class="search-box" onsubmit="return searchFarm(event)">
            <input id="farmSearch"
                   type="text"
                   placeholder="Search crops, diseases, fertilizers or tips...">
            <button type="submit">Search →</button>
        </form>
    </div>
</section>

<section class="services" id="services">
    <div class="section-heading">
        <h2>Explore Our Services 🌾</h2>
        <p>Everything you need for smarter and healthier farming.</p>
    </div>

    <div class="cards">

        <div class="card">
            <img src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=700&q=80">
            <div class="card-content">
                <div class="icon">🌱</div>
                <h3>Crop Information</h3>
                <p>Learn about crops, growing seasons, soil requirements and cultivation methods.</p>
                <a class="btn" href="/crops">Explore Crops →</a>
            </div>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=700&q=80">
            <div class="card-content">
                <div class="icon">🛡️</div>
                <h3>Crop Diseases</h3>
                <p>Understand common crop diseases, their symptoms, prevention and management.</p>
                <a class="btn" href="/diseases">View Diseases →</a>
            </div>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1416879595882-3373a0480b5b?auto=format&fit=crop&w=700&q=80">
            <div class="card-content">
                <div class="icon">🧪</div>
                <h3>Fertilizer Guide</h3>
                <p>Learn about soil nutrients, fertilizer types and responsible application.</p>
                <a class="btn" href="/fertilizer">Learn More →</a>
            </div>
        </div>

        <div class="card">
            <img src="https://images.unsplash.com/photo-1499529112087-3cb3b73cec95?auto=format&fit=crop&w=700&q=80">
            <div class="card-content">
                <div class="icon">💡</div>
                <h3>Farming Tips</h3>
                <p>Discover practical advice for irrigation, soil care and sustainable farming.</p>
                <a class="btn" href="/tips">Get Tips →</a>
            </div>
        </div>

    </div>
</section>

<footer>
    <h3>🌿 Agriculture Help & Management System</h3>
    <p>Smart Information for Better Farming</p>
    <p>© 2026 AgriCare | Helping Farmers Grow Better</p>
</footer>

<script>
function searchFarm(event) {
    event.preventDefault();

    let query = document.getElementById("farmSearch").value
        .toLowerCase().trim();

    if (query.includes("disease") || query.includes("रोग")) {
        window.location.href = "/diseases";
    } else if (query.includes("fertilizer") || query.includes("खाद")) {
        window.location.href = "/fertilizer";
    } else if (query.includes("tip") || query.includes("farming")) {
        window.location.href = "/tips";
    } else if (query.includes("crop") || query.includes("wheat") ||
               query.includes("गेहूं") || query.includes("धान")) {
        window.location.href = "/crops";
    } else {
        alert("Please search for crops, diseases, fertilizers or farming tips.");
    }

    return false;
}
</script>

</body>
</html>
""")
@app.route("/crops")
def crops():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Crop Information</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f1f8f3;
                color: #164e45;
            }

            /* Navigation Bar */
            nav {
                background: #075735;
                padding: 20px;
                display: flex;
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                gap: 15px;
            }

            nav a {
                color: white;
                text-decoration: none;
                font-weight: bold;
            }

            /* Hero Section */
            .hero {
                min-height: 270px;
                padding: 45px 4%;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 25px;

                background:
                    linear-gradient(
                        90deg,
                        rgba(235, 250, 241, 0.98),
                        rgba(235, 250, 241, 0.75),
                        rgba(235, 250, 241, 0.1)
                    ),
                    url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=85");

                background-size: cover;
                background-position: center;
            }

            .hero-text {
                max-width: 600px;
            }

            .hero h1 {
                font-size: 42px;
                margin: 0 0 15px;
                color: #073e3c;
            }

            .hero p {
                font-size: 18px;
                line-height: 1.7;
            }

            .hero img {
                width: 240px;
                height: 220px;
                object-fit: cover;
                border-radius: 18px;
                border: 4px solid white;
            }

            /* Search */
            .search {
                display: block;
                width: 90%;
                max-width: 450px;
                padding: 14px;
                margin: 25px auto;
                border: 1px solid #b7d6c2;
                border-radius: 8px;
                font-size: 16px;
            }

            /* Crop Cards */
            .crop-container {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 20px;
                padding: 10px 3% 35px;
            }

            .card {
                background: white;
                border-radius: 14px;
                overflow: hidden;
                box-shadow: 0 4px 15px #174d3015;
                padding-bottom: 20px;
                transition: transform 0.2s;
            }

            .card:hover {
                transform: translateY(-5px);
            }

            .crop-image {
                width: 100%;
                height: 200px;
                object-fit: cover;
            }

            .card-content {
                padding: 0 18px;
            }

            .card h2 {
                color: #075735;
                font-size: 25px;
            }

            .card p {
                line-height: 1.6;
                font-size: 15px;
            }

            .season {
                display: inline-block;
                background: #d8f5df;
                color: #075735;
                padding: 7px 12px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: bold;
            }

            .button {
                display: block;
                text-align: center;
                background: #087443;
                color: white;
                text-decoration: none;
                padding: 12px;
                margin-top: 18px;
                border-radius: 7px;
                font-weight: bold;
            }

            .button:hover {
                background: #05532f;
            }

            .back {
                display: block;
                width: fit-content;
                margin: 0 auto 30px;
                background: #087443;
                color: white;
                text-decoration: none;
                padding: 13px 25px;
                border-radius: 8px;
            }

            footer {
                background: #075735;
                color: white;
                padding: 22px;
                text-align: center;
            }

            /* Mobile Responsive */
            @media (max-width: 1000px) {
                .crop-container {
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }
            }

            @media (max-width: 600px) {
                .crop-container {
                    grid-template-columns: 1fr;
                }

                .hero {
                    flex-direction: column;
                    align-items: flex-start;
                }

                .hero h1 {
                    font-size: 30px;
                }

                .hero img {
                    width: 100%;
                    height: 220px;
                }

                nav {
                    flex-direction: column;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <a href="/">🌿 Agriculture Help</a>
            <a href="/">Home</a>
            <a href="/crops">Crop Information</a>
            <a href="/fertilizer">Fertilizer Guide</a>
            <a href="/diseases">Crop Diseases</a>
            <a href="/tips">Farming Tips</a>
        </nav>

        <section class="hero">
            <div class="hero-text">
                <h1>🌱 Crop Information</h1>

                <p>
                    Learn about important agricultural crops,
                    their growing seasons, cultivation methods
                    and uses.
                </p>
            </div>

            <img
                src="https://images.unsplash.com/photo-1592982537447-6f2a6a0d0dca?auto=format&fit=crop&w=600&q=85"
                alt="Farmer working in a field"
            >
        </section>

        <input
            type="text"
            id="search"
            class="search"
            placeholder="Search Wheat, Rice, Mustard, Cotton..."
            onkeyup="searchCrops()"
        >

        <section class="crop-container">

            <!-- Wheat -->
            <div class="card">
                <img
                    class="crop-image"
                    src="https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=700&q=85"
                    alt="Wheat crop"
                >

                <div class="card-content">
                    <h2>Wheat</h2>
                    <span class="season">Rabi Season</span>

                    <p><b>🌱 Sowing:</b> October–December</p>
                    <p><b>🌿 Growing Period:</b> About 4–5 months</p>
                    <p><b>Use:</b> Flour, bread and food products.</p>

                    <a class="button" href="/crops#wheat">
                        Learn More →
                    </a>
                </div>
            </div>

            <!-- Rice -->
            <div class="card">
                <img
                    class="crop-image"
                    src="https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?auto=format&fit=crop&w=700&q=85"
                    alt="Rice crop"
                >

                <div class="card-content">
                    <h2>Rice</h2>
                    <span class="season">Kharif Season</span>

                    <p><b>🌱 Sowing:</b> Depends on local conditions</p>
                    <p><b>🌿 Growing Period:</b> About 3–6 months</p>
                    <p><b>Use:</b> A major food crop.</p>

                    <a class="button" href="/crops#rice">
                        Learn More →
                    </a>
                </div>
            </div>

            <!-- Mustard -->
            <div class="card">
                <img
                    class="crop-image"
                    src="https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=700&q=85"
                    alt="Yellow flowers"
                >

                <div class="card-content">
                    <h2>Mustard</h2>
                    <span class="season">Rabi Season</span>

                    <p><b>🌱 Sowing:</b> Usually October–November</p>
                    <p><b>🌿 Growing Period:</b> About 3–4 months</p>
                    <p><b>Use:</b> Oil and spices.</p>

                    <a class="button" href="/crops#mustard">
                        Learn More →
                    </a>
                </div>
            </div>

            <!-- Cotton -->
            <div class="card">
                <img
    class="crop-image"
    src="/static/cotton.jpg"
    alt="Cotton crop"
>

                <div class="card-content">
                    <h2>Cotton</h2>
                    <span class="season">Kharif Season</span>

                    <p><b>🌱 Sowing:</b> Depends on region and variety</p>
                    <p><b>🌿 Growing Period:</b> Several months</p>
                    <p><b>Use:</b> Textile and clothing industries.</p>

                    <a class="button" href="/crops#cotton">
                        Learn More →
                    </a>
                </div>
            </div>

        </section>

        <a class="back" href="/">← Back to Home</a>

        <footer>
            <p>© 2026 Agriculture Help and Management System</p>
            <p>BTech CSE Minor Project</p>
        </footer>

        <script>
            function searchCrops() {
                let query = document
                    .getElementById("search")
                    .value.toLowerCase();

                let cards = document.querySelectorAll(".card");

                cards.forEach(function(card) {
                    let text = card.innerText.toLowerCase();

                    card.style.display =
                        text.includes(query) ? "" : "none";
                });
            }
        </script>

    </body>
    </html>
    """
@app.route("/fertilizer")
def fertilizer():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fertilizer Guide</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f3f8f0;
                margin: 0;
                color: #26382a;
            }

            header {
                background-color: #176b36;
                color: white;
                text-align: center;
                padding: 25px;
            }

            .container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                padding: 30px 15px;
            }

            .card {
                background: white;
                width: 250px;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 3px 10px #00000015;
            }

            h2 {
                color: #176b36;
            }

            .back {
                display: inline-block;
                background: #176b36;
                color: white;
                padding: 12px 20px;
                margin: 10px 20px 25px;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🧪 Fertilizer Guide</h1>
            <p>Learn About Fertilizers and Their Uses</p>
        </header>

        <div class="container">

            <div class="card">
                <h2>🌱 Urea</h2>
                <p><b>Type:</b> Nitrogen fertilizer</p>
                <p><b>Purpose:</b> Supplies nitrogen for plant growth.</p>
                <p>Use according to soil-test results and crop recommendations.</p>
            </div>

            <div class="card">
                <h2>🌿 DAP</h2>
                <p><b>Full Form:</b> Diammonium Phosphate</p>
                <p><b>Purpose:</b> Supplies nitrogen and phosphorus.</p>
                <p>Apply according to the crop's nutrient requirements.</p>
            </div>

            <div class="card">
                <h2>🍃 Compost</h2>
                <p><b>Type:</b> Organic soil amendment</p>
                <p><b>Purpose:</b> Adds organic matter and can improve soil structure.</p>
                <p>Quality and nutrient content depend on the material used.</p>
            </div>

            <div class="card">
                <h2>🌾 NPK Fertilizer</h2>
                <p><b>Full Form:</b> Nitrogen, Phosphorus, Potassium</p>
                <p><b>Purpose:</b> Supplies essential plant nutrients.</p>
                <p>Choose the appropriate grade based on crop and soil needs.</p>
            </div>

        </div>

        <a class="back" href="/">⬅ Back to Home</a>

    </body>
    </html>
    """
@app.route("/diseases")
def diseases():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Crop Diseases | Agriculture Help</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f3f8f0;
                color: #243b2a;
            }

            nav {
                background: #176b3a;
                color: white;
                padding: 18px 7%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 12px;
            }

            nav h2 {
                font-size: 23px;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin-left: 18px;
                font-weight: bold;
            }

            .hero {
                min-height: 340px;
                padding: 65px 8%;
                display: flex;
                align-items: center;
                color: white;
                background:
                    linear-gradient(90deg, rgba(0,45,20,.88),
                    rgba(0,45,20,.20)),
                    url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=85")
                    center/cover;
            }

            .hero-content {
                max-width: 600px;
            }

            .hero h1 {
                font-size: clamp(32px, 5vw, 48px);
                margin-bottom: 16px;
            }

            .hero p {
                font-size: 18px;
                line-height: 1.7;
                margin-bottom: 22px;
            }

            .btn {
                display: inline-block;
                background: #f4c542;
                color: #173d24;
                padding: 13px 22px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
            }

            .section {
                max-width: 1150px;
                margin: auto;
                padding: 45px 20px;
            }

            .section-title {
                text-align: center;
                font-size: 32px;
                color: #176b3a;
                margin-bottom: 12px;
            }

            .subtitle {
                text-align: center;
                color: #607267;
                margin-bottom: 32px;
                line-height: 1.6;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 24px;
            }

            .card {
                background: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 5px 18px rgba(0,0,0,.08);
                transition: transform .25s, box-shadow .25s;
            }

            .card:hover {
                transform: translateY(-7px);
                box-shadow: 0 12px 25px rgba(0,0,0,.15);
            }

            .card img {
                width: 100%;
                height: 190px;
                object-fit: cover;
                display: block;
            }

            .card-content {
                padding: 22px;
            }

            .card h3 {
                color: #176b3a;
                margin-bottom: 12px;
                font-size: 21px;
            }

            .card p {
                line-height: 1.7;
                margin-bottom: 10px;
                font-size: 14px;
            }

            .label {
                font-weight: bold;
                color: #354e39;
            }

            .notice {
                background: #fff4d5;
                border-left: 5px solid #e4a900;
                padding: 18px;
                margin-top: 30px;
                border-radius: 8px;
                line-height: 1.7;
            }

            footer {
                text-align: center;
                background: #124d2b;
                color: white;
                padding: 24px;
                line-height: 1.8;
            }

            @media(max-width: 600px) {
                nav {
                    flex-direction: column;
                    text-align: center;
                }

                nav a {
                    margin: 8px;
                    display: inline-block;
                }

                .hero {
                    padding: 45px 6%;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <h2>🌱 AgriCare</h2>
            <div>
                <a href="/">Home</a>
                <a href="/crops">Crops</a>
                <a href="/fertilizer">Fertilizer</a>
                <a href="/tips">Farming Tips</a>
            </div>
        </nav>

        <section class="hero">
            <div class="hero-content">
                <h1>Protect Your Crops 🌾</h1>
                <p>
                    Learn about common crop diseases, identify their symptoms,
                    and understand ways to protect your farm.
                </p>
                <a href="#diseases" class="btn">Explore Diseases ↓</a>
            </div>
        </section>

        <section class="section" id="diseases">

            <h2 class="section-title">Common Crop Diseases</h2>

            <p class="subtitle">
                Recognize common symptoms and take advice before treating crops.
            </p>

            <div class="grid">

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=700&q=80"
                        alt="Wheat field"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌾 Wheat Rust</h3>
                        <p><span class="label">Symptoms:</span>
                        Orange, yellow or brown rust-like spots on leaves.</p>
                        <p><span class="label">Prevention:</span>
                        Choose suitable resistant varieties and inspect the crop regularly.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1536630596251-b0c7c5b5e4e6?auto=format&fit=crop&w=700&q=80"
                        alt="Rice cultivation"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌱 Rice Blast</h3>
                        <p><span class="label">Symptoms:</span>
                        Spindle-shaped leaf spots with grey centres and brown edges.</p>
                        <p><span class="label">Prevention:</span>
                        Use balanced nutrients and seek expert advice if symptoms appear.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1595872018818-97555653a011?auto=format&fit=crop&w=700&q=80"
                        alt="Green agricultural crop"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌿 Cotton Leaf Curl</h3>
                        <p><span class="label">Symptoms:</span>
                        Leaves may curl and plant growth may become stunted.</p>
                        <p><span class="label">Prevention:</span>
                        Monitor whiteflies and use healthy seeds suitable for your region.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1499529112087-3cb3b73cec95?auto=format&fit=crop&w=700&q=80"
                        alt="Green mustard-like crop field"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌼 Mustard White Rust</h3>
                        <p><span class="label">Symptoms:</span>
                        White raised pustules may appear on leaves or other plant parts.</p>
                        <p><span class="label">Prevention:</span>
                        Inspect plants and confirm the disease before choosing treatment.</p>
                    </div>
                </div>

            </div>

            <div class="notice">
                <strong>⚠️ Important Farmer Advisory</strong><br>
                Images are illustrative and do not confirm a disease diagnosis.
                Similar symptoms can have different causes. Consult a local
                agriculture expert before applying pesticides or fungicides.
            </div>
            <div style="text-align:center; padding:25px;">
                <a href="/" style="
                    display:inline-block;
                    background:#176b3a;
                    color:white;
                    padding:14px 25px;
                    border-radius:8px;
                    text-decoration:none;
                    font-weight:bold;">
                    🏠 Back to Home
                </a>
            </div>

        </section>

        <footer>
            <h3>🌱 Agriculture Help and Management System</h3>
            <p>Helping farmers make informed crop-management decisions.</p>
        </footer>

    </body>
    </html>
    """)
@app.route("/tips")
def tips():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Smart Farming Tips | AgriCare</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f3f8f0;
                color: #263b2a;
            }

            nav {
                background: #176b3a;
                color: white;
                padding: 18px 7%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                gap: 12px;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin-left: 18px;
                font-weight: bold;
            }

            .hero {
                min-height: 360px;
                padding: 65px 8%;
                display: flex;
                align-items: center;
                color: white;
                background:
                    linear-gradient(90deg, rgba(0,45,20,.88),
                    rgba(0,45,20,.15)),
                    url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1600&q=85")
                    center/cover;
            }

            .hero-content {
                max-width: 600px;
            }

            .hero h1 {
                font-size: clamp(32px, 5vw, 48px);
                margin-bottom: 16px;
            }

            .hero p {
                font-size: 18px;
                line-height: 1.7;
                margin-bottom: 22px;
            }

            .btn {
                display: inline-block;
                background: #f4c542;
                color: #173d24;
                padding: 13px 22px;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
            }

            .section {
                max-width: 1150px;
                margin: auto;
                padding: 45px 20px;
            }

            .section-title {
                text-align: center;
                color: #176b3a;
                font-size: 32px;
                margin-bottom: 12px;
            }

            .subtitle {
                text-align: center;
                color: #607267;
                margin-bottom: 32px;
                line-height: 1.6;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
                gap: 24px;
            }

            .card {
                background: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 5px 18px rgba(0,0,0,.08);
                transition: transform .25s, box-shadow .25s;
            }

            .card:hover {
                transform: translateY(-7px);
                box-shadow: 0 12px 25px rgba(0,0,0,.15);
            }

            .card img {
                width: 100%;
                height: 190px;
                object-fit: cover;
                display: block;
            }

            .card-content {
                padding: 22px;
            }

            .card h3 {
                color: #176b3a;
                font-size: 21px;
                margin-bottom: 12px;
            }

            .card p {
                line-height: 1.7;
                font-size: 15px;
            }

            .bottom {
                background: #e0efdc;
                text-align: center;
                padding: 30px 15px;
                border-radius: 12px;
                margin-top: 35px;
            }

            .bottom h3 {
                color: #176b3a;
                margin-bottom: 12px;
            }

            .bottom p {
                line-height: 1.7;
                margin-bottom: 18px;
            }

            footer {
                text-align: center;
                background: #124d2b;
                color: white;
                padding: 24px;
                line-height: 1.8;
            }

            @media(max-width: 600px) {
                nav {
                    flex-direction: column;
                    text-align: center;
                }

                nav a {
                    margin: 8px;
                    display: inline-block;
                }

                .hero {
                    padding: 45px 6%;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <h2>🌱 AgriCare</h2>
            <div>
                <a href="/">Home</a>
                <a href="/crops">Crops</a>
                <a href="/fertilizer">Fertilizer</a>
                <a href="/diseases">Crop Diseases</a>
            </div>
        </nav>

        <section class="hero">
            <div class="hero-content">
                <h1>Smart Farming, Better Future 🌾</h1>
                <p>
                    Discover practical farming tips to manage water,
                    improve soil health and take better care of your crops.
                </p>
                <a href="#tips" class="btn">Explore Farming Tips ↓</a>
            </div>
        </section>

        <section class="section" id="tips">

            <h2 class="section-title">Smart Farming Guide</h2>

            <p class="subtitle">
                Simple practices for informed and sustainable farming.
            </p>

            <div class="grid">

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1560493676-04071c5f467b?auto=format&fit=crop&w=700&q=80"
                        alt="Irrigation in agriculture"
                        loading="lazy">

                    <div class="card-content">
                        <h3>💧 Water Management</h3>
                        <p>Check soil moisture and crop needs before irrigation. Avoid waterlogging and unnecessary water use.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=700&q=80"
                        alt="Agricultural field"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌱 Soil Health</h3>
                        <p>Get soil tested and use the results to guide fertilizer and nutrient management.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?auto=format&fit=crop&w=700&q=80"
                        alt="Growing crops"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌾 Quality Seeds</h3>
                        <p>Choose certified seeds and crop varieties suitable for your region and sowing season.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1499529112087-3cb3b73cec95?auto=format&fit=crop&w=700&q=80"
                        alt="Green plants"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🐛 Pest Monitoring</h3>
                        <p>Inspect leaves and stems regularly. Identify pests correctly before selecting a control method.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=700&q=80"
                        alt="Farm produce"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌿 Fertilizer Planning</h3>
                        <p>Apply fertilizers according to soil-test results, crop needs and local agricultural guidance.</p>
                    </div>
                </div>

                <div class="card">
                    <img
                        src="https://images.unsplash.com/photo-1511497584788-876760111969?auto=format&fit=crop&w=700&q=80"
                        alt="Nature and environment"
                        loading="lazy">

                    <div class="card-content">
                        <h3>🌦️ Weather Planning</h3>
                        <p>Check the local weather forecast before planning irrigation, spraying or harvesting.</p>
                    </div>
                </div>

            </div>

            <div class="bottom">
                <h3>🌍 Take Care of Your Farm</h3>
                <p>
                    Healthy soil, suitable seeds, careful irrigation and
                    regular crop inspection can support better farm management.
                </p>
                <a href="/" class="btn">Back to Home 🏠</a>
            </div>
            <div style="text-align:center; padding:25px;">
                <a href="/" style="
                    display:inline-block;
                    background:#176b3a;
                    color:white;
                    padding:14px 25px;
                    border-radius:8px;
                    text-decoration:none;
                    font-weight:bold;">
                    🏠 Back to Home
                </a>
            </div>

        </section>

        <footer>
            <h3>🌱 Agriculture Help and Management System</h3>
            <p>Smart information for farmers and sustainable agriculture.</p>
        </footer>

    </body>
    </html>
    """)
if __name__ == "__main__":
    app.run(debug=True)