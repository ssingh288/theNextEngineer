import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(
    page_title="The Next Engineer — Online Coding Bootcamp",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome and padding from the outer wrapper page
st.markdown("""
<style>
#MainMenu, footer, header                    { visibility: hidden !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"]               { display: none !important; }
.main .block-container                       { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stMain"]                { padding: 0 !important; }
.stApp                                       { background: #080810 !important; }
.element-container, .stMarkdown              { padding: 0 !important; margin: 0 !important; }
iframe                                       { display: block; border: none; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# Remove Streamlit chrome and padding from the outer wrapper page
st.markdown("""
<style>
#MainMenu, footer, header                              { visibility: hidden !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"]                         { display: none !important; }
.main .block-container                                 { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stMain"]                          { padding: 0 !important; }
.stApp                                                 { background: #080810 !important; }
.element-container, .stMarkdown                        { padding: 0 !important; margin: 0 !important; }
iframe                                                 { display: block; border: none; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

FORM_URL  = "https://docs.google.com/forms/d/e/1FAIpQLSclF7YODQUuzhHzsudwYSHinMRQswR2y9aSHh9SHaRfwnIH-g/viewform?usp=sharing&ouid=109749639989339515327"
WA_NUMBER = "918019101592"
WA_MSG    = "Hello%2C%20I%27m%20interested%20in%20The%20Next%20Engineer%20bootcamp!"
WA_URL    = f"https://wa.me/{WA_NUMBER}?text={WA_MSG}"

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
    border-radius: 24px; padding: 80px;
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
    padding: 36px 60px;
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
</style>

<!-- ══ Stars ═══════════════════════════════════════════ -->
{STARS_HTML}

<!-- ══ Atmospheric glow ════════════════════════════════ -->
<div class="atmos"></div>

<!-- ══ WhatsApp Float ══════════════════════════════════ -->
<a href="{WA_URL}" class="wa-float" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 2C8.268 2 2 8.268 2 16c0 2.42.638 4.688 1.75 6.655L2 30l7.59-1.722A13.94 13.94 0 0016 30c7.732 0 14-6.268 14-14S23.732 2 16 2zm0 25.5a11.45 11.45 0 01-5.85-1.605l-.42-.252-4.507 1.022 1.06-4.37-.276-.45A11.47 11.47 0 014.5 16C4.5 9.649 9.649 4.5 16 4.5S27.5 9.649 27.5 16 22.351 27.5 16 27.5zm6.267-8.574c-.34-.17-2.015-1-2.328-1.11-.315-.113-.543-.17-.773.17-.228.34-.886 1.11-1.087 1.34-.2.227-.4.254-.74.085-.34-.17-1.432-.527-2.726-1.684-1.007-.9-1.687-2.01-1.884-2.35-.198-.34-.02-.524.148-.693.153-.152.34-.396.51-.594.17-.197.226-.34.34-.566.112-.228.056-.427-.028-.597-.085-.17-.773-1.862-1.06-2.55-.28-.668-.564-.578-.774-.588l-.66-.011a1.27 1.27 0 00-.917.43c-.316.34-1.2 1.172-1.2 2.857s1.228 3.314 1.4 3.543c.17.228 2.417 3.692 5.86 5.18.82.354 1.46.565 1.958.723.823.261 1.572.224 2.163.136.66-.099 2.015-.823 2.3-1.618.283-.797.283-1.48.2-1.62-.084-.14-.313-.227-.654-.397z"/>
  </svg>
</a>

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
  <button onclick="openWorkshopPayment()" class="ws-banner-btn" style="border:none;cursor:pointer;">
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
    Only 20 seats per batch
  </div>
  <h1 class="hero-h1">
    <span class="grad-text">Learn. Implement. Grow 📈</span>
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
    <a href="{FORM_URL}" target="_blank" rel="noopener" class="btn-p">
      Enroll Now
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </a>
    <a href="#courses" class="btn-o">Explore Courses</a>
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
      <div class="course-chip"><span>📈</span><span>Tableau</span></div>
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
     STATS
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="stats">
  <div class="stats-wrap reveal">
    <div class="stats-row">
      <div class="stat-item">
        <div class="stat-num">100%</div>
        <div class="stat-lbl">Online &amp; Flexible</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">4</div>
        <div class="stat-lbl">Programs Available</div>
      </div>
      <div class="stat-item">
        <div class="stat-num">∞</div>
        <div class="stat-lbl">Career Possibilities</div>
      </div>
    </div>
  </div>
</section>

<hr class="glow-divider"/>

<!-- ══════════════════════════════════════════════════════
     COURSES
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="courses">
  <div class="sec-inner">
    <div class="reveal" style="margin-bottom:56px;">
      <span class="sec-label">// what we teach</span>
      <h2 class="sec-title">Programs built for<br>real-world impact</h2>
      <p class="sec-sub">Industry-aligned curriculum designed to take you from zero to job-ready in data analytics.</p>
    </div>

    <div class="courses-grid">
      <!-- Featured: Data Analytics Bootcamp -->
      <div class="course-featured reveal">
        <div>
          <div class="course-icon">📊</div>
          <span class="course-tag">Flagship Program</span>
          <h3 class="course-title">Data Analytics Bootcamp</h3>
          <p class="course-desc">Our comprehensive bootcamp takes you from data beginner to analytics professional. Covering the full data stack — collection, querying, analysis and visualisation — with real projects and mentorship throughout.</p>
          <ul class="course-list">
            <li>Foundations of Data Analytics &amp; Statistical Thinking</li>
            <li>Python for Data Analysis — Pandas &amp; NumPy</li>
            <li>SQL &amp; Database Querying</li>
            <li>Data Visualisation with Tableau</li>
            <li>Capstone Project with Real Dataset</li>
            <li>Career Coaching &amp; Portfolio Review</li>
          </ul>
          <br>
          <a href="{FORM_URL}" target="_blank" rel="noopener" class="btn-p" style="margin-top:8px;">
            Enroll in Bootcamp
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
              <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </div>
        <div class="skills-viz">
          <span style="font-family:'Space Mono',monospace;font-size:11px;color:{W50};letter-spacing:0.08em;text-transform:uppercase;margin-bottom:8px;display:block;">Skills You'll Gain</span>
          <div class="bar-row"><span class="bar-lbl">Python</span><div class="bar-track"><div class="bar-fill" style="width:90%"></div></div><span class="bar-pct">90%</span></div>
          <div class="bar-row"><span class="bar-lbl">SQL</span><div class="bar-track"><div class="bar-fill" style="width:85%"></div></div><span class="bar-pct">85%</span></div>
          <div class="bar-row"><span class="bar-lbl">Tableau</span><div class="bar-track"><div class="bar-fill" style="width:80%"></div></div><span class="bar-pct">80%</span></div>
          <div class="bar-row"><span class="bar-lbl">Analytics</span><div class="bar-track"><div class="bar-fill" style="width:95%"></div></div><span class="bar-pct">95%</span></div>
          <div class="bar-row"><span class="bar-lbl">Excel</span><div class="bar-track"><div class="bar-fill" style="width:72%"></div></div><span class="bar-pct">72%</span></div>
          <div class="format-box">
            <span class="format-lbl">Program Format</span>
            <div class="format-item"><span>🌐</span> 100% Online &amp; Self-paced</div>
            <div class="format-item"><span>👨‍🏫</span> Live Mentorship Sessions</div>
            <div class="format-item"><span>🏆</span> Certificate of Completion</div>
          </div>
        </div>
      </div>

      <!-- Short Courses -->
      <div class="short-row">
        <div class="card course-card reveal">
          <div class="course-icon">🐍</div>
          <span class="course-tag">Short Course</span>
          <h3 class="course-title">Python Essentials</h3>
          <p class="course-desc">Master Python fundamentals and data libraries used in every analytics role.</p>
          <ul class="course-list">
            <li>Python syntax &amp; fundamentals</li>
            <li>Data structures &amp; control flow</li>
            <li>Pandas &amp; NumPy for data</li>
            <li>Hands-on mini projects</li>
          </ul>
        </div>
        <div class="card course-card reveal">
          <div class="course-icon">🗄️</div>
          <span class="course-tag">Short Course</span>
          <h3 class="course-title">SQL Mastery</h3>
          <p class="course-desc">Query databases like a pro and extract insights from real-world datasets.</p>
          <ul class="course-list">
            <li>SELECT, JOINs &amp; aggregations</li>
            <li>Subqueries &amp; CTEs</li>
            <li>Window functions</li>
            <li>Real database practice</li>
          </ul>
        </div>
        <div class="card course-card reveal">
          <div class="course-icon">📈</div>
          <span class="course-tag">Short Course</span>
          <h3 class="course-title">Tableau for Analysts</h3>
          <p class="course-desc">Turn raw data into compelling dashboards that drive business decisions.</p>
          <ul class="course-list">
            <li>Tableau Desktop basics</li>
            <li>Charts, maps &amp; filters</li>
            <li>Dashboard design principles</li>
            <li>Publishing &amp; sharing</li>
          </ul>
        </div>
      </div>
    </div>
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
      <h2 class="sec-title">The people who'll<br>guide your journey</h2>
      <p class="sec-sub">Industry practitioners who work with data every day — not just teachers.</p>
    </div>
    <div class="mentors-grid">

      <!-- Sandeep -->
      <div class="mentor-card reveal">
        <div class="mentor-img-wrap">
          <img src="Sandeep.PNG" alt="Sandeep Singh" class="mentor-img" />
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
     WORKSHOP
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="workshop">
  <div class="sec-inner">
    <div class="workshop-card reveal">
      <div>
        <span class="sec-label">// upcoming event</span>
        <h2 class="workshop-title">
          Data Analytics<br>
          <span class="grad-text">Workshop</span>
        </h2>
        <p class="workshop-desc">Join our free hands-on workshop and get a real taste of the data analyst's world. We'll walk through a live dataset, build a Tableau dashboard, and answer every question you have.</p>
        <div class="workshop-meta">
          <div class="meta-item"><span class="live-dot"></span> Saturday, 18 April 2026</div>
          <div class="meta-item"><span class="live-dot"></span> 10:30 AM (Online)</div>
          <div class="meta-item"><span class="live-dot"></span> ₹100 · Beginner Friendly</div>
        </div>
      </div>
      <div class="workshop-cta-wrap">
        <button onclick="openWorkshopPayment()" class="btn-p" style="font-size:16px;padding:16px 36px;white-space:nowrap;border:none;cursor:pointer;">
          Register — ₹100 →
        </button>
        <span class="spots-txt">Limited spots available</span>
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
          <li class="step"><div class="step-num">01</div><div class="step-text"><strong>Fill out the application</strong><span>Takes 3 minutes. Tell us about your goals.</span></div></li>
          <li class="step"><div class="step-num">02</div><div class="step-text"><strong>We review &amp; reach out</strong><span>Our team will contact you within 24 hours.</span></div></li>
          <li class="step"><div class="step-num">03</div><div class="step-text"><strong>Confirm your seat</strong><span>Secure your spot and receive onboarding details.</span></div></li>
          <li class="step"><div class="step-num">04</div><div class="step-text"><strong>Start learning</strong><span>Day one begins your transformation.</span></div></li>
        </ol>
      </div>
      <div class="enroll-card">
        <h3>Apply Now</h3>
        <p>Fill in our short Google Form — we'll get back to you within 24 hours.</p>
        <a href="{FORM_URL}" target="_blank" rel="noopener"
           class="btn-p" style="width:100%;justify-content:center;font-size:16px;padding:16px 0;">
          Open Application Form →
        </a>
        <div class="timing-note">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="7" cy="7" r="6"/><path d="M7 4v3l2 2"/>
          </svg>
          Response within 24 hours guaranteed
        </div>
        <div class="info-box">
          <span class="info-box-lbl">Courses Offered</span>
          <div class="info-box-item"><span>📊</span> Data Analytics Bootcamp (Full Program)</div>
          <div class="info-box-item"><span>🐍</span> Python Essentials</div>
          <div class="info-box-item"><span>🗄️</span> SQL Mastery</div>
          <div class="info-box-item"><span>📈</span> Tableau for Analysts</div>
        </div>
      </div>
    </div>
  </div>
</section>

<hr class="glow-divider"/>

<!-- ══════════════════════════════════════════════════════
     WHY US
     ══════════════════════════════════════════════════════ -->
<section class="sec" id="why">
  <div class="sec-inner">
    <div class="reveal" style="margin-bottom:56px;">
      <span class="sec-label">// why choose us</span>
      <h2 class="sec-title">Built for results,<br>not just certificates</h2>
      <p class="sec-sub">Everything about The Next Engineer is designed to get you hired.</p>
    </div>
    <div class="why-grid">
      <div class="card why-card reveal"><div class="why-icon">🎯</div><h4 class="why-title">Outcome-Focused</h4><p class="why-desc">Curriculum built backwards from what employers actually hire for — not just theory.</p></div>
      <div class="card why-card reveal"><div class="why-icon">🌐</div><h4 class="why-title">100% Online</h4><p class="why-desc">Learn at your own pace from anywhere. Flexible enough to fit around your life.</p></div>
      <div class="card why-card reveal"><div class="why-icon">🤝</div><h4 class="why-title">Real Mentorship</h4><p class="why-desc">Live sessions with instructors who work in data every single day.</p></div>
      <div class="card why-card reveal"><div class="why-icon">🏗️</div><h4 class="why-title">Project-Based</h4><p class="why-desc">Build a portfolio of real projects to show employers — not just quizzes.</p></div>
      <div class="card why-card reveal"><div class="why-icon">⚡</div><h4 class="why-title">Fast-Track Learning</h4><p class="why-desc">Get job-ready as fast as possible without cutting corners on depth.</p></div>
      <div class="card why-card reveal"><div class="why-icon">🏆</div><h4 class="why-title">Recognised Certificate</h4><p class="why-desc">A certificate that adds real credibility to your CV and LinkedIn profile.</p></div>
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
      <h2 class="contact-h2">Have questions?<br>We're here for you.</h2>
      <p class="contact-sub">Not sure which program is right for you? Reach out on WhatsApp and our team will help you find the best path.</p>
      <div class="contact-btns">
        <a href="{WA_URL}" target="_blank" rel="noopener" class="btn-wa">
          <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
            <path d="M16 2C8.268 2 2 8.268 2 16c0 2.42.638 4.688 1.75 6.655L2 30l7.59-1.722A13.94 13.94 0 0016 30c7.732 0 14-6.268 14-14S23.732 2 16 2zm0 25.5a11.45 11.45 0 01-5.85-1.605l-.42-.252-4.507 1.022 1.06-4.37-.276-.45A11.47 11.47 0 014.5 16C4.5 9.649 9.649 4.5 16 4.5S27.5 9.649 27.5 16 22.351 27.5 16 27.5zm6.267-8.574c-.34-.17-2.015-1-2.328-1.11-.315-.113-.543-.17-.773.17-.228.34-.886 1.11-1.087 1.34-.2.227-.4.254-.74.085-.34-.17-1.432-.527-2.726-1.684-1.007-.9-1.687-2.01-1.884-2.35-.198-.34-.02-.524.148-.693.153-.152.34-.396.51-.594.17-.197.226-.34.34-.566.112-.228.056-.427-.028-.597-.085-.17-.773-1.862-1.06-2.55-.28-.668-.564-.578-.774-.588l-.66-.011a1.27 1.27 0 00-.917.43c-.316.34-1.2 1.172-1.2 2.857s1.228 3.314 1.4 3.543c.17.228 2.417 3.692 5.86 5.18.82.354 1.46.565 1.958.723.823.261 1.572.224 2.163.136.66-.099 2.015-.823 2.3-1.618.283-.797.283-1.48.2-1.62-.084-.14-.313-.227-.654-.397z"/>
          </svg>
          Chat on WhatsApp
        </a>
        <a href="{FORM_URL}" target="_blank" rel="noopener" class="btn-o">Apply Now</a>
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
    <a href="#courses">Courses</a>
    <a href="#workshop">Workshop</a>
    <a href="{FORM_URL}" target="_blank" rel="noopener">Enroll</a>
  </div>
</footer>

</div><!-- /tne-page -->
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
function openWorkshopPayment() {
  var rzp = new Razorpay({
    key: "rzp_live_SahJJtEgrCiJOp",
    amount: 10000,
    currency: "INR",
    name: "The Next Engineer",
    description: "Data Analytics Workshop — 18 Apr 2026",
    handler: function(response) {
      var msg = encodeURIComponent(
        "Hi! I just registered for the Data Analytics Workshop. My Razorpay Payment ID: "
        + response.razorpay_payment_id
      );
      var overlay = document.getElementById("rzp-success");
      overlay.style.display = "flex";
      setTimeout(function() {
        window.open("https://wa.me/918019101592?text=" + msg, "_blank");
        overlay.style.display = "none";
      }, 2000);
    },
    theme: { color: "#0047ff" },
    modal: { backdropclose: false }
  });
  rzp.open();
}
window.addEventListener("load", function() {
  if (window.frameElement) {
    window.frameElement.style.height = (document.documentElement.scrollHeight + 20) + "px";
  }
});
</script>
</body>
</html>"""

components.html(HTML_HEAD + page + HTML_FOOT, height=8500, scrolling=False)
