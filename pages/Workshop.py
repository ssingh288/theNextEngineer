import streamlit as st
import streamlit.components.v1 as components
import base64, os, random

st.set_page_config(
    page_title="Data Analytics Workshop — 18 Apr 2026 · ₹100",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header                    { visibility: hidden !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"]               { display: none !important; }
.main .block-container                       { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stMain"]                { padding: 0 !important; overflow: hidden !important; }
.stApp                                       { background: #080810 !important; overflow: hidden !important; }
.element-container, .stMarkdown              { padding: 0 !important; margin: 0 !important; }
iframe                                       { display: block; border: none;
                                               width: 100vw !important;
                                               height: 100vh !important;
                                               min-height: 100vh !important; }
html, body                                   { overflow: hidden !important; margin: 0 !important; padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

_img_path = os.path.join(os.path.dirname(__file__), "..", "Sandeep.PNG")
with open(_img_path, "rb") as _f:
    SANDEEP_SRC = "data:image/png;base64," + base64.b64encode(_f.read()).decode()

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyIahJO9hJNTd4Z08Xi7S2RtkOTZUgCxQ0xaELMFrK68lpxcdsFrEkBV-w2SXX6e-5T/exec"
PAYMENT_LINK    = "https://rzp.io/rzp/XTP0oz9"

random.seed(99)
star_styles, star_divs = [], []
for i in range(120):
    x, y   = random.uniform(0, 100), random.uniform(0, 100)
    size   = random.uniform(0.8, 2.2)
    dly    = random.uniform(0, 8)
    dur    = random.uniform(2, 6)
    op     = random.uniform(0.10, 0.70)
    star_styles.append(f".s{i}{{left:{x:.1f}%;top:{y:.1f}%;}}")
    star_divs.append(
        f'<div class="star s{i}" style="width:{size:.1f}px;height:{size:.1f}px;'
        f'animation-delay:{dly:.1f}s;animation-duration:{dur:.1f}s;opacity:{op:.2f}"></div>'
    )
STARS_CSS  = "\n".join(star_styles)
STARS_HTML = "\n".join(star_divs)

page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
    font-family: 'Manrope', sans-serif;
    background: #080810;
    color: #ffffff;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
}}
::-webkit-scrollbar       {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: #080810; }}
::-webkit-scrollbar-thumb {{ background: #0047ff; border-radius: 2px; }}

/* Stars */
.star {{
    position: fixed; border-radius: 50%;
    background: rgba(180,210,255,1);
    pointer-events: none; z-index: 0;
    animation: twinkle linear infinite alternate;
}}
@keyframes twinkle {{
    from {{ opacity: 0.05; transform: scale(0.8); }}
    to   {{ opacity: 1;    transform: scale(1.2); }}
}}
{STARS_CSS}

.atmos {{
    position: fixed; top: -300px; left: 50%; transform: translateX(-50%);
    width: 800px; height: 800px; border-radius: 50%;
    background: conic-gradient(from 0deg at 50% 50%, #0047ff 46deg, #06003a 226deg);
    filter: blur(130px); opacity: 0.14;
    z-index: 0; pointer-events: none;
}}

/* Layout */
.wrap {{ position: relative; z-index: 1; max-width: 720px; margin: 0 auto; padding: 0 24px 120px; }}

/* ── HERO ── */
.hero {{
    text-align: center;
    padding: 64px 0 48px;
}}
.badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,100,255,0.30);
    border-radius: 100px; padding: 8px 20px;
    font-family: 'Space Mono', monospace; font-size: 12px;
    color: #4f9eff; margin-bottom: 28px;
}}
.badge-dot {{
    width: 8px; height: 8px; border-radius: 50%;
    background: #00db57; box-shadow: 0 0 8px #00db57;
    animation: pulse 2s infinite;
}}
@keyframes pulse {{
    0%,100% {{ opacity:1; transform:scale(1); }}
    50%     {{ opacity:0.4; transform:scale(1.5); }}
}}
.hero-h1 {{
    font-size: clamp(32px, 6vw, 58px); font-weight: 800;
    letter-spacing: -0.055em; line-height: 1.05;
    margin-bottom: 20px; color: #fff;
}}
.hero-h1 .cyan {{ color: #00d4ff; }}
.hero-sub {{
    font-size: 17px; color: rgba(255,255,255,0.60);
    line-height: 1.65; max-width: 560px;
    margin: 0 auto 36px;
}}
.price-row {{
    display: flex; align-items: center; justify-content: center;
    gap: 12px; margin-bottom: 28px;
}}
.price {{
    font-size: 42px; font-weight: 800; letter-spacing: -0.05em; color: #fff;
}}
.price-note {{
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: rgba(255,255,255,0.40); line-height: 1.5; text-align: left;
}}
.cta-btn {{
    display: inline-flex; align-items: center; gap: 10px;
    background: #0047ff; color: #fff;
    padding: 18px 40px; border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 800;
    letter-spacing: -0.02em; cursor: pointer; text-decoration: none;
    transition: background 0.2s, box-shadow 0.2s, transform 0.15s;
    box-shadow: 0 0 40px rgba(0,71,255,0.40);
}}
.cta-btn:hover {{
    background: #4f9eff; box-shadow: 0 0 60px rgba(0,71,255,0.55);
    transform: translateY(-2px);
}}
.seats-note {{
    margin-top: 14px;
    font-family: 'Space Mono', monospace; font-size: 12px;
    color: rgba(255,255,255,0.35);
}}
.seats-note span {{ color: #00db57; }}

/* ── COUNTDOWN ── */
.countdown-wrap {{
    display: flex; justify-content: center; gap: 16px;
    margin: 40px 0 0;
}}
.cd-block {{
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px; padding: 16px 20px; min-width: 72px; text-align: center;
}}
.cd-num {{
    font-size: 32px; font-weight: 800; letter-spacing: -0.05em;
    color: #fff; line-height: 1;
    font-family: 'Space Mono', monospace;
}}
.cd-lbl {{
    font-family: 'Space Mono', monospace; font-size: 10px;
    color: rgba(255,255,255,0.35); letter-spacing: 0.08em;
    text-transform: uppercase; margin-top: 6px;
}}

/* ── DIVIDER ── */
hr.glow {{
    border: none; height: 1px;
    background: #0047ff;
    box-shadow: 0 0 60px 6px #0047ff, 0 0 160px 12px rgba(0,71,255,0.3);
    margin: 56px 0;
}}

/* ── SECTION ── */
.sec-label {{
    font-family: 'Space Mono', monospace; font-size: 11px;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: #4f9eff; margin-bottom: 14px; display: block;
}}
.sec-title {{
    font-size: clamp(24px, 4vw, 36px); font-weight: 800;
    letter-spacing: -0.05em; line-height: 1.1;
    margin-bottom: 32px;
}}

/* ── LEARN LIST ── */
.learn-list {{ list-style: none; display: flex; flex-direction: column; gap: 16px; }}
.learn-item {{
    display: flex; align-items: flex-start; gap: 14px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px; padding: 18px 20px;
}}
.learn-icon {{
    font-size: 22px; flex-shrink: 0; margin-top: 2px;
}}
.learn-text strong {{ display: block; font-size: 15px; font-weight: 700; margin-bottom: 3px; color: #fff; }}
.learn-text span   {{ font-size: 13px; color: rgba(255,255,255,0.50); line-height: 1.5; }}

/* ── INSTRUCTOR ── */
.instructor-card {{
    display: flex; align-items: center; gap: 28px;
    background: rgba(15,15,30,1); border: 1px solid rgba(0,100,255,0.25);
    border-radius: 20px; padding: 28px 32px;
    position: relative; overflow: hidden;
}}
.instructor-card::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, #0047ff, #00d4ff, transparent);
}}
.instructor-img {{
    width: 90px; height: 90px; border-radius: 50%;
    object-fit: cover; object-position: top;
    border: 2px solid rgba(0,100,255,0.40); flex-shrink: 0;
}}
.instructor-name {{ font-size: 18px; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 4px; }}
.instructor-role {{ font-family: 'Space Mono', monospace; font-size: 11px; color: #4f9eff; margin-bottom: 10px; }}
.instructor-bio  {{ font-size: 13px; color: rgba(255,255,255,0.55); line-height: 1.6; }}

/* ── DETAILS BOX ── */
.details-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
}}
.detail-item {{
    display: flex; align-items: center; gap: 12px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 16px 18px;
}}
.detail-icon {{ font-size: 20px; flex-shrink: 0; }}
.detail-text strong {{ display: block; font-size: 13px; font-weight: 700; color: #fff; }}
.detail-text span   {{ font-size: 12px; color: rgba(255,255,255,0.45); font-family: 'Space Mono', monospace; }}

/* ── STICKY BOTTOM CTA ── */
.sticky-cta {{
    position: fixed; bottom: 0; left: 0; right: 0; z-index: 500;
    background: rgba(8,8,16,0.95); backdrop-filter: blur(16px);
    border-top: 1px solid rgba(0,100,255,0.25);
    padding: 16px 24px;
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
}}
.sticky-info {{ display: flex; flex-direction: column; gap: 2px; }}
.sticky-info strong {{ font-size: 15px; font-weight: 800; color: #fff; }}
.sticky-info span   {{ font-size: 12px; color: rgba(255,255,255,0.45); font-family: 'Space Mono', monospace; }}
.sticky-btn {{
    display: inline-flex; align-items: center; gap: 8px;
    background: #0047ff; color: #fff;
    padding: 13px 28px; border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 800;
    cursor: pointer; white-space: nowrap;
    transition: background 0.2s, box-shadow 0.2s;
    box-shadow: 0 0 30px rgba(0,71,255,0.40);
}}
.sticky-btn:hover {{ background: #4f9eff; box-shadow: 0 0 50px rgba(0,71,255,0.55); }}

/* ── MODAL (reused) ── */
.reg-modal {{
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(8,8,16,0.92); backdrop-filter: blur(8px);
    align-items: center; justify-content: center; padding: 20px;
}}
.reg-card {{
    background: #0f0f1e; border: 1px solid rgba(0,100,255,0.35);
    border-radius: 24px; padding: 48px 40px; width: 100%; max-width: 440px;
    position: relative; box-shadow: 0 0 80px rgba(0,71,255,0.15);
}}
.reg-card::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, #0047ff, #00d4ff, transparent);
}}
.reg-close {{
    position: absolute; top: 16px; right: 20px;
    background: none; border: none; cursor: pointer;
    font-size: 24px; color: rgba(255,255,255,0.4); line-height: 1; transition: color 0.2s;
}}
.reg-close:hover {{ color: #fff; }}
.reg-title {{ font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: #fff; margin-bottom: 6px; }}
.reg-sub   {{ font-size: 13px; color: rgba(255,255,255,0.50); margin-bottom: 28px; line-height: 1.55; }}
.reg-label {{
    display: block; font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 0.10em; text-transform: uppercase;
    color: #4f9eff; margin-bottom: 8px;
}}
.reg-input {{
    width: 100%; padding: 13px 16px;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.10);
    border-radius: 12px; font-family: 'Manrope', sans-serif;
    font-size: 14px; color: #fff; outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    margin-bottom: 20px; box-sizing: border-box;
}}
.reg-input::placeholder {{ color: rgba(255,255,255,0.22); }}
.reg-input:focus {{ border-color: rgba(0,100,255,0.50); box-shadow: 0 0 0 3px rgba(0,71,255,0.12); }}
.reg-input option {{ background: #1a1a2e; color: #fff; }}
.reg-input option:disabled {{ color: rgba(255,255,255,0.35); }}
.reg-submit {{
    width: 100%; padding: 15px; background: #0047ff; color: #fff;
    border: none; border-radius: 100px; font-family: 'Manrope', sans-serif;
    font-size: 15px; font-weight: 700; letter-spacing: -0.02em;
    cursor: pointer; transition: background 0.2s, box-shadow 0.2s;
}}
.reg-submit:hover:not(:disabled) {{ background: #4f9eff; box-shadow: 0 0 40px rgba(0,71,255,0.4); }}
.reg-submit:disabled {{ opacity: 0.6; cursor: not-allowed; }}
.reg-note {{ text-align: center; font-size: 11px; color: rgba(255,255,255,0.25); margin-top: 16px; font-family: 'Space Mono', monospace; }}

@keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(20px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
.fade {{ animation: fadeUp 0.7s ease both; }}
.fade-1 {{ animation-delay: 0.05s; }}
.fade-2 {{ animation-delay: 0.15s; }}
.fade-3 {{ animation-delay: 0.25s; }}
.fade-4 {{ animation-delay: 0.35s; }}

@media (max-width: 600px) {{
    .details-grid {{ grid-template-columns: 1fr; }}
    .instructor-card {{ flex-direction: column; text-align: center; }}
    .sticky-cta {{ flex-direction: column; text-align: center; gap: 10px; }}
    .sticky-btn {{ width: 100%; justify-content: center; }}
    .countdown-wrap {{ gap: 10px; }}
    .cd-block {{ min-width: 60px; padding: 12px 14px; }}
    .cd-num {{ font-size: 26px; }}
}}
</style>
</head>
<body>

{STARS_HTML}
<div class="atmos"></div>

<div class="wrap">

  <!-- ── HERO ── -->
  <div class="hero">
    <div class="badge fade fade-1">
      <span class="badge-dot"></span>
      Live Online &nbsp;·&nbsp; Saturday, 18 April 2026
    </div>

    <h1 class="hero-h1 fade fade-2">
      Your First Step into<br><span class="cyan">Data Analytics</span>
    </h1>

    <p class="hero-sub fade fade-3">
      A hands-on 2-hour workshop where you'll see exactly how data analysts work —
      real tools, real data, zero fluff. Walk away knowing if this career is for you.
    </p>

    <div class="price-row fade fade-4">
      <div class="price">₹100</div>
      <div class="price-note">One-time entry fee<br>Seats fill fast</div>
    </div>

    <button onclick="openRegModal()" class="cta-btn fade fade-4">
      Reserve My Seat →
    </button>
    <p class="seats-note fade fade-4">⚡ Only <span>20 seats</span> available</p>

    <!-- Countdown -->
    <div class="countdown-wrap fade fade-4">
      <div class="cd-block"><div class="cd-num" id="cd-days">--</div><div class="cd-lbl">Days</div></div>
      <div class="cd-block"><div class="cd-num" id="cd-hours">--</div><div class="cd-lbl">Hours</div></div>
      <div class="cd-block"><div class="cd-num" id="cd-mins">--</div><div class="cd-lbl">Mins</div></div>
      <div class="cd-block"><div class="cd-num" id="cd-secs">--</div><div class="cd-lbl">Secs</div></div>
    </div>
  </div>

  <hr class="glow"/>

  <!-- ── WHAT YOU'LL LEARN ── -->
  <section>
    <span class="sec-label">// what you'll walk away with</span>
    <h2 class="sec-title">4 things you'll learn<br>in 2 hours</h2>
    <ul class="learn-list">
      <li class="learn-item">
        <span class="learn-icon">📊</span>
        <div class="learn-text">
          <strong>What Data Analytics actually is</strong>
          <span>No jargon. You'll see what a data analyst does on a real Monday morning at work.</span>
        </div>
      </li>
      <li class="learn-item">
        <span class="learn-icon">🐍</span>
        <div class="learn-text">
          <strong>Your first Python + SQL query — live</strong>
          <span>We'll pull real data and answer a real business question together, step by step.</span>
        </div>
      </li>
      <li class="learn-item">
        <span class="learn-icon">📈</span>
        <div class="learn-text">
          <strong>How to turn numbers into a story</strong>
          <span>See how pros build charts that actually convince managers to take action.</span>
        </div>
      </li>
      <li class="learn-item">
        <span class="learn-icon">🗺️</span>
        <div class="learn-text">
          <strong>Your personal roadmap to become an analyst</strong>
          <span>What to learn, in what order, and how long it realistically takes — no BS.</span>
        </div>
      </li>
    </ul>
  </section>

  <hr class="glow"/>

  <!-- ── INSTRUCTOR ── -->
  <section>
    <span class="sec-label">// your instructor</span>
    <div class="instructor-card">
      <img src="{SANDEEP_SRC}" alt="Sandeep Singh" class="instructor-img"/>
      <div>
        <div class="instructor-name">Sandeep Singh</div>
        <div class="instructor-role">Founder · The Next Engineer</div>
        <p class="instructor-bio">
          Trained 500+ students across France, Sweden &amp; India. Worked with
          Nova.space, Ironhack, Guardant Health and Cognizant.
          This isn't theory — everything I teach, I've done at work.
        </p>
      </div>
    </div>
  </section>

  <hr class="glow"/>

  <!-- ── DETAILS ── -->
  <section>
    <span class="sec-label">// workshop details</span>
    <h2 class="sec-title">Everything you need to know</h2>
    <div class="details-grid">
      <div class="detail-item">
        <span class="detail-icon">📅</span>
        <div class="detail-text">
          <strong>Saturday, 18 April 2026</strong>
          <span>10:30 AM — 12:30 PM IST</span>
        </div>
      </div>
      <div class="detail-item">
        <span class="detail-icon">💻</span>
        <div class="detail-text">
          <strong>100% Online</strong>
          <span>Google Meet · Link sent on email</span>
        </div>
      </div>
      <div class="detail-item">
        <span class="detail-icon">🎯</span>
        <div class="detail-text">
          <strong>Hands-on session</strong>
          <span>Live coding · Q&amp;A included</span>
        </div>
      </div>
      <div class="detail-item">
        <span class="detail-icon">🎟️</span>
        <div class="detail-text">
          <strong>Only ₹100 entry</strong>
          <span>20 seats · First come first served</span>
        </div>
      </div>
      <div class="detail-item">
        <span class="detail-icon">📹</span>
        <div class="detail-text">
          <strong>Recording provided</strong>
          <span>Watch back anytime after the session</span>
        </div>
      </div>
      <div class="detail-item">
        <span class="detail-icon">🚀</span>
        <div class="detail-text">
          <strong>No prior experience needed</strong>
          <span>Just bring curiosity &amp; a laptop</span>
        </div>
      </div>
    </div>
  </section>

  <hr class="glow"/>

  <!-- ── FINAL CTA ── -->
  <section style="text-align:center;padding:16px 0 40px;">
    <h2 style="font-size:clamp(26px,5vw,40px);font-weight:800;letter-spacing:-0.05em;margin-bottom:12px;">
      Don't think too long —<br>seats go fast.
    </h2>
    <p style="font-size:15px;color:rgba(255,255,255,0.50);margin-bottom:32px;line-height:1.6;">
      ₹100 is less than a coffee. Two hours could change your career.
    </p>
    <button onclick="openRegModal()" class="cta-btn">
      Reserve My Seat — ₹100 →
    </button>
  </section>

</div><!-- /wrap -->

<!-- ── STICKY BOTTOM BAR ── -->
<div class="sticky-cta">
  <div class="sticky-info">
    <strong>Data Analytics Workshop</strong>
    <span>18 Apr 2026 · 10:30 AM · ₹100 · 20 seats only</span>
  </div>
  <button onclick="openRegModal()" class="sticky-btn">Reserve My Seat →</button>
</div>

<!-- ── REGISTRATION MODAL ── -->
<div id="reg-modal" class="reg-modal">
  <div class="reg-card">
    <button class="reg-close" onclick="closeRegModal()" aria-label="Close">&times;</button>
    <p class="reg-title">Reserve Your Seat</p>
    <p class="reg-sub">
      Workshop — ₹100 &nbsp;·&nbsp; Saturday, 18 April 2026 &nbsp;·&nbsp; 10:30 AM<br>
      Fill in your details — you'll be redirected to pay.
    </p>
    <form id="reg-form">
      <label class="reg-label" for="reg-name">Full Name</label>
      <input class="reg-input" type="text" id="reg-name" placeholder="Your name" required />

      <label class="reg-label" for="reg-email">Email Address</label>
      <input class="reg-input" type="email" id="reg-email" placeholder="you@email.com" required />

      <label class="reg-label" for="reg-phone">Phone Number</label>
      <input class="reg-input" type="tel" id="reg-phone" placeholder="+91 98765 43210" required />

      <label class="reg-label" for="reg-status">Current Status</label>
      <select class="reg-input" id="reg-status" required style="cursor:pointer;">
        <option value="" disabled selected>Select your status…</option>
        <option value="Working Professional">Working Professional</option>
        <option value="Looking for a Job">Looking for a Job</option>
      </select>

      <button type="submit" class="reg-submit" id="reg-submit">Proceed to Payment →</button>
    </form>
    <p class="reg-note">Your info is only used to send you workshop details.</p>
  </div>
</div>

<script>
var APPS_SCRIPT_URL = "{APPS_SCRIPT_URL}";
var PAYMENT_LINK    = "{PAYMENT_LINK}";

// ── Countdown to 18 Apr 2026 10:30 AM IST (UTC+5:30) ──
var target = new Date("2026-04-18T05:00:00Z"); // 10:30 AM IST
function tick() {{
  var now  = new Date();
  var diff = target - now;
  if (diff <= 0) {{
    document.querySelector('.countdown-wrap').style.display = 'none';
    return;
  }}
  var d = Math.floor(diff / 86400000);
  var h = Math.floor((diff % 86400000) / 3600000);
  var m = Math.floor((diff % 3600000)  / 60000);
  var s = Math.floor((diff % 60000)    / 1000);
  document.getElementById('cd-days').textContent  = String(d).padStart(2,'0');
  document.getElementById('cd-hours').textContent = String(h).padStart(2,'0');
  document.getElementById('cd-mins').textContent  = String(m).padStart(2,'0');
  document.getElementById('cd-secs').textContent  = String(s).padStart(2,'0');
}}
tick();
setInterval(tick, 1000);

// ── Modal ──
function openRegModal() {{
  document.getElementById('reg-modal').style.display = 'flex';
}}
function closeRegModal() {{
  document.getElementById('reg-modal').style.display = 'none';
  document.getElementById('reg-form').reset();
  var b = document.getElementById('reg-submit');
  if (b) {{ b.textContent = 'Proceed to Payment \u2192'; b.disabled = false; }}
}}
document.addEventListener('DOMContentLoaded', function() {{
  document.getElementById('reg-modal').addEventListener('click', function(e) {{
    if (e.target === this) closeRegModal();
  }});
  document.getElementById('reg-form').addEventListener('submit', function(e) {{
    e.preventDefault();
    var btn = document.getElementById('reg-submit');
    btn.textContent = 'Saving…'; btn.disabled = true;
    var body = 'name='   + encodeURIComponent(document.getElementById('reg-name').value.trim())
             + '&email=' + encodeURIComponent(document.getElementById('reg-email').value.trim())
             + '&phone=' + encodeURIComponent(document.getElementById('reg-phone').value.trim())
             + '&status='+ encodeURIComponent(document.getElementById('reg-status').value);
    fetch(APPS_SCRIPT_URL, {{
      method: 'POST', mode: 'no-cors',
      headers: {{'Content-Type': 'application/x-www-form-urlencoded'}},
      body: body
    }}).finally(function() {{
      closeRegModal();
      window.open(PAYMENT_LINK, '_blank');
    }});
  }});
}});

// ── Fill viewport ──
function resizeIframe() {{
  if (window.frameElement) {{
    window.frameElement.style.height   = window.parent.innerHeight + 'px';
    window.frameElement.style.width    = '100%';
    window.frameElement.style.display  = 'block';
    window.frameElement.style.border   = 'none';
    window.frameElement.style.position = 'fixed';
    window.frameElement.style.top      = '0';
    window.frameElement.style.left     = '0';
    window.frameElement.style.zIndex   = '9999';
  }}
}}
window.addEventListener('load',   resizeIframe);
window.addEventListener('resize', resizeIframe);
</script>
</body>
</html>
"""

components.html(page, height=900, scrolling=True)
