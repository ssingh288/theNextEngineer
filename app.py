import streamlit as st
import streamlit.components.v1 as components
import random
import base64
import os

st.set_page_config(
    page_title="The Next Engineer — Online Coding Bootcamp",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip all Streamlit chrome and make the iframe fill the full viewport
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

FORM_URL  = "https://docs.google.com/forms/d/e/1FAIpQLSclF7YODQUuzhHzsudwYSHinMRQswR2y9aSHh9SHaRfwnIH-g/viewform?usp=sharing&ouid=109749639989339515327"
WA_NUMBER = "918019101592"
WA_MSG    = "Hello%2C%20I%27m%20interested%20in%20The%20Next%20Engineer%20bootcamp!"
WA_URL    = f"https://wa.me/{WA_NUMBER}?text={WA_MSG}"

# Embed photo as base64 so it loads inside Streamlit's iframe
_img_path = os.path.join(os.path.dirname(__file__), "Sandeep.PNG")
with open(_img_path, "rb") as _f:
    SANDEEP_SRC = "data:image/png;base64," + base64.b64encode(_f.read()).decode()

# ── CSS star elements generated in Python ──────────────────────────────────────
random.seed(42)
star_styles, star_divs = [], []
for i in range(180):
    x, y   = random.uniform(0, 100), random.uniform(0, 100)
    size   = random.uniform(0.8, 2.4)
    dly    = random.uniform(0, 8)
    dur    = random.uniform(2, 6)
    op     = random.uniform(0.15, 0.80)
    star_styles.append(f".s{i}{{left:{x:.1f}%;top:{y:.1f}%;}}")
    star_divs.append(
        f'<div class="star s{i}" style="width:{size:.1f}px;height:{size:.1f}px;'
        f'animation-delay:{dly:.1f}s;animation-duration:{dur:.1f}s;opacity:{op:.2f}"></div>'
    )
STARS_CSS  = "\n".join(star_styles)
STARS_HTML = "\n".join(star_divs)

# ── All hardcoded colour values (no CSS vars — Streamlit overrides :root) ──────
WHITE       = "#ffffff"
W80         = "rgba(255,255,255,0.85)"
W50         = "rgba(255,255,255,0.60)"   # bumped from 0.50 → more readable
W20         = "rgba(255,255,255,0.22)"
BLUE        = "#0047ff"
BLUE_B      = "#4f9eff"                  # bumped brightness for visibility
CYAN        = "#00d4ff"
GREEN       = "#00db57"
BG          = "#080810"
BG_CARD     = "#0f0f1e"
BORDER      = "rgba(255,255,255,0.10)"
BORDER_BLUE = "rgba(0,100,255,0.35)"
BLUE_GLOW   = "rgba(0,71,255,0.40)"

page = f"""
<style>
/* ════════════════════════════════════════════════════════
   STREAMLIT CHROME RESET — force white text everywhere
   ════════════════════════════════════════════════════════ */
#MainMenu, footer, header                   {{ visibility: hidden !important; }}
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"]              {{ display: none !important; }}
.main .block-container                      {{ padding: 0 !important; max-width: 100% !important; }}
section[data-testid="stMain"]              {{ padding: 0 !important; }}

/* Override Streamlit's default grey text on every wrapper */
.stApp,
.stApp *,
[data-testid="stAppViewContainer"],
[data-testid="stVerticalBlock"],
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] div  {{
    color: {WHITE} !important;
    font-family: 'Manrope', sans-serif !important;
}}

.stApp  {{ background: {BG} !important; }}

/* ════════════════════════════════════════════════════════
   GOOGLE FONTS
   ════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');

/* ════════════════════════════════════════════════════════
   BASE
   ════════════════════════════════════════════════════════ */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html  {{ scroll-behavior: smooth; }}
body  {{
    font-family: 'Manrope', sans-serif !important;
    background: {BG} !important;
    color: {WHITE} !important;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
}}
::-webkit-scrollbar       {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {BLUE}; border-radius: 2px; }}

/* ════════════════════════════════════════════════════════
   STARS
   ════════════════════════════════════════════════════════ */
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

/* ════════════════════════════════════════════════════════
   ATMOSPHERIC GLOW
   ════════════════════════════════════════════════════════ */
.atmos {{
    position: fixed; top: -350px; left: 50%;
    transform: translateX(-50%);
    width: 900px; height: 900px; border-radius: 50%;
    background: conic-gradient(from 0deg at 50% 50%, #0047ff 46deg, #06003a 226deg);
    filter: blur(140px); opacity: 0.16;
    z-index: 0; pointer-events: none;
}}

/* ════════════════════════════════════════════════════════
   WORKSHOP ANNOUNCEMENT BANNER  (fixed top strip)
   ════════════════════════════════════════════════════════ */
.ws-banner {{
    position: fixed; top: 0; left: 0; right: 0;
    z-index: 200;
    background: linear-gradient(90deg, #0a0a20, #0d1640, #0a0a20);
    border-bottom: 1px solid {BORDER_BLUE};
    padding: 10px 24px;
    display: flex; align-items: center; justify-content: center;
    gap: 16px; flex-wrap: wrap;
    box-shadow: 0 2px 40px rgba(0,71,255,0.25);
}}
.ws-banner-pulse {{
    width: 8px; height: 8px; border-radius: 50%;
    background: {GREEN}; box-shadow: 0 0 10px {GREEN};
    animation: pulse 2s infinite; flex-shrink: 0;
}}
@keyframes pulse {{
    0%,100% {{ opacity:1; transform:scale(1); }}
    50%     {{ opacity:0.4; transform:scale(1.5); }}
}}
.ws-banner-text {{
    font-family: 'Manrope', sans-serif;
    font-size: 13px; font-weight: 600;
    color: {WHITE} !important;
    letter-spacing: -0.01em;
}}
.ws-banner-text .ws-date {{
    color: {CYAN} !important;
    font-weight: 700;
}}
.ws-banner-btn {{
    display: inline-flex; align-items: center; gap: 6px;
    background: {BLUE}; color: {WHITE} !important;
    padding: 6px 16px; border-radius: 100px;
    font-family: 'Manrope', sans-serif;
    font-size: 12px; font-weight: 700;
    text-decoration: none; white-space: nowrap;
    transition: background 0.2s, box-shadow 0.2s;
}}
.ws-banner-btn:hover {{
    background: {BLUE_B};
    box-shadow: 0 0 20px {BLUE_GLOW};
    color: {WHITE} !important;
}}
.ws-banner-sep {{
    color: {W20} !important;
    font-size: 16px;
}}

/* ════════════════════════════════════════════════════════
   NAV  (sits below the 44px banner)
   ════════════════════════════════════════════════════════ */
.tne-header {{
    position: fixed; top: 44px; left: 0; right: 0;
    z-index: 100;
    display: flex; align-items: center; justify-content: center;
    padding: 16px 40px;
    background: rgba(8,8,16,0.85);
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid {BORDER};
}}
.tne-brand {{
    display: flex; align-items: center; gap: 10px; text-decoration: none;
}}
.tne-brand-icon {{
    width: 34px; height: 34px;
    background: linear-gradient(135deg, {BLUE}, {CYAN});
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Mono', monospace; font-size: 12px; font-weight: 700;
    color: {WHITE} !important; flex-shrink: 0;
}}
.tne-brand-name {{
    font-size: 16px; font-weight: 800; letter-spacing: -0.03em;
    color: {WHITE} !important;
}}
.tne-brand-name span {{ color: {BLUE_B} !important; }}

/* ════════════════════════════════════════════════════════
   PAGE WRAPPER  (top padding for banner + nav)
   ════════════════════════════════════════════════════════ */
.tne-page {{ position: relative; z-index: 1; padding-top: 104px; }}

/* ════════════════════════════════════════════════════════
   WHATSAPP FLOAT
   ════════════════════════════════════════════════════════ */
.wa-float {{
    position: fixed; bottom: 28px; right: 28px; z-index: 999;
    width: 56px; height: 56px; border-radius: 50%;
    background: #25D366;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 24px rgba(37,211,102,0.5);
    text-decoration: none;
    transition: transform 0.2s, box-shadow 0.2s;
}}
.wa-float:hover {{ transform: scale(1.1); box-shadow: 0 8px 32px rgba(37,211,102,0.65); }}
.wa-float svg {{ width: 28px; height: 28px; fill: white; }}

/* ════════════════════════════════════════════════════════
   SECTION COMMON
   ════════════════════════════════════════════════════════ */
.sec {{ position: relative; z-index: 1; }}
.sec-inner {{ max-width: 1180px; margin: 0 auto; padding: 96px 60px; }}
.sec-label {{
    font-family: 'Space Mono', monospace; font-size: 11px;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: {BLUE_B} !important; margin-bottom: 16px; display: block;
}}
.sec-title {{
    font-size: clamp(32px, 4vw, 52px); font-weight: 800;
    letter-spacing: -0.05em; line-height: 1.1;
    color: {WHITE} !important;
}}
.sec-sub {{
    font-size: 17px; color: {W50} !important; max-width: 520px;
    line-height: 1.65; letter-spacing: -0.02em; margin-top: 14px;
}}
.glow-divider {{
    width: 100%; height: 1px; border: none;
    background: {BLUE};
    box-shadow: 0 0 80px 8px {BLUE}, 0 0 200px 16px rgba(0,71,255,0.4);
}}
.grad-text {{
    background: linear-gradient(90deg, {BLUE_B}, {CYAN});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}}

/* ════════════════════════════════════════════════════════
   BUTTONS
   ════════════════════════════════════════════════════════ */
.btn-p {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 13px 28px; background: {BLUE}; color: {WHITE} !important;
    border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 700;
    letter-spacing: -0.02em; cursor: pointer; text-decoration: none;
    transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
}}
.btn-p:hover {{
    background: {BLUE_B}; box-shadow: 0 0 40px {BLUE_GLOW};
    transform: translateY(-2px); color: {WHITE} !important;
}}
.btn-o {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 13px 28px; background: transparent; color: {W80} !important;
    border: 1px solid {BORDER}; border-radius: 100px;
    font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 600;
    letter-spacing: -0.02em; cursor: pointer; text-decoration: none;
    transition: border-color 0.2s, color 0.2s, background 0.2s;
}}
.btn-o:hover {{
    border-color: {BLUE_B}; color: {WHITE} !important;
    background: rgba(0,71,255,0.08);
}}
.btn-wa {{
    display: inline-flex; align-items: center; gap: 10px;
    padding: 14px 32px; background: #25D366; color: {WHITE} !important;
    border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 700;
    letter-spacing: -0.02em; cursor: pointer; text-decoration: none;
    transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
}}
.btn-wa:hover {{
    background: #20c05c; box-shadow: 0 0 40px rgba(37,211,102,0.4);
    transform: translateY(-2px); color: {WHITE} !important;
}}
.btn-wa svg {{ width: 20px; height: 20px; }}

/* ════════════════════════════════════════════════════════
   CARDS
   ════════════════════════════════════════════════════════ */
.card {{
    background: {BG_CARD}; border: 1px solid {BORDER};
    border-radius: 20px;
    transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
}}
.card:hover {{
    border-color: {BORDER_BLUE}; transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.5), inset 0 0 30px rgba(0,71,255,0.05);
}}


.hero-logo {{
    display: inline-flex; align-items: center; gap: 12px;
    text-decoration: none; margin-bottom: 32px;
    animation: fadeUp 0.8s ease both;
}}
.hero-logo-icon {{
    width: 48px; height: 48px;
    background: linear-gradient(135deg, {BLUE}, {CYAN});
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Mono', monospace;
    font-size: 15px; font-weight: 700; color: {WHITE} !important;
    box-shadow: 0 0 32px {BLUE_GLOW};
}}
.hero-logo-text {{
    font-size: 22px; font-weight: 800;
    letter-spacing: -0.04em; color: {WHITE} !important;
}}
.hero-logo-text span {{ color: {BLUE_B} !important; }}

/* ════════════════════════════════════════════════════════
   HERO
   ════════════════════════════════════════════════════════ */
#hero {{
    min-height: 100vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center; padding: 100px 24px 80px;
    position: relative;
}}
.hero-badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,100,255,0.30);
    border-radius: 100px; padding: 8px 18px;
    font-family: 'Space Mono', monospace; font-size: 12px;
    color: {BLUE_B} !important; margin-bottom: 36px;
    animation: fadeUp 0.8s ease both;
}}
.hero-badge-dot {{
    width: 6px; height: 6px; border-radius: 50%;
    background: {GREEN}; box-shadow: 0 0 8px {GREEN};
    animation: pulse 2s infinite;
}}
.hero-h1 {{
    font-size: clamp(44px, 7vw, 88px); font-weight: 800;
    letter-spacing: -0.055em; line-height: 1.0;
    max-width: 880px; margin-bottom: 24px;
    color: {WHITE} !important;
    animation: fadeUp 0.8s 0.1s ease both;
}}
.hero-sub {{
    font-size: 18px; font-weight: 500; color: {W50} !important;
    max-width: 520px; line-height: 1.65; letter-spacing: -0.02em;
    margin-bottom: 48px;
    animation: fadeUp 0.8s 0.2s ease both;
}}
.hero-ctas {{
    display: flex; gap: 14px; flex-wrap: wrap; justify-content: center;
    animation: fadeUp 0.8s 0.3s ease both;
}}
.hero-orbit {{
    position: absolute; bottom: -40px; left: 50%;
    transform: translateX(-50%);
    width: 360px; height: 360px; border-radius: 50%;
    border: 1px solid rgba(0,71,255,0.14); pointer-events: none;
}}
.hero-orbit::before {{
    content: ''; position: absolute; inset: 24px;
    border-radius: 50%; border: 1px solid rgba(0,71,255,0.07);
}}
.orbit-dot {{
    position: absolute; width: 8px; height: 8px;
    border-radius: 50%; background: {BLUE_B};
    box-shadow: 0 0 14px {BLUE};
    top: 50%; left: -4px; transform: translateY(-50%);
    animation: orbitDot 7s linear infinite;
}}
@keyframes orbitDot {{
    from {{ transform: translateY(-50%) rotate(0deg) translateX(180px) rotate(0deg); }}
    to   {{ transform: translateY(-50%) rotate(360deg) translateX(180px) rotate(-360deg); }}
}}
.scroll-hint {{
    position: absolute; bottom: 32px; left: 50%; transform: translateX(-50%);
    display: flex; flex-direction: column; align-items: center; gap: 8px;
    opacity: 0.35; animation: fadeIn 1s 1.2s ease both;
}}
.scroll-hint span {{
    font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 0.1em; text-transform: uppercase;
    color: {W50} !important;
}}
.scroll-arrow {{
    width: 14px; height: 14px;
    border-right: 1.5px solid {WHITE}; border-bottom: 1.5px solid {WHITE};
    transform: rotate(45deg); animation: bounce 1.5s infinite;
}}
@keyframes bounce {{
    0%,100% {{ transform: rotate(45deg) translateY(0); }}
    50%     {{ transform: rotate(45deg) translateY(5px); }}
}}
@keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(24px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
@keyframes fadeIn {{
    from {{ opacity:0; }} to {{ opacity:0.35; }}
}}


.hero-courses {{
    display: flex; flex-direction: column; align-items: center;
    gap: 14px; animation: fadeUp 0.8s 0.4s ease both;
}}
.hero-course-label {{
    font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 0.14em; text-transform: uppercase;
    color: rgba(255,255,255,0.22);
}}
.hero-course-chips {{
    display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;
}}
.course-chip {{
    display: inline-flex; align-items: center; gap: 7px;
    padding: 9px 16px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 100px; font-size: 13px; font-weight: 600;
    color: rgba(255,255,255,0.85); letter-spacing: -0.01em;
    transition: border-color 0.2s, background 0.2s;
}}
.course-chip:hover {{
    border-color: rgba(0,100,255,0.35);
    background: rgba(0,71,255,0.08);
}}
.chip-flagship {{
    border-color: rgba(0,100,255,0.35);
    background: rgba(0,71,255,0.10);
    color: #ffffff;
}}
.chip-tag {{
    font-family: 'Space Mono', monospace; font-size: 9px;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #4f9eff; background: rgba(0,71,255,0.15);
    border: 1px solid rgba(0,71,255,0.25);
    border-radius: 100px; padding: 2px 8px;
}}

/* ════════════════════════════════════════════════════════
   SCROLL REVEAL  (CSS Scroll-Driven Animations — modern browsers)
   Fallback: always visible for older browsers.
   ════════════════════════════════════════════════════════ */
@supports (animation-timeline: scroll()) {{
    .reveal {{
        animation: revealUp linear both;
        animation-timeline: view();
        animation-range: entry 0% entry 28%;
    }}
}}
@supports not (animation-timeline: scroll()) {{
    .reveal {{ opacity: 1 !important; transform: none !important; }}
}}
@keyframes revealUp {{
    from {{ opacity:0; transform:translateY(28px); }}
    to   {{ opacity:1; transform:none; }}
}}

/* ════════════════════════════════════════════════════════
   STATS
   ════════════════════════════════════════════════════════ */
.stats-wrap {{ padding: 56px 60px; max-width: 1180px; margin: 0 auto; }}
.stats-row {{
    display: grid; grid-template-columns: repeat(3, 1fr);
    background: {BG_CARD}; border: 1px solid {BORDER};
    border-radius: 20px; overflow: hidden;
}}
.stat-item {{
    padding: 48px 40px; text-align: center;
    border-right: 1px solid {BORDER};
}}
.stat-item:last-child {{ border-right: none; }}
.stat-num {{
    font-size: 64px; font-weight: 800; letter-spacing: -0.07em;
    line-height: 1; margin-bottom: 8px;
    background: linear-gradient(135deg, {WHITE}, {BLUE_B});
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}}
.stat-lbl {{
    font-family: 'Space Mono', monospace; font-size: 12px;
    color: {W50} !important; letter-spacing: 0.06em; text-transform: uppercase;
}}

/* ════════════════════════════════════════════════════════
   COURSES
   ════════════════════════════════════════════════════════ */
.courses-grid {{ display: flex; flex-direction: column; gap: 24px; }}
.course-featured {{
    background: {BG_CARD}; border: 1px solid {BORDER_BLUE};
    border-radius: 20px; padding: 48px;
    display: grid; grid-template-columns: 1fr 1fr; gap: 48px;
    align-items: center;
    box-shadow: inset 0 0 40px rgba(0,71,255,0.05);
    position: relative; overflow: hidden;
}}
.course-featured::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,100,255,0.6), transparent);
}}
.short-row {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
.course-card {{ padding: 36px; }}
.course-icon {{
    width: 52px; height: 52px; border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px; margin-bottom: 20px;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,71,255,0.20);
}}
.course-tag {{
    font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 0.1em; text-transform: uppercase;
    color: {BLUE_B} !important;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,71,255,0.20);
    border-radius: 100px; padding: 4px 12px;
    display: inline-block; margin-bottom: 14px;
}}
.course-title {{
    font-size: 22px; font-weight: 800; letter-spacing: -0.04em;
    margin-bottom: 12px; color: {WHITE} !important;
}}
.course-desc {{
    font-size: 14px; color: {W50} !important;
    line-height: 1.65; margin-bottom: 20px;
}}
.course-list {{ list-style: none; display: flex; flex-direction: column; gap: 9px; }}
.course-list li {{
    display: flex; align-items: center; gap: 10px;
    font-size: 13px; color: {W80} !important; font-weight: 500;
}}
.course-list li::before {{
    content: ''; width: 5px; height: 5px;
    border-radius: 50%; background: {BLUE_B}; flex-shrink: 0;
}}

/* Skills bars */
.skills-viz {{ display: flex; flex-direction: column; gap: 12px; }}
.bar-row    {{ display: flex; align-items: center; gap: 12px; }}
.bar-lbl    {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {W50} !important; width: 80px; flex-shrink: 0; }}
.bar-track  {{ flex: 1; height: 5px; background: rgba(255,255,255,0.06); border-radius: 3px; overflow: hidden; }}
.bar-fill   {{
    height: 100%; border-radius: 3px;
    background: linear-gradient(90deg, {BLUE}, {CYAN});
    animation: barGrow 1.8s 0.5s ease both;
}}
@keyframes barGrow {{ from {{ width: 0 !important; }} }}
.bar-pct    {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {BLUE_B} !important; width: 34px; text-align: right; }}
.format-box {{
    margin-top: 24px; padding: 20px;
    background: rgba(0,71,255,0.07); border: 1px solid rgba(0,71,255,0.16);
    border-radius: 14px;
}}
.format-lbl {{
    font-family: 'Space Mono', monospace; font-size: 10px;
    color: {BLUE_B} !important; letter-spacing: 0.1em;
    text-transform: uppercase; margin-bottom: 12px; display: block;
}}
.format-item {{
    display: flex; align-items: center; gap: 10px;
    font-size: 13px; color: {W80} !important; margin-bottom: 8px;
}}

/* ════════════════════════════════════════════════════════
   WORKSHOP SECTION CARD
   ════════════════════════════════════════════════════════ */
.workshop-card {{
    background: {BG_CARD}; border: 1px solid {BORDER_BLUE};
    border-radius: 24px; padding: 64px;
    display: grid; grid-template-columns: 1fr auto; gap: 64px;
    align-items: center; position: relative; overflow: hidden;
    box-shadow: inset 0 0 60px rgba(0,71,255,0.05);
}}
.workshop-card::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, {BLUE}, {CYAN}, transparent);
}}
.workshop-title {{
    font-size: clamp(28px, 3vw, 40px); font-weight: 800;
    letter-spacing: -0.05em; line-height: 1.1; margin-bottom: 14px;
    color: {WHITE} !important;
}}
.workshop-desc  {{ font-size: 15px; color: {W50} !important; line-height: 1.65; max-width: 460px; margin-bottom: 28px; }}
.workshop-meta  {{ display: flex; gap: 20px; flex-wrap: wrap; }}
.meta-item      {{ display: flex; align-items: center; gap: 8px; font-family: 'Space Mono', monospace; font-size: 12px; color: {W50} !important; }}
.live-dot       {{ width: 6px; height: 6px; border-radius: 50%; background: {GREEN}; box-shadow: 0 0 8px {GREEN}; animation: pulse 2s infinite; }}
.workshop-cta-wrap  {{ display: flex; flex-direction: column; align-items: center; gap: 14px; }}
.spots-txt      {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {W50} !important; letter-spacing: 0.06em; text-align: center; }}

/* ════════════════════════════════════════════════════════
   ENROLL
   ════════════════════════════════════════════════════════ */
.enroll-grid  {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start; }}
.enroll-h2    {{ font-size: clamp(32px, 4vw, 48px); font-weight: 800; letter-spacing: -0.05em; line-height: 1.1; margin-bottom: 16px; color: {WHITE} !important; }}
.enroll-p     {{ font-size: 15px; color: {W50} !important; line-height: 1.65; margin-bottom: 32px; }}
.steps        {{ list-style: none; display: flex; flex-direction: column; gap: 20px; }}
.step         {{ display: flex; align-items: flex-start; gap: 14px; }}
.step-num     {{
    width: 30px; height: 30px; border-radius: 50%;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,71,255,0.24);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: {BLUE_B} !important; flex-shrink: 0;
}}
.step-text strong {{ display: block; font-size: 14px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 3px; color: {WHITE} !important; }}
.step-text span   {{ font-size: 13px; color: {W50} !important; }}
.enroll-card      {{ background: {BG_CARD}; border: 1px solid {BORDER}; border-radius: 24px; padding: 44px; }}
.enroll-card h3   {{ font-size: 22px; font-weight: 800; letter-spacing: -0.04em; margin-bottom: 6px; color: {WHITE} !important; }}
.enroll-card > p  {{ font-size: 13px; color: {W50} !important; margin-bottom: 28px; }}
.timing-note      {{ display: flex; align-items: center; gap: 8px; font-size: 12px; color: {W50} !important; margin-top: 16px; }}
.info-box         {{ margin-top: 24px; padding: 20px; background: rgba(0,71,255,0.06); border: 1px solid rgba(0,71,255,0.16); border-radius: 14px; }}
.info-box-lbl     {{ font-family: 'Space Mono', monospace; font-size: 10px; color: {BLUE_B} !important; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 12px; display: block; }}
.info-box-item    {{ display: flex; align-items: center; gap: 10px; font-size: 13px; color: {W80} !important; margin-bottom: 8px; }}

/* ════════════════════════════════════════════════════════
   WHY US
   ════════════════════════════════════════════════════════ */
.why-grid  {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }}
.why-card  {{ padding: 32px 28px; }}
.why-icon  {{ font-size: 30px; margin-bottom: 16px; }}
.why-title {{ font-size: 17px; font-weight: 700; letter-spacing: -0.03em; margin-bottom: 8px; color: {WHITE} !important; }}
.why-desc  {{ font-size: 13px; color: {W50} !important; line-height: 1.65; }}

/* ════════════════════════════════════════════════════════
   CONTACT
   ════════════════════════════════════════════════════════ */
.contact-card {{
    background: {BG_CARD}; border: 1px solid {BORDER};
    border-radius: 24px; padding: 48px 40px;
    text-align: center; position: relative; overflow: hidden;
}}
.contact-card::before {{
    content: ''; position: absolute;
    bottom: -200px; left: 50%; transform: translateX(-50%);
    width: 600px; height: 400px; border-radius: 50%;
    background: {BLUE}; filter: blur(120px); opacity: 0.06; pointer-events: none;
}}
.contact-h2  {{ font-size: clamp(32px, 4vw, 52px); font-weight: 800; letter-spacing: -0.055em; line-height: 1.1; margin-bottom: 18px; color: {WHITE} !important; }}
.contact-sub {{ font-size: 16px; color: {W50} !important; max-width: 460px; margin: 0 auto 36px; line-height: 1.65; }}
.contact-btns {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }}

/* ════════════════════════════════════════════════════════
   FOOTER
   ════════════════════════════════════════════════════════ */
.tne-footer {{
    position: relative; z-index: 1;
    border-top: 1px solid {BORDER};
    padding: 24px 60px;
    display: flex; align-items: center;
    justify-content: space-between; flex-wrap: wrap; gap: 12px;
}}
.footer-logo  {{ font-size: 14px; font-weight: 800; letter-spacing: -0.03em; color: {W50} !important; }}
.footer-copy  {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {W20} !important; }}
.footer-links {{ display: flex; gap: 20px; }}
.footer-links a {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {W50} !important; text-decoration: none; letter-spacing: 0.03em; transition: color 0.2s; }}
.footer-links a:hover {{ color: {WHITE} !important; }}


/* ════════════════════════════════════════════════════════
   MENTORS
   ════════════════════════════════════════════════════════ */
.mentors-grid {{
    display: flex; gap: 32px; justify-content: center; flex-wrap: wrap;
}}
.mentor-card {{
    background: #0f0f1e; border: 1px solid rgba(255,255,255,0.10);
    border-radius: 20px; padding: 36px 32px;
    display: flex; flex-direction: column; align-items: center;
    gap: 20px; width: 220px; text-align: center;
    transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
}}
.mentor-card:hover {{
    border-color: rgba(0,100,255,0.35); transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 0 30px rgba(0,71,255,0.05);
}}
.mentor-img-wrap {{
    width: 120px; height: 120px; border-radius: 50%;
    overflow: hidden; border: 2px solid rgba(0,100,255,0.35); flex-shrink: 0;
}}
.mentor-img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; }}
.mentor-img-empty {{
    background: #181830; display: flex;
    align-items: center; justify-content: center; border-style: dashed;
}}
.mentor-question {{
    font-size: 40px; font-weight: 800;
    color: rgba(255,255,255,0.22); font-family: 'Space Mono', monospace; line-height: 1;
}}
.mentor-info {{ display: flex; flex-direction: column; align-items: center; gap: 6px; }}
.mentor-name {{ font-size: 16px; font-weight: 700; letter-spacing: -0.03em; color: #ffffff !important; }}
.mentor-role {{ font-size: 12px; color: rgba(255,255,255,0.60) !important; font-family: 'Space Mono', monospace; letter-spacing: 0.02em; }}
.mentor-linkedin {{
    display: inline-flex; align-items: center; gap: 6px; margin-top: 8px;
    padding: 7px 16px; background: rgba(0,71,255,0.12);
    border: 1px solid rgba(0,71,255,0.25); border-radius: 100px;
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: #4f9eff !important; text-decoration: none;
    transition: background 0.2s, border-color 0.2s;
}}
.mentor-linkedin:hover {{ background: rgba(0,71,255,0.22); border-color: #4f9eff; }}
.mentor-linkedin-ghost {{
    color: rgba(255,255,255,0.60) !important; background: rgba(255,255,255,0.04); border-color: rgba(255,255,255,0.10);
}}
.mentor-linkedin-ghost:hover {{
    color: #ffffff !important; background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.22);
}}

.hero-batch-note {{
    display: inline-flex; align-items: center; gap: 6px;
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: rgba(255,255,255,0.50); letter-spacing: 0.06em;
    margin-top: -20px; margin-bottom: 36px;
    animation: fadeUp 0.8s 0.15s ease both;
}}
.hero-link {{
    color: #00d4ff; text-decoration: none;
    border-bottom: 1px solid rgba(0,212,255,0.3);
    transition: color 0.2s, border-color 0.2s;
}}
.hero-link:hover {{ color: #ffffff; border-color: #ffffff; }}

/* ════════════════════════════════════════════════════════
   RESPONSIVE
   ════════════════════════════════════════════════════════ */
@media (max-width: 900px) {{
    nav.tne-nav       {{ padding: 14px 20px; top: 44px; }}
    .tne-page         {{ padding-top: 110px; }}
    .sec-inner        {{ padding: 64px 20px; }}
    .stats-wrap       {{ padding: 40px 20px; }}
    .stats-row        {{ grid-template-columns: 1fr; }}
    .stat-item        {{ border-right: none; border-bottom: 1px solid {BORDER}; }}
    .stat-item:last-child {{ border-bottom: none; }}
    .course-featured  {{ grid-template-columns: 1fr; gap: 32px; padding: 32px; }}
    .short-row        {{ grid-template-columns: 1fr; }}
    .workshop-card    {{ grid-template-columns: 1fr; gap: 32px; padding: 32px; }}
    .enroll-grid      {{ grid-template-columns: 1fr; }}
    .why-grid         {{ grid-template-columns: 1fr; }}
    .contact-card     {{ padding: 48px 24px; }}
    .tne-footer       {{ padding: 28px 20px; flex-direction: column; text-align: center; }}
    .footer-links     {{ justify-content: center; }}
    .ws-banner        {{ padding: 8px 16px; gap: 10px; }}
    .ws-banner-text   {{ font-size: 12px; text-align: center; }}
}}

/* ════════════════════════════════════════════════════════
   REGISTRATION MODAL
   ════════════════════════════════════════════════════════ */
.reg-modal {{
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(8,8,16,0.92); backdrop-filter: blur(8px);
    align-items: center; justify-content: center; padding: 20px;
}}
.reg-card {{
    background: #0f0f1e; border: 1px solid {BORDER_BLUE};
    border-radius: 24px; padding: 48px 40px; width: 100%; max-width: 440px;
    position: relative; box-shadow: 0 0 80px rgba(0,71,255,0.15);
}}
.reg-card::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, {BLUE}, {CYAN}, transparent);
}}
.reg-close {{
    position: absolute; top: 16px; right: 20px;
    background: none; border: none; cursor: pointer;
    font-size: 24px; color: {W50}; line-height: 1; transition: color 0.2s;
}}
.reg-close:hover {{ color: {WHITE}; }}
.reg-title {{ font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: {WHITE} !important; margin-bottom: 6px; }}
.reg-sub   {{ font-size: 13px; color: {W50} !important; margin-bottom: 28px; line-height: 1.55; }}
.reg-label {{
    display: block; font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 0.10em; text-transform: uppercase;
    color: {BLUE_B} !important; margin-bottom: 8px;
}}
.reg-input {{
    width: 100%; padding: 13px 16px;
    background: rgba(255,255,255,0.04); border: 1px solid {BORDER};
    border-radius: 12px; font-family: 'Manrope', sans-serif;
    font-size: 14px; color: {WHITE} !important; outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    margin-bottom: 20px; box-sizing: border-box;
}}
.reg-input::placeholder {{ color: {W20}; }}
.reg-input option {{
    background: #1a1a2e; color: {WHITE};
}}
.reg-input option:disabled {{ color: rgba(255,255,255,0.35); }}
.reg-input:focus {{
    border-color: {BORDER_BLUE}; box-shadow: 0 0 0 3px rgba(0,71,255,0.12);
}}
.reg-submit {{
    width: 100%; padding: 15px; background: {BLUE}; color: {WHITE} !important;
    border: none; border-radius: 100px; font-family: 'Manrope', sans-serif;
    font-size: 15px; font-weight: 700; letter-spacing: -0.02em;
    cursor: pointer; transition: background 0.2s, box-shadow 0.2s;
}}
.reg-submit:hover:not(:disabled) {{ background: {BLUE_B}; box-shadow: 0 0 40px {BLUE_GLOW}; }}
.reg-submit:disabled {{ opacity: 0.6; cursor: not-allowed; }}
.reg-note {{ text-align: center; font-size: 11px; color: {W20} !important; margin-top: 16px; font-family: 'Space Mono', monospace; }}
</style>

<!-- ══ Stars ═══════════════════════════════════════════ -->
{STARS_HTML}

<!-- ══ Atmospheric glow ════════════════════════════════ -->
<div class="atmos"></div>


<!-- ══════════════════════════════════════════════════════
     WORKSHOP ANNOUNCEMENT BANNER
     ══════════════════════════════════════════════════════ -->
<div class="ws-banner">
  <span class="ws-banner-pulse"></span>
  <span class="ws-banner-text">
    🗓&nbsp; <strong>Workshop — ₹100:</strong>&nbsp;
    <span class="ws-date">Saturday, 18 April 2026 · 10:30 AM</span>
    &nbsp;—&nbsp; Intro to Data Analytics (Live Online)
  </span>
  <span class="ws-banner-sep">·</span>
  <button onclick="openRegModal()" class="ws-banner-btn" style="border:none;cursor:pointer;">
    Register — ₹100 →
  </button>
</div>

<!-- ══ Header ════════════════════════════════════════════ -->
<header class="tne-header">
  <a href="#hero" class="tne-brand">
    <div class="tne-brand-icon">TNE</div>
    <div class="tne-brand-name">The Next <span>Engineer</span></div>
  </a>
</header>

<div class="tne-page">

<!-- ══════════════════════════════════════════════════════
     HERO
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="hero">
  <a href="#hero" class="hero-logo">
    <div class="hero-logo-icon">TNE</div>
    <div class="hero-logo-text">The Next <span>Engineer</span></div>
  </a>

  <div class="hero-badge">
    <span class="hero-badge-dot"></span>
    Now Enrolling · 1st Cohort starting 4th May 2026
  </div>
  <div class="hero-batch-note">
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="5" width="10" height="7" rx="1.5"/><path d="M3.5 5V3.5a2.5 2.5 0 015 0V5"/></svg>
    Online Only · Tue &amp; Thu 7–9 PM · Sat 10 AM–6 PM · 8 Weeks · 20 seats
  </div>
  <h1 class="hero-h1" style="white-space:nowrap;">
    Learn. Implement. Grow 📈
  </h1>
  <p class="hero-sub">
    I'm a passionate trainer with international experience in Data Analytics &amp; Data Engineering —
    working in France, Sweden and India with multinationals like
    <a href="https://nova.space/" target="_blank" rel="noopener" class="hero-link">Nova.space</a>,
    <a href="https://www.ironhack.com/us" target="_blank" rel="noopener" class="hero-link">Ironhack</a>,
    <a href="https://nodcoding.com/" target="_blank" rel="noopener" class="hero-link">NodCoding</a>,
    <a href="https://guardanthealth.com/" target="_blank" rel="noopener" class="hero-link">Guardant Health</a>
    and Cognizant.
  </p>
  <div class="hero-ctas">
    <button onclick="openEnrollModal()" class="btn-p" style="border:none;cursor:pointer;">
      Enroll Now
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </div>

  <!-- Course highlight chips -->
  <div class="hero-courses reveal" style="margin-top:12px;">
    <div class="hero-course-label">What we teach</div>
    <div class="hero-course-chips">
      <div class="course-chip chip-flagship">
        <span>📊</span>
        <span>Data Analytics Bootcamp</span>
        <span class="chip-tag">Flagship</span>
      </div>
      <div class="course-chip"><span>🐍</span><span>Python</span></div>
      <div class="course-chip"><span>🗄️</span><span>SQL</span></div>
      <div class="course-chip"><span>📈</span><span>Data Visualization</span></div>
      <div class="course-chip"><span>🤖</span><span>Machine Learning Algorithms</span></div>
      <div class="course-chip"><span>🎯</span><span>Recommendation Engines</span></div>
    </div>
  </div>

  <div class="hero-orbit"><div class="orbit-dot"></div></div>
  <div class="scroll-hint">
    <span>Scroll</span>
    <div class="scroll-arrow"></div>
  </div>
</section>

<hr class="glow-divider"/>

<!-- ══════════════════════════════════════════════════════
     MENTORS
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="mentors">
  <div class="sec-inner">
    <div class="reveal" style="margin-bottom:56px;">
      <span class="sec-label">// know your mentors</span>
      <h2 class="sec-title" style="white-space:nowrap;">The people who'll guide your journey</h2>
      <p class="sec-sub" style="white-space:nowrap;">Not just a teacher — an industry practitioner who works with data every day.</p>
    </div>
    <div class="mentors-grid">

      <!-- Sandeep -->
      <div class="mentor-card reveal">
        <div class="mentor-img-wrap">
          <img src="{SANDEEP_SRC}" alt="Sandeep Singh" class="mentor-img" />
        </div>
        <div class="mentor-info">
          <h4 class="mentor-name">Sandeep Singh</h4>
          <p class="mentor-role">Founder &amp; Lead Instructor</p>
          <a href="https://www.linkedin.com/in/sandeepsingh1910/" target="_blank" rel="noopener" class="mentor-linkedin">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
            LinkedIn
          </a>
        </div>
      </div>

      <!-- Placeholder -->
      <div class="mentor-card mentor-placeholder reveal">
        <div class="mentor-img-wrap mentor-img-empty">
          <span class="mentor-question">?</span>
        </div>
        <div class="mentor-info">
          <h4 class="mentor-name" style="color:rgba(255,255,255,0.5)!important;">You?</h4>
          <p class="mentor-role">You could be the next mentor</p>
          <a href="https://wa.me/918019101592?text=Hi%2C%20I%27d%20like%20to%20be%20a%20mentor%20at%20The%20Next%20Engineer!" target="_blank" rel="noopener" class="mentor-linkedin mentor-linkedin-ghost">
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
              <path d="M8 1v14M1 8h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
            </svg>
            Get in touch
          </a>
        </div>
      </div>

    </div>
  </div>
</section>


<!-- ══════════════════════════════════════════════════════
     ENROLL
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="enroll">
  <div class="sec-inner">
    <div class="enroll-grid reveal">
      <div>
        <span class="sec-label">// join the bootcamp</span>
        <h2 class="enroll-h2">Ready to become<br>a data analyst?</h2>
        <p class="enroll-p">Spots are limited each cohort. Apply now to secure your seat and take the first step toward your new career in data.</p>
        <ol class="steps">
          <li class="step"><div class="step-num">01</div><div class="step-text"><strong>Fill out the form</strong><span>Takes 3 minutes. Tell us about your goals.</span></div></li>
          <li class="step"><div class="step-num">02</div><div class="step-text"><strong>We review &amp; interview call</strong><span>Our team will review your application and schedule a quick call.</span></div></li>
          <li class="step"><div class="step-num">03</div><div class="step-text"><strong>Confirm your seat</strong><span>Secure your spot and receive onboarding details.</span></div></li>
          <li class="step"><div class="step-num">04</div><div class="step-text"><strong>Prework before bootcamp</strong><span>Complete the pre-reading materials to hit the ground running.</span></div></li>
          <li class="step"><div class="step-num">05</div><div class="step-text"><strong>Join the bootcamp</strong><span>Day one begins your transformation — live, online, together.</span></div></li>
        </ol>
      </div>
      <div class="enroll-card">
        <h3>Apply Now</h3>
        <p>Fill in our short form — we'll get back to you within 24 hours.</p>
        <button onclick="openEnrollModal()"
           class="btn-p" style="width:100%;justify-content:center;font-size:16px;padding:16px 0;border:none;cursor:pointer;">
          Open Application Form →
        </button>
        <div class="timing-note">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="7" cy="7" r="6"/><path d="M7 4v3l2 2"/>
          </svg>
          Response within 24 hours guaranteed
        </div>
        <div class="info-box">
          <span class="info-box-lbl">Program Format</span>
          <div class="info-box-item"><span>🎥</span> 100% Live Online Classes</div>
          <div class="info-box-item"><span>📹</span> Recordings provided after every session</div>
          <div class="info-box-item"><span>📅</span> Tue &amp; Thu: 7 PM – 9 PM</div>
          <div class="info-box-item"><span>📅</span> Saturday: 10 AM – 6 PM</div>
          <div class="info-box-item"><span>⏱️</span> 8 Weeks · 20 seats per cohort</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════════════════
     CONTACT
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="contact">
  <div class="sec-inner">
    <div class="contact-card reveal">
      <span class="sec-label">// let's talk</span>
      <h2 class="contact-h2">Have questions?</h2>
      <p class="contact-sub">Text your teacher directly on LinkedIn and ask for a call.</p>
      <div class="contact-btns">
        <a href="https://www.linkedin.com/in/sandeepsingh1910/" target="_blank" rel="noopener" class="btn-p">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
          </svg>
          Text your teacher on LinkedIn
        </a>
      </div>
    </div>
  </div>
</section>

<!-- ══ Footer ════════════════════════════════════════════ -->
<footer class="tne-footer">
  <div class="footer-logo">The Next Engineer</div>
  <div class="footer-copy">© 2025 The Next Engineer · All rights reserved.</div>
  <div class="footer-links">
    <a href="{WA_URL}" target="_blank" rel="noopener">WhatsApp</a>
    <a href="#enroll">Enroll</a>
    <a href="#mentors">Mentors</a>
    <a href="{FORM_URL}" target="_blank" rel="noopener">Apply Now</a>
  </div>
</footer>

</div><!-- /tne-page -->

<!-- ══ Enroll Modal ══════════════════════════════════════ -->
<div id="enroll-modal" class="reg-modal">
  <div class="reg-card" style="max-width:500px;">
    <button class="reg-close" onclick="closeEnrollModal()" aria-label="Close">&times;</button>
    <p class="reg-title">Apply for the Bootcamp</p>
    <p class="reg-sub">Data Analytics Bootcamp · 1st Cohort starting 4th May 2026<br>We'll review your application and reach out within 24 hours.</p>

    <div id="enroll-success" style="display:none;text-align:center;padding:24px 0;">
      <div style="font-size:48px;margin-bottom:16px;">🎉</div>
      <p style="font-size:17px;font-weight:700;color:#fff;margin-bottom:8px;">Application received!</p>
      <p style="font-size:13px;color:rgba(255,255,255,0.55);line-height:1.6;">We'll review your details and get back to you within 24 hours.<br>Check your inbox for a confirmation email.</p>
    </div>

    <form id="enroll-form">
      <label class="reg-label" for="enroll-name">Full Name</label>
      <input class="reg-input" type="text" id="enroll-name" placeholder="Your name" required />

      <label class="reg-label" for="enroll-email">Email Address</label>
      <input class="reg-input" type="email" id="enroll-email" placeholder="you@email.com" required />

      <label class="reg-label" for="enroll-phone">Phone Number</label>
      <input class="reg-input" type="tel" id="enroll-phone" placeholder="+91 98765 43210" required />

      <label class="reg-label" for="enroll-status">Current Status</label>
      <select class="reg-input" id="enroll-status" required style="cursor:pointer;">
        <option value="" disabled selected>Select your status…</option>
        <option value="Working Professional">Working Professional</option>
        <option value="Looking for a Job">Looking for a Job</option>
      </select>

      <label class="reg-label" for="enroll-edu">Highest Education</label>
      <select class="reg-input" id="enroll-edu" required style="cursor:pointer;">
        <option value="" disabled selected>Select your qualification…</option>
        <option value="High School">High School / 12th</option>
        <option value="Diploma">Diploma</option>
        <option value="Bachelor's Degree">Bachelor's Degree</option>
        <option value="Master's Degree">Master's Degree</option>
        <option value="PhD">PhD</option>
        <option value="Other">Other</option>
      </select>

      <label class="reg-label" for="enroll-city">City</label>
      <input class="reg-input" type="text" id="enroll-city" placeholder="Your city" required />

      <button type="submit" class="reg-submit" id="enroll-submit">Submit Application →</button>
    </form>
    <p class="reg-note">Your info is only used to process your application.</p>
  </div>
</div>

<!-- ══ Registration Modal ════════════════════════════════ -->
<div id="reg-modal" class="reg-modal">
  <div class="reg-card">
    <button class="reg-close" onclick="closeRegModal()" aria-label="Close">&times;</button>
    <p class="reg-title">Register for the Workshop</p>
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
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  /* Inside components.html, 100vh = iframe height (8500px). Override hero to prevent 8500px blank section. */
  #hero { min-height: 720px !important; }
</style>
</head>
<body style="margin:0;padding:0;">
"""

HTML_FOOT = """
<div id="rzp-success" style="display:none;position:fixed;inset:0;background:rgba(8,8,16,0.96);z-index:9999;flex-direction:column;align-items:center;justify-content:center;gap:16px;text-align:center;padding:24px;">
  <div style="font-size:56px">&#x2705;</div>
  <h2 style="font-family:'Manrope',sans-serif;font-size:24px;font-weight:800;letter-spacing:-0.04em;color:#fff;margin:0;">Payment Successful!</h2>
  <p style="font-family:'Manrope',sans-serif;font-size:15px;color:rgba(255,255,255,0.55);max-width:380px;line-height:1.6;margin:0;">Redirecting you to WhatsApp to confirm your workshop spot...</p>
</div>
<script>
var APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyIahJO9hJNTd4Z08Xi7S2RtkOTZUgCxQ0xaELMFrK68lpxcdsFrEkBV-w2SXX6e-5T/exec";
var PAYMENT_LINK    = "https://rzp.io/rzp/XTP0oz9";

function openRegModal() {
  document.getElementById('reg-modal').style.display = 'flex';
}
function closeRegModal() {
  document.getElementById('reg-modal').style.display = 'none';
  var f = document.getElementById('reg-form');
  if (f) f.reset();
  var b = document.getElementById('reg-submit');
  if (b) { b.textContent = 'Proceed to Payment \u2192'; b.disabled = false; }
}

document.addEventListener('DOMContentLoaded', function() {
  // Close modal on backdrop click
  document.getElementById('reg-modal').addEventListener('click', function(e) {
    if (e.target === this) closeRegModal();
  });

  document.getElementById('reg-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var name   = document.getElementById('reg-name').value.trim();
    var email  = document.getElementById('reg-email').value.trim();
    var phone  = document.getElementById('reg-phone').value.trim();
    var status = document.getElementById('reg-status').value;

    var btn = document.getElementById('reg-submit');
    btn.textContent = 'Saving…';
    btn.disabled = true;

    var body = 'name='   + encodeURIComponent(name)
             + '&email=' + encodeURIComponent(email)
             + '&phone=' + encodeURIComponent(phone)
             + '&status='+ encodeURIComponent(status);

    // no-cors: response is opaque but data reaches Apps Script
    fetch(APPS_SCRIPT_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body
    }).finally(function() {
      closeRegModal();
      window.open(PAYMENT_LINK, '_blank');
    });
  });
});

// ── Enroll modal ──────────────────────────────────────────
function openEnrollModal() {
  document.getElementById('enroll-modal').style.display = 'flex';
}
function closeEnrollModal() {
  document.getElementById('enroll-modal').style.display = 'none';
  document.getElementById('enroll-form').style.display = 'block';
  document.getElementById('enroll-success').style.display = 'none';
  document.getElementById('enroll-form').reset();
  var b = document.getElementById('enroll-submit');
  if (b) { b.textContent = 'Submit Application \u2192'; b.disabled = false; }
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('enroll-modal').addEventListener('click', function(e) {
    if (e.target === this) closeEnrollModal();
  });

  document.getElementById('enroll-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var btn = document.getElementById('enroll-submit');
    btn.textContent = 'Submitting…';
    btn.disabled = true;

    var body = 'formType=enroll'
             + '&name='    + encodeURIComponent(document.getElementById('enroll-name').value.trim())
             + '&email='   + encodeURIComponent(document.getElementById('enroll-email').value.trim())
             + '&phone='   + encodeURIComponent(document.getElementById('enroll-phone').value.trim())
             + '&status='  + encodeURIComponent(document.getElementById('enroll-status').value)
             + '&education='+ encodeURIComponent(document.getElementById('enroll-edu').value)
             + '&city='    + encodeURIComponent(document.getElementById('enroll-city').value.trim());

    fetch(APPS_SCRIPT_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: body
    }).finally(function() {
      document.getElementById('enroll-form').style.display = 'none';
      document.getElementById('enroll-success').style.display = 'block';
      setTimeout(closeEnrollModal, 4000);
    });
  });
});

// Make iframe fill the full parent viewport
function resizeIframe() {
  if (window.frameElement) {
    window.frameElement.style.height = window.parent.innerHeight + 'px';
    window.frameElement.style.width  = '100%';
    window.frameElement.style.display = 'block';
    window.frameElement.style.border  = 'none';
    window.frameElement.style.position = 'fixed';
    window.frameElement.style.top  = '0';
    window.frameElement.style.left = '0';
    window.frameElement.style.zIndex = '9999';
  }
}
window.addEventListener("load",   resizeIframe);
window.addEventListener("resize", resizeIframe);
</script>
</body>
</html>"""

components.html(HTML_HEAD + page + HTML_FOOT, height=900, scrolling=True)
