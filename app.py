import streamlit as st
import streamlit.components.v1 as components
import random
import base64
import os

st.set_page_config(
    page_title="The Next Engineer — Data Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header                    { visibility: hidden !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stAppViewBlockContainer"],
.stDeployButton,
#stDecoration                                { display: none !important; }
[class*="viewerBadge"],
[class*="managedBy"],
[class*="toolbarActions"]                    { display: none !important; }
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

FORM_URL  = "https://docs.google.com/forms/d/e/1FAIpQLSclF7YODQUuzhHzsudwYSHinMRQswR2y9aSHh9SHaRfwnIH-g/viewform"
WA_NUMBER = "918019101592"
WA_MSG    = "Hello%2C%20I%27m%20interested%20in%20The%20Next%20Engineer%20bootcamp!"
WA_URL    = f"https://wa.me/{WA_NUMBER}?text={WA_MSG}"
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyIahJO9hJNTd4Z08Xi7S2RtkOTZUgCxQ0xaELMFrK68lpxcdsFrEkBV-w2SXX6e-5T/exec"
PAYMENT_LINK    = "https://rzp.io/rzp/XTP0oz9"

_img_path = os.path.join(os.path.dirname(__file__), "Sandeep.PNG")
with open(_img_path, "rb") as _f:
    SANDEEP_SRC = "data:image/png;base64," + base64.b64encode(_f.read()).decode()

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

WHITE       = "#ffffff"
W80         = "rgba(255,255,255,0.85)"
W50         = "rgba(255,255,255,0.60)"
W20         = "rgba(255,255,255,0.22)"
BLUE        = "#0047ff"
BLUE_B      = "#4f9eff"
CYAN        = "#00d4ff"
GREEN       = "#00db57"
BG          = "#080810"
BG_CARD     = "#0f0f1e"
BORDER      = "rgba(255,255,255,0.10)"
BORDER_BLUE = "rgba(0,100,255,0.35)"
BLUE_GLOW   = "rgba(0,71,255,0.40)"

page = f"""
<style>
/* ── BASE ── */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html  {{ scroll-behavior: smooth; }}
body  {{
    font-family: 'Manrope', sans-serif;
    background: {BG};
    color: {WHITE};
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
}}
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');
::-webkit-scrollbar {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {BLUE}; border-radius: 2px; }}

/* ── STARS / ATMOS ── */
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
    position: fixed; top: -350px; left: 50%; transform: translateX(-50%);
    width: 900px; height: 900px; border-radius: 50%;
    background: conic-gradient(from 0deg at 50% 50%, #0047ff 46deg, #06003a 226deg);
    filter: blur(140px); opacity: 0.16;
    z-index: 0; pointer-events: none;
}}

/* ════════════════════════════════════════════════════════
   TOP NAV  (brand left · tab buttons right)
   ════════════════════════════════════════════════════════ */
.tne-nav {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 300;
    height: 64px;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px;
    background: rgba(8,8,16,0.92);
    backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid {BORDER};
}}
.tne-brand {{
    display: flex; align-items: center; gap: 10px; text-decoration: none; cursor: pointer;
}}
.tne-brand-icon {{
    width: 34px; height: 34px;
    background: linear-gradient(135deg, {BLUE}, {CYAN});
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Mono', monospace; font-size: 12px; font-weight: 700;
    color: {WHITE}; flex-shrink: 0;
}}
.tne-brand-name {{
    font-size: 16px; font-weight: 800; letter-spacing: -0.03em; color: {WHITE};
}}
.tne-brand-name span {{ color: {BLUE_B}; }}
.tab-btns {{ display: flex; gap: 8px; }}
.tab-btn {{
    padding: 9px 20px; border-radius: 100px;
    border: 1px solid rgba(255,255,255,0.15);
    background: transparent; color: rgba(255,255,255,0.55);
    font-family: 'Manrope', sans-serif; font-size: 13px; font-weight: 700;
    cursor: pointer; transition: all 0.2s; letter-spacing: -0.01em;
    white-space: nowrap;
}}
.tab-btn.active {{ background: {BLUE}; border-color: {BLUE}; color: {WHITE}; }}
.tab-btn:hover:not(.active) {{ border-color: {BORDER_BLUE}; color: {WHITE}; }}

/* ════════════════════════════════════════════════════════
   WORKSHOP BANNER  (course tab only, fixed below nav)
   ════════════════════════════════════════════════════════ */
.ws-banner {{
    position: fixed; top: 64px; left: 0; right: 0; z-index: 200;
    background: linear-gradient(90deg, #0a0a20, #0d1640, #0a0a20);
    border-bottom: 1px solid {BORDER_BLUE};
    padding: 14px 32px;
    display: none; align-items: center; justify-content: center;
    gap: 20px; flex-wrap: wrap;
    box-shadow: 0 2px 48px rgba(0,71,255,0.28);
}}
.ws-banner-pulse {{
    width: 10px; height: 10px; border-radius: 50%;
    background: {GREEN}; box-shadow: 0 0 12px {GREEN};
    animation: pulse 2s infinite; flex-shrink: 0;
}}
@keyframes pulse {{
    0%,100% {{ opacity:1; transform:scale(1); }}
    50%     {{ opacity:0.4; transform:scale(1.5); }}
}}
.ws-banner-text {{
    font-family: 'Manrope', sans-serif;
    font-size: 15px; font-weight: 600; color: {WHITE};
}}
.ws-banner-text .ws-date {{ color: {CYAN}; font-weight: 800; }}
.ws-banner-btn {{
    display: inline-flex; align-items: center; gap: 8px;
    background: {BLUE}; color: {WHITE};
    padding: 10px 22px; border-radius: 100px;
    font-family: 'Manrope', sans-serif;
    font-size: 14px; font-weight: 700;
    border: none; white-space: nowrap; cursor: pointer;
    transition: background 0.2s, box-shadow 0.2s;
}}
.ws-banner-btn:hover {{ background: {BLUE_B}; box-shadow: 0 0 24px {BLUE_GLOW}; }}
.ws-banner-sep {{ color: {W20}; font-size: 18px; }}

/* ════════════════════════════════════════════════════════
   TAB CONTENT WRAPPERS
   ════════════════════════════════════════════════════════ */
.tab-content {{ display: none; }}
.tab-content.active {{ display: block; }}

/* ════════════════════════════════════════════════════════
   ██  WORKSHOP TAB
   ════════════════════════════════════════════════════════ */
.ws-wrap {{
    position: relative; z-index: 1;
    max-width: 720px; margin: 0 auto;
    padding: 80px 24px 120px;
}}
.ws-hero {{ text-align: center; padding-bottom: 24px; }}
.ws-badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,100,255,0.30);
    border-radius: 100px; padding: 8px 20px;
    font-family: 'Space Mono', monospace; font-size: 12px;
    color: {BLUE_B}; margin-bottom: 28px;
    animation: fadeUp 0.7s ease both;
}}
.ws-badge-dot {{
    width: 8px; height: 8px; border-radius: 50%;
    background: {GREEN}; box-shadow: 0 0 8px {GREEN};
    animation: pulse 2s infinite;
}}
.ws-h1 {{
    font-size: clamp(30px, 6vw, 56px); font-weight: 800;
    letter-spacing: -0.055em; line-height: 1.05;
    margin-bottom: 20px; color: {WHITE};
    animation: fadeUp 0.7s 0.1s ease both;
}}
.ws-h1 .cyan {{ color: {CYAN}; }}
.ws-sub {{
    font-size: 17px; color: {W50};
    line-height: 1.65; max-width: 560px;
    margin: 0 auto 32px;
    animation: fadeUp 0.7s 0.2s ease both;
}}
.ws-price-row {{
    display: flex; align-items: center; justify-content: center;
    gap: 12px; margin-bottom: 24px;
    animation: fadeUp 0.7s 0.25s ease both;
}}
.ws-price {{ font-size: 44px; font-weight: 800; letter-spacing: -0.05em; color: {WHITE}; }}
.ws-price-note {{
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: {W50}; line-height: 1.5; text-align: left;
}}
.ws-cta-btn {{
    display: inline-flex; align-items: center; gap: 10px;
    background: {BLUE}; color: {WHITE};
    padding: 18px 44px; border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 18px; font-weight: 800;
    letter-spacing: -0.02em; cursor: pointer;
    transition: background 0.2s, box-shadow 0.2s, transform 0.15s;
    box-shadow: 0 0 40px rgba(0,71,255,0.40);
    animation: fadeUp 0.7s 0.3s ease both;
}}
.ws-cta-btn:hover {{ background: {BLUE_B}; box-shadow: 0 0 60px rgba(0,71,255,0.55); transform: translateY(-2px); }}
.ws-seats-note {{
    margin-top: 12px;
    font-family: 'Space Mono', monospace; font-size: 12px;
    color: {W50};
    animation: fadeUp 0.7s 0.35s ease both;
}}
.ws-seats-note span {{ color: {GREEN}; }}

/* Countdown */
.ws-countdown {{
    display: flex; justify-content: center; gap: 16px;
    margin: 36px 0 0;
    animation: fadeUp 0.7s 0.4s ease both;
}}
.cd-block {{
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px; padding: 16px 20px; min-width: 72px; text-align: center;
}}
.cd-num {{
    font-size: 32px; font-weight: 800; letter-spacing: -0.05em;
    color: {WHITE}; line-height: 1; font-family: 'Space Mono', monospace;
}}
.cd-lbl {{
    font-family: 'Space Mono', monospace; font-size: 10px;
    color: {W50}; letter-spacing: 0.08em;
    text-transform: uppercase; margin-top: 6px;
}}

/* Glow divider */
hr.ws-glow {{
    border: none; height: 1px;
    background: {BLUE};
    box-shadow: 0 0 60px 6px {BLUE}, 0 0 160px 12px rgba(0,71,255,0.3);
    margin: 56px 0;
}}

/* Section label */
.ws-sec-label {{
    font-family: 'Space Mono', monospace; font-size: 11px;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: {BLUE_B}; margin-bottom: 14px; display: block;
}}
.ws-sec-title {{
    font-size: clamp(22px, 4vw, 34px); font-weight: 800;
    letter-spacing: -0.05em; line-height: 1.1; margin-bottom: 28px;
    color: {WHITE};
}}

/* Learn list */
.ws-learn-list {{ list-style: none; display: flex; flex-direction: column; gap: 14px; }}
.ws-learn-item {{
    display: flex; align-items: flex-start; gap: 14px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px; padding: 18px 20px;
}}
.ws-learn-icon {{ font-size: 22px; flex-shrink: 0; margin-top: 2px; }}
.ws-learn-text strong {{ display: block; font-size: 15px; font-weight: 700; margin-bottom: 3px; color: {WHITE}; }}
.ws-learn-text span   {{ font-size: 13px; color: {W50}; line-height: 1.5; }}

/* Instructor */
.ws-instructor {{
    display: flex; align-items: center; gap: 28px;
    background: {BG_CARD}; border: 1px solid {BORDER_BLUE};
    border-radius: 20px; padding: 28px 32px;
    position: relative; overflow: hidden;
}}
.ws-instructor::before {{
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, {BLUE}, {CYAN}, transparent);
}}
.ws-instructor-img {{
    width: 90px; height: 90px; border-radius: 50%;
    object-fit: cover; object-position: top;
    border: 2px solid {BORDER_BLUE}; flex-shrink: 0;
}}
.ws-instructor-name {{ font-size: 18px; font-weight: 800; letter-spacing: -0.03em; margin-bottom: 4px; color: {WHITE}; }}
.ws-instructor-role {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {BLUE_B}; margin-bottom: 10px; }}
.ws-instructor-bio  {{ font-size: 13px; color: {W50}; line-height: 1.6; }}

/* Details grid */
.ws-details-grid {{
    display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
}}
.ws-detail-item {{
    display: flex; align-items: center; gap: 12px;
    background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 16px 18px;
}}
.ws-detail-icon {{ font-size: 20px; flex-shrink: 0; }}
.ws-detail-text strong {{ display: block; font-size: 13px; font-weight: 700; color: {WHITE}; }}
.ws-detail-text span   {{ font-size: 12px; color: {W50}; font-family: 'Space Mono', monospace; }}

/* Sticky bottom CTA */
.ws-sticky {{
    position: fixed; bottom: 0; left: 0; right: 0; z-index: 200;
    background: rgba(8,8,16,0.96); backdrop-filter: blur(16px);
    border-top: 1px solid {BORDER_BLUE};
    padding: 14px 32px;
    display: flex; align-items: center; justify-content: space-between; gap: 16px;
}}
.ws-sticky-info strong {{ display: block; font-size: 15px; font-weight: 800; color: {WHITE}; }}
.ws-sticky-info span   {{ font-size: 12px; color: {W50}; font-family: 'Space Mono', monospace; }}
.ws-sticky-btn {{
    display: inline-flex; align-items: center; gap: 8px;
    background: {BLUE}; color: {WHITE};
    padding: 13px 28px; border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 800;
    cursor: pointer; white-space: nowrap;
    transition: background 0.2s, box-shadow 0.2s;
    box-shadow: 0 0 30px rgba(0,71,255,0.40);
}}
.ws-sticky-btn:hover {{ background: {BLUE_B}; box-shadow: 0 0 50px rgba(0,71,255,0.55); }}

/* ════════════════════════════════════════════════════════
   ██  COURSE TAB
   ════════════════════════════════════════════════════════ */
.tne-page {{ position: relative; z-index: 1; padding-top: 130px; }}

.sec {{ position: relative; z-index: 1; }}
.sec-inner {{ max-width: 1180px; margin: 0 auto; padding: 96px 60px; }}
.sec-label {{
    font-family: 'Space Mono', monospace; font-size: 11px;
    letter-spacing: 0.12em; text-transform: uppercase;
    color: {BLUE_B}; margin-bottom: 16px; display: block;
}}
.sec-title {{
    font-size: clamp(32px, 4vw, 52px); font-weight: 800;
    letter-spacing: -0.05em; line-height: 1.1; color: {WHITE};
}}
.sec-sub {{
    font-size: 17px; color: {W50}; max-width: 520px;
    line-height: 1.65; letter-spacing: -0.02em; margin-top: 14px;
}}
.glow-divider {{
    width: 100%; height: 1px; border: none; background: {BLUE};
    box-shadow: 0 0 80px 8px {BLUE}, 0 0 200px 16px rgba(0,71,255,0.4);
}}

/* Buttons */
.btn-p {{
    display: inline-flex; align-items: center; gap: 8px;
    padding: 13px 28px; background: {BLUE}; color: {WHITE};
    border-radius: 100px; border: none;
    font-family: 'Manrope', sans-serif; font-size: 15px; font-weight: 700;
    letter-spacing: -0.02em; cursor: pointer; text-decoration: none;
    transition: background 0.2s, box-shadow 0.2s, transform 0.2s;
}}
.btn-p:hover {{ background: {BLUE_B}; box-shadow: 0 0 40px {BLUE_GLOW}; transform: translateY(-2px); color: {WHITE}; }}

/* Hero (course tab) */
#hero {{
    min-height: 100vh; display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    text-align: center; padding: 100px 24px 80px; position: relative;
}}
.hero-badge {{
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,100,255,0.30);
    border-radius: 100px; padding: 8px 18px;
    font-family: 'Space Mono', monospace; font-size: 15px;
    color: {BLUE_B}; margin-bottom: 36px; animation: fadeUp 0.8s ease both;
}}
.hero-badge-dot {{
    width: 6px; height: 6px; border-radius: 50%;
    background: {GREEN}; box-shadow: 0 0 8px {GREEN}; animation: pulse 2s infinite;
}}
.hero-h1 {{
    font-size: clamp(44px, 7vw, 88px); font-weight: 800;
    letter-spacing: -0.055em; line-height: 1.0;
    max-width: 880px; margin-bottom: 24px; color: {WHITE};
    animation: fadeUp 0.8s 0.1s ease both;
}}
.hero-ctas {{
    display: flex; gap: 14px; flex-wrap: wrap; justify-content: center;
    animation: fadeUp 0.8s 0.3s ease both;
}}
.hero-orbit {{
    position: absolute; bottom: -40px; left: 50%; transform: translateX(-50%);
    width: 360px; height: 360px; border-radius: 50%;
    border: 1px solid rgba(0,71,255,0.14); pointer-events: none;
}}
.hero-orbit::before {{
    content: ''; position: absolute; inset: 24px;
    border-radius: 50%; border: 1px solid rgba(0,71,255,0.07);
}}
.orbit-dot {{
    position: absolute; width: 8px; height: 8px;
    border-radius: 50%; background: {BLUE_B}; box-shadow: 0 0 14px {BLUE};
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
    letter-spacing: 0.1em; text-transform: uppercase; color: {W50};
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
    font-family: 'Space Mono', monospace; font-size: 13px;
    letter-spacing: 0.10em; text-transform: uppercase; color: rgba(255,255,255,0.50);
}}
.hero-course-chips {{ display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }}
.course-chip {{
    display: inline-flex; align-items: center; gap: 7px;
    padding: 9px 16px; background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 100px; font-size: 13px; font-weight: 600;
    color: rgba(255,255,255,0.85); letter-spacing: -0.01em;
    transition: border-color 0.2s, background 0.2s;
}}
.course-chip:hover {{ border-color: rgba(0,100,255,0.35); background: rgba(0,71,255,0.08); }}
.chip-flagship {{ border-color: rgba(0,100,255,0.35); background: rgba(0,71,255,0.10); color: #ffffff; }}
.chip-tag {{
    font-family: 'Space Mono', monospace; font-size: 9px;
    letter-spacing: 0.08em; text-transform: uppercase;
    color: #4f9eff; background: rgba(0,71,255,0.15);
    border: 1px solid rgba(0,71,255,0.25); border-radius: 100px; padding: 2px 8px;
}}
.hero-batch-note {{
    display: inline-flex; align-items: center; gap: 6px;
    font-family: 'Space Mono', monospace; font-size: 14px;
    color: rgba(255,255,255,0.60); letter-spacing: 0.04em;
    margin-top: -20px; margin-bottom: 36px; animation: fadeUp 0.8s 0.15s ease both;
}}
.hero-link {{
    color: {CYAN}; text-decoration: none; border-bottom: 1px solid rgba(0,212,255,0.3);
    transition: color 0.2s, border-color 0.2s;
}}
.hero-link:hover {{ color: {WHITE}; border-color: {WHITE}; }}
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

/* Mentors */
.mentors-grid {{ display: flex; gap: 32px; justify-content: center; flex-wrap: wrap; }}
.mentor-card {{
    background: {BG_CARD}; border: 1px solid {BORDER};
    border-radius: 20px; padding: 36px 32px;
    display: flex; flex-direction: column; align-items: center;
    gap: 20px; width: 220px; text-align: center;
    transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
}}
.mentor-card:hover {{ border-color: {BORDER_BLUE}; transform: translateY(-4px); box-shadow: 0 20px 60px rgba(0,0,0,0.4); }}
.mentor-img-wrap {{ width: 120px; height: 120px; border-radius: 50%; overflow: hidden; border: 2px solid {BORDER_BLUE}; flex-shrink: 0; }}
.mentor-img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; }}
.mentor-img-empty {{ background: #181830; display: flex; align-items: center; justify-content: center; border-style: dashed; }}
.mentor-question {{ font-size: 40px; font-weight: 800; color: rgba(255,255,255,0.22); font-family: 'Space Mono', monospace; line-height: 1; }}
.mentor-info {{ display: flex; flex-direction: column; align-items: center; gap: 6px; }}
.mentor-name {{ font-size: 16px; font-weight: 700; letter-spacing: -0.03em; color: {WHITE}; }}
.mentor-role {{ font-size: 12px; color: {W50}; font-family: 'Space Mono', monospace; letter-spacing: 0.02em; }}
.mentor-linkedin {{
    display: inline-flex; align-items: center; gap: 6px; margin-top: 8px;
    padding: 7px 16px; background: rgba(0,71,255,0.12);
    border: 1px solid rgba(0,71,255,0.25); border-radius: 100px;
    font-family: 'Space Mono', monospace; font-size: 11px;
    color: {BLUE_B}; text-decoration: none; transition: background 0.2s, border-color 0.2s;
}}
.mentor-linkedin:hover {{ background: rgba(0,71,255,0.22); border-color: {BLUE_B}; }}
.mentor-linkedin-ghost {{ color: {W50}; background: rgba(255,255,255,0.04); border-color: rgba(255,255,255,0.10); }}
.mentor-linkedin-ghost:hover {{ color: {WHITE}; background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.22); }}

/* Enroll */
.enroll-grid  {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: start; }}
.enroll-h2    {{ font-size: clamp(32px, 4vw, 48px); font-weight: 800; letter-spacing: -0.05em; line-height: 1.1; margin-bottom: 16px; color: {WHITE}; }}
.enroll-p     {{ font-size: 15px; color: {W50}; line-height: 1.65; margin-bottom: 32px; }}
.steps        {{ list-style: none; display: flex; flex-direction: column; gap: 20px; }}
.step         {{ display: flex; align-items: flex-start; gap: 14px; }}
.step-num     {{
    width: 30px; height: 30px; border-radius: 50%;
    background: rgba(0,71,255,0.12); border: 1px solid rgba(0,71,255,0.24);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Mono', monospace; font-size: 11px; color: {BLUE_B}; flex-shrink: 0;
}}
.step-text strong {{ display: block; font-size: 14px; font-weight: 700; letter-spacing: -0.02em; margin-bottom: 3px; color: {WHITE}; }}
.step-text span   {{ font-size: 13px; color: {W50}; }}
.enroll-card      {{ background: {BG_CARD}; border: 1px solid {BORDER}; border-radius: 24px; padding: 44px; }}
.enroll-card h3   {{ font-size: 22px; font-weight: 800; letter-spacing: -0.04em; margin-bottom: 6px; color: {WHITE}; }}
.enroll-card > p  {{ font-size: 13px; color: {W50}; margin-bottom: 28px; }}
.timing-note      {{ display: flex; align-items: center; gap: 8px; font-size: 12px; color: {W50}; margin-top: 16px; }}
.info-box         {{ margin-top: 24px; padding: 20px; background: rgba(0,71,255,0.06); border: 1px solid rgba(0,71,255,0.16); border-radius: 14px; }}
.info-box-lbl     {{ font-family: 'Space Mono', monospace; font-size: 10px; color: {BLUE_B}; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 12px; display: block; }}
.info-box-item    {{ display: flex; align-items: center; gap: 10px; font-size: 13px; color: {W80}; margin-bottom: 8px; }}

/* Contact */
.contact-card {{
    background: {BG_CARD}; border: 1px solid {BORDER};
    border-radius: 24px; padding: 48px 40px;
    text-align: center; position: relative; overflow: hidden;
}}
.contact-card::before {{
    content: ''; position: absolute; bottom: -200px; left: 50%; transform: translateX(-50%);
    width: 600px; height: 400px; border-radius: 50%;
    background: {BLUE}; filter: blur(120px); opacity: 0.06; pointer-events: none;
}}
.contact-h2  {{ font-size: clamp(32px, 4vw, 52px); font-weight: 800; letter-spacing: -0.055em; line-height: 1.1; margin-bottom: 18px; color: {WHITE}; }}
.contact-sub {{ font-size: 16px; color: {W50}; max-width: 460px; margin: 0 auto 36px; line-height: 1.65; }}
.contact-btns {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap; }}

/* Footer */
.tne-footer {{
    position: relative; z-index: 1; border-top: 1px solid {BORDER};
    padding: 24px 60px; display: flex; align-items: center;
    justify-content: space-between; flex-wrap: wrap; gap: 12px;
}}
.footer-logo  {{ font-size: 14px; font-weight: 800; letter-spacing: -0.03em; color: {W50}; }}
.footer-copy  {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {W20}; }}
.footer-links {{ display: flex; gap: 20px; }}
.footer-links a {{ font-family: 'Space Mono', monospace; font-size: 11px; color: {W50}; text-decoration: none; letter-spacing: 0.03em; transition: color 0.2s; }}
.footer-links a:hover {{ color: {WHITE}; }}

/* ════════════════════════════════════════════════════════
   MODALS
   ════════════════════════════════════════════════════════ */
.reg-modal {{
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(8,8,16,0.92); backdrop-filter: blur(8px);
    align-items: center; justify-content: center; padding: 20px;
}}
.reg-card {{
    background: {BG_CARD}; border: 1px solid {BORDER_BLUE};
    border-radius: 24px; padding: 48px 40px; width: 100%; max-width: 440px;
    position: relative; box-shadow: 0 0 80px rgba(0,71,255,0.15);
    max-height: 90vh; overflow-y: auto;
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
.reg-title {{ font-size: 22px; font-weight: 800; letter-spacing: -0.04em; color: {WHITE}; margin-bottom: 6px; }}
.reg-sub   {{ font-size: 13px; color: {W50}; margin-bottom: 28px; line-height: 1.55; }}
.reg-label {{
    display: block; font-family: 'Space Mono', monospace; font-size: 10px;
    letter-spacing: 0.10em; text-transform: uppercase; color: {BLUE_B}; margin-bottom: 8px;
}}
.reg-input {{
    width: 100%; padding: 13px 16px;
    background: rgba(255,255,255,0.04); border: 1px solid {BORDER};
    border-radius: 12px; font-family: 'Manrope', sans-serif;
    font-size: 14px; color: {WHITE}; outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    margin-bottom: 20px; box-sizing: border-box;
}}
.reg-input::placeholder {{ color: {W20}; }}
.reg-input:focus {{ border-color: {BORDER_BLUE}; box-shadow: 0 0 0 3px rgba(0,71,255,0.12); }}
.reg-input option {{ background: #1a1a2e; color: {WHITE}; }}
.reg-input option:disabled {{ color: rgba(255,255,255,0.35); }}
.reg-submit {{
    width: 100%; padding: 15px; background: {BLUE}; color: {WHITE};
    border: none; border-radius: 100px; font-family: 'Manrope', sans-serif;
    font-size: 15px; font-weight: 700; letter-spacing: -0.02em;
    cursor: pointer; transition: background 0.2s, box-shadow 0.2s;
}}
.reg-submit:hover:not(:disabled) {{ background: {BLUE_B}; box-shadow: 0 0 40px {BLUE_GLOW}; }}
.reg-submit:disabled {{ opacity: 0.6; cursor: not-allowed; }}
.reg-note {{ text-align: center; font-size: 11px; color: {W20}; margin-top: 16px; font-family: 'Space Mono', monospace; }}

/* Responsive */
@media (max-width: 900px) {{
    .tne-nav      {{ padding: 0 20px; }}
    .tne-page     {{ padding-top: 130px; }}
    .sec-inner    {{ padding: 64px 20px; }}
    .enroll-grid  {{ grid-template-columns: 1fr; }}
    .contact-card {{ padding: 48px 24px; }}
    .tne-footer   {{ padding: 28px 20px; flex-direction: column; text-align: center; }}
    .footer-links {{ justify-content: center; }}
    .ws-banner    {{ padding: 10px 16px; gap: 10px; }}
    .ws-banner-text {{ font-size: 13px; text-align: center; }}
    .ws-details-grid {{ grid-template-columns: 1fr; }}
    .ws-instructor {{ flex-direction: column; text-align: center; }}
    .ws-sticky {{ flex-direction: column; text-align: center; gap: 10px; }}
    .ws-sticky-btn {{ width: 100%; justify-content: center; }}
    .ws-countdown {{ gap: 10px; }}
    .cd-block {{ min-width: 60px; padding: 12px 14px; }}
    .cd-num {{ font-size: 26px; }}
    .tab-btn {{ font-size: 12px; padding: 7px 14px; }}
}}
</style>

{STARS_HTML}
<div class="atmos"></div>

<!-- ══════════════════════════════════════════════════════
     TOP NAV
     ══════════════════════════════════════════════════════ -->
<nav class="tne-nav">
  <div class="tne-brand" onclick="showTab('workshop')">
    <div class="tne-brand-icon">TNE</div>
    <div class="tne-brand-name">The Next <span>Engineer</span></div>
  </div>
  <div class="tab-btns">
    <button class="tab-btn active" data-tab="workshop" onclick="showTab('workshop')">Workshop</button>
    <button class="tab-btn" data-tab="course" onclick="showTab('course')">Data Analytics Course</button>
  </div>
</nav>

<!-- ══════════════════════════════════════════════════════
     WORKSHOP BANNER  (shown only on course tab)
     ══════════════════════════════════════════════════════ -->
<div class="ws-banner" id="ws-banner">
  <span class="ws-banner-pulse"></span>
  <span class="ws-banner-text">
    🗓&nbsp; <strong>Workshop — ₹99:</strong>&nbsp;
    <span class="ws-date">Saturday, 18 April 2026 · 10:00 AM – 11:30 AM</span>
    &nbsp;—&nbsp; Your First Step towards the Data Team (Live Online)
  </span>
  <span class="ws-banner-sep">·</span>
  <button onclick="openRegModal()" class="ws-banner-btn">Register — ₹99 →</button>
</div>

<!-- ══════════════════════════════════════════════════════
     WORKSHOP TAB  (default)
     ══════════════════════════════════════════════════════ -->
<div id="tab-workshop" class="tab-content active">
  <div class="ws-wrap">

    <!-- Hero -->
    <div class="ws-hero">
      <div class="ws-badge">
        <span class="ws-badge-dot"></span>
        Live Online &nbsp;·&nbsp; Saturday, 18 April 2026 &nbsp;·&nbsp; 10:00 AM – 11:30 AM
      </div>
      <h1 class="ws-h1">
        Your First Step towards<br><span class="cyan">the Data Team</span>
      </h1>
      <p class="ws-sub">
        A 1.5-hour workshop where you'll see exactly how a Data Analyst, Data Engineer,
        Data Scientist and Business Analyst work — real tools, skills required,
        and honest time it takes to master each role.
      </p>
      <div class="ws-price-row">
        <div>
          <div style="font-size:13px;color:rgba(255,255,255,0.4);text-decoration:line-through;margin-bottom:2px;">₹299</div>
          <div class="ws-price">₹99</div>
        </div>
        <div class="ws-price-note">One-time entry fee<br>Seats fill fast</div>
      </div>
      <button onclick="openRegModal()" class="ws-cta-btn">Reserve My Seat →</button>
      <p class="ws-seats-note">⚡ Seats are limited — register early</p>
      <div class="ws-countdown">
        <div class="cd-block"><div class="cd-num" id="cd-days">--</div><div class="cd-lbl">Days</div></div>
        <div class="cd-block"><div class="cd-num" id="cd-hours">--</div><div class="cd-lbl">Hours</div></div>
        <div class="cd-block"><div class="cd-num" id="cd-mins">--</div><div class="cd-lbl">Mins</div></div>
        <div class="cd-block"><div class="cd-num" id="cd-secs">--</div><div class="cd-lbl">Secs</div></div>
      </div>
    </div>

    <hr class="ws-glow"/>

    <!-- What you'll learn -->
    <section>
      <span class="ws-sec-label">// what you'll walk away with</span>
      <h2 class="ws-sec-title">4 roles. 1.5 hours. Zero fluff.</h2>
      <ul class="ws-learn-list">
        <li class="ws-learn-item">
          <span class="ws-learn-icon">📊</span>
          <div class="ws-learn-text">
            <strong>Data Analyst</strong>
            <span>You become the person everyone turns to for answers. Your charts sit in boardroom presentations. Your findings help companies save money and make smarter decisions. Great starting point — achievable without a degree in 4–6 months.</span>
          </div>
        </li>
        <li class="ws-learn-item">
          <span class="ws-learn-icon">⚙️</span>
          <div class="ws-learn-text">
            <strong>Data Engineer</strong>
            <span>Less visible but one of the highest-paid roles in tech. You build the systems that power every other data role. If you enjoy building things and solving complex problems — this is your lane. 8–12 months to get job-ready.</span>
          </div>
        </li>
        <li class="ws-learn-item">
          <span class="ws-learn-icon">🤖</span>
          <div class="ws-learn-text">
            <strong>Data Scientist</strong>
            <span>The role that makes headlines. You predict outcomes, spot hidden patterns and build AI models. It's the most exciting — and the most challenging. Requires patience, but the career ceiling is sky-high. Plan for 10–14 months.</span>
          </div>
        </li>
        <li class="ws-learn-item">
          <span class="ws-learn-icon">💼</span>
          <div class="ws-learn-text">
            <strong>Business Analyst</strong>
            <span>The easiest door into the data world, especially if you already have work experience. You translate what the business needs into what the data team builds. High demand, good pay, and you don't need to code heavily. 3–5 months.</span>
          </div>
        </li>
      </ul>
    </section>

    <hr class="ws-glow"/>

    <!-- Instructor -->
    <section>
      <span class="ws-sec-label">// your instructor</span>
      <div class="ws-instructor">
        <img src="{SANDEEP_SRC}" alt="Sandeep Singh" class="ws-instructor-img"/>
        <div>
          <div class="ws-instructor-name">Sandeep Singh</div>
          <div class="ws-instructor-role">Founder · The Next Engineer</div>
          <div class="ws-instructor-role" style="color:rgba(255,255,255,0.55);font-size:12px;margin-top:2px;">Senior Data Engineer at Guardant Health</div>
          <p class="ws-instructor-bio">
            Trained 50+ students across France, Sweden &amp; India. Worked with
            Nova.space, Ironhack, Guardant Health and Cognizant.
            Everything I teach, I've done at work.
          </p>
          <a href="https://www.linkedin.com/in/sandeepsingh1910/" target="_blank" rel="noopener"
             style="display:inline-flex;align-items:center;gap:8px;margin-top:14px;
                    padding:8px 18px;background:rgba(0,71,255,0.12);border:1px solid rgba(0,100,255,0.30);
                    border-radius:100px;font-family:'Space Mono',monospace;font-size:11px;
                    color:#4f9eff;text-decoration:none;transition:background 0.2s,border-color 0.2s;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            linkedin.com/in/sandeepsingh1910
          </a>
        </div>
      </div>
    </section>

    <hr class="ws-glow"/>

    <!-- Details -->
    <section>
      <span class="ws-sec-label">// workshop details</span>
      <h2 class="ws-sec-title">Everything you need to know</h2>
      <div class="ws-details-grid">
        <div class="ws-detail-item">
          <span class="ws-detail-icon">📅</span>
          <div class="ws-detail-text"><strong>Saturday, 18 April 2026</strong><span>10:00 AM — 11:30 AM IST</span></div>
        </div>
        <div class="ws-detail-item">
          <span class="ws-detail-icon">💻</span>
          <div class="ws-detail-text"><strong>100% Online</strong><span>Google Meet · Link sent on email</span></div>
        </div>
        <div class="ws-detail-item">
          <span class="ws-detail-icon">🎟️</span>
          <div class="ws-detail-text"><strong>Only ₹99 entry</strong><span>Limited seats · Register early</span></div>
        </div>
        <div class="ws-detail-item">
          <span class="ws-detail-icon">❓</span>
          <div class="ws-detail-text"><strong>Live Q&amp;A included</strong><span>Ask anything — no question is silly</span></div>
        </div>
        <div class="ws-detail-item">
          <span class="ws-detail-icon">🚀</span>
          <div class="ws-detail-text"><strong>No prior experience needed</strong><span>Just bring curiosity &amp; a laptop</span></div>
        </div>
      </div>
    </section>

    <hr class="ws-glow"/>

    <!-- Final CTA -->
    <section style="text-align:center;padding:8px 0 40px;">
      <h2 style="font-size:clamp(24px,5vw,38px);font-weight:800;letter-spacing:-0.05em;margin-bottom:12px;color:#fff;">
        Don't think too long —<br>seats go fast.
      </h2>
      <p style="font-size:15px;color:rgba(255,255,255,0.50);margin-bottom:32px;line-height:1.6;">
        ₹99 is less than a coffee. 1.5 hours could change your career.
      </p>
      <button onclick="openRegModal()" class="ws-cta-btn">Reserve My Seat — ₹99 →</button>
    </section>

  </div><!-- /ws-wrap -->

  <!-- Sticky bottom bar (workshop tab only) -->
  <div class="ws-sticky" id="ws-sticky">
    <div class="ws-sticky-info">
      <strong>Data Analytics Workshop</strong>
      <span>18 Apr 2026 · 10:00 AM – 11:30 AM · ₹99</span>
    </div>
    <button onclick="openRegModal()" class="ws-sticky-btn">Reserve My Seat →</button>
  </div>
</div><!-- /tab-workshop -->

<!-- ══════════════════════════════════════════════════════
     COURSE TAB
     ══════════════════════════════════════════════════════ -->
<div id="tab-course" class="tab-content">
<div class="tne-page">

<section class="sec" id="hero">
  <div class="hero-badge">
    <span class="hero-badge-dot"></span>
    Now Enrolling · 1st Cohort starting 4th May 2026
  </div>
  <div class="hero-batch-note">
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="5" width="10" height="7" rx="1.5"/><path d="M3.5 5V3.5a2.5 2.5 0 015 0V5"/></svg>
    Online Only · Tue &amp; Thu 7–9 PM · Sat 10 AM–6 PM · 8 Weeks · 20 seats
  </div>
  <h1 class="hero-h1" style="white-space:nowrap;">Learn. Build. Grow 📈</h1>
  <div class="hero-ctas">
    <button onclick="openEnrollModal()" class="btn-p" style="border:none;cursor:pointer;">
      Enroll Now
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
        <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
    </button>
  </div>
  <div class="hero-courses reveal" style="margin-top:12px;">
    <div class="hero-course-label">What we teach</div>
    <div class="hero-course-chips">
      <div class="course-chip chip-flagship"><span>📊</span><span>Data Analytics Bootcamp</span><span class="chip-tag">Flagship</span></div>
      <div class="course-chip"><span>🐍</span><span>Python</span></div>
      <div class="course-chip"><span>🗄️</span><span>SQL</span></div>
      <div class="course-chip"><span>📈</span><span>Data Visualization</span></div>
      <div class="course-chip"><span>🤖</span><span>Machine Learning Algorithms</span></div>
      <div class="course-chip"><span>🎯</span><span>Recommendation Engines</span></div>
      <div class="course-chip"><span>🐙</span><span>GitHub</span></div>
      <div class="course-chip" style="border-color:rgba(0,212,255,0.50);background:rgba(0,212,255,0.10);color:#fff;"><span>🛠️</span><span>Guided projects every Saturday</span></div>
      <div class="course-chip" style="border-color:rgba(0,212,255,0.50);background:rgba(0,212,255,0.10);color:#fff;"><span>🌐</span><span>Weekly Portfolio Website Updates</span></div>
    </div>
  </div>
  <div class="hero-orbit"><div class="orbit-dot"></div></div>
  <div class="scroll-hint"><span>Scroll</span><div class="scroll-arrow"></div></div>
</section>

<hr class="glow-divider"/>

<section class="sec" id="mentors">
  <div class="sec-inner">
    <div class="reveal" style="margin-bottom:56px;">
      <span class="sec-label">// know your mentors</span>
      <h2 class="sec-title" style="white-space:nowrap;">The people who'll guide your journey</h2>
      <p class="sec-sub" style="max-width:860px;">I'm a passionate trainer with international experience in Data Analytics &amp; Data Engineering — working in France, Sweden and India with multinationals like
        <a href="https://nova.space/" target="_blank" rel="noopener" class="hero-link">Nova.space</a>,
        <a href="https://www.ironhack.com/us" target="_blank" rel="noopener" class="hero-link">Ironhack</a>,
        <a href="https://nodcoding.com/" target="_blank" rel="noopener" class="hero-link">NodCoding</a>,
        <a href="https://guardanthealth.com/" target="_blank" rel="noopener" class="hero-link">Guardant Health</a>
        and Cognizant.
      </p>
    </div>
    <div class="mentors-grid">
      <div class="mentor-card reveal">
        <div class="mentor-img-wrap">
          <img src="{SANDEEP_SRC}" alt="Sandeep Singh" class="mentor-img" />
        </div>
        <div class="mentor-info">
          <h4 class="mentor-name">Sandeep Singh</h4>
          <p class="mentor-role">Founder &amp; Lead Instructor</p>
          <p class="mentor-role" style="font-size:12px;color:rgba(255,255,255,0.50);margin-top:2px;">Senior Data Engineer at Guardant Health</p>
          <a href="https://www.linkedin.com/in/sandeepsingh1910/" target="_blank" rel="noopener" class="mentor-linkedin">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            LinkedIn
          </a>
        </div>
      </div>
      <div class="mentor-card mentor-placeholder reveal">
        <div class="mentor-img-wrap mentor-img-empty"><span class="mentor-question">?</span></div>
        <div class="mentor-info">
          <h4 class="mentor-name" style="color:rgba(255,255,255,0.5)!important;">You?</h4>
          <p class="mentor-role">You could be the next mentor</p>
          <a href="https://wa.me/918019101592?text=Hi%2C%20I%27d%20like%20to%20be%20a%20mentor%20at%20The%20Next%20Engineer!" target="_blank" rel="noopener" class="mentor-linkedin mentor-linkedin-ghost">
            <svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M8 1v14M1 8h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            Get in touch
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="enroll">
  <div class="sec-inner">
    <div class="enroll-grid reveal">
      <div>
        <span class="sec-label">// join the bootcamp</span>
        <h2 class="enroll-h2">Ready to become<br>a data analyst?</h2>
        <p class="enroll-p">Spots are limited each cohort. Apply now to secure your seat and take the first step toward your new career in data.</p>
        <ol class="steps">
          <li class="step"><div class="step-num">01</div><div class="step-text"><strong>Fill out the form</strong><span>Takes &lt;1 min.</span></div></li>
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
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="7" cy="7" r="6"/><path d="M7 4v3l2 2"/></svg>
          Response within 24 hours guaranteed
        </div>
        <div style="margin:16px 0 0;text-align:center;">
          <span style="font-size:13px;color:rgba(255,255,255,0.4);text-decoration:line-through;">₹24,999</span>
          <span style="font-size:26px;font-weight:700;color:#00e5ff;margin-left:10px;">₹19,999</span>
        </div>
        <div style="text-align:center;margin-bottom:16px;font-size:12px;color:rgba(255,255,255,0.5);">
          🎓 Scholarships for best performers at end of Week 8
        </div>
        <div class="info-box">
          <span class="info-box-lbl">Program Format</span>
          <div class="info-box-item"><span>🎥</span> 100% Live Online Classes</div>
          <div class="info-box-item"><span>📹</span> Recordings provided after every session</div>
          <div class="info-box-item"><span>📅</span> Tue &amp; Thu: 7 PM – 9 PM</div>
          <div class="info-box-item"><span>📅</span> Saturday: 10 AM – 6 PM · Guided projects</div>
          <div class="info-box-item"><span>⏱️</span> 8 Weeks · 20 seats per cohort</div>
          <div class="info-box-item"><span>🌐</span> Build your own portfolio website from Week 1</div>
          <div class="info-box-item"><span>📝</span> Assignments after every lecture</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="contact">
  <div class="sec-inner">
    <div class="contact-card reveal">
      <span class="sec-label">// let's talk</span>
      <h2 class="contact-h2">Have questions?</h2>
      <p class="contact-sub">Text your teacher directly on LinkedIn and ask for a call.</p>
      <div class="contact-btns">
        <a href="https://www.linkedin.com/in/sandeepsingh1910/" target="_blank" rel="noopener" class="btn-p">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          Text your teacher on LinkedIn
        </a>
      </div>
    </div>
  </div>
</section>

<footer class="tne-footer">
  <div class="footer-logo">The Next Engineer</div>
  <div class="footer-copy">© 2026 The Next Engineer · All rights reserved.</div>
  <div class="footer-links">
    <a href="{WA_URL}" target="_blank" rel="noopener">WhatsApp</a>
    <a href="#enroll">Enroll</a>
    <a href="#mentors">Mentors</a>
  </div>
</footer>

</div><!-- /tne-page -->
</div><!-- /tab-course -->

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

<!-- ══ Workshop Register Modal ═══════════════════════════ -->
<div id="reg-modal" class="reg-modal">
  <div class="reg-card">
    <button class="reg-close" onclick="closeRegModal()" aria-label="Close">&times;</button>
    <p class="reg-title">Reserve Your Seat</p>
    <p class="reg-sub">Workshop — ₹99 &nbsp;·&nbsp; Saturday, 18 April 2026 &nbsp;·&nbsp; 10:00 AM – 11:30 AM<br>Fill in your details — you'll be redirected to pay.</p>
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
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  #hero { min-height: 720px !important; }
</style>
</head>
<body style="margin:0;padding:0;">
"""

HTML_FOOT = f"""
<script>
var APPS_SCRIPT_URL = "{APPS_SCRIPT_URL}";
var PAYMENT_LINK    = "{PAYMENT_LINK}";

// ── Countdown ──
var cdTarget = new Date("2026-04-18T05:00:00Z");
function tick() {{
  var diff = cdTarget - new Date();
  if (diff <= 0) {{ document.querySelector('.ws-countdown') && (document.querySelector('.ws-countdown').style.display='none'); return; }}
  var pad = function(n) {{ return String(Math.floor(n)).padStart(2,'0'); }};
  document.getElementById('cd-days').textContent  = pad(diff/86400000);
  document.getElementById('cd-hours').textContent = pad((diff%86400000)/3600000);
  document.getElementById('cd-mins').textContent  = pad((diff%3600000)/60000);
  document.getElementById('cd-secs').textContent  = pad((diff%60000)/1000);
}}
tick(); setInterval(tick, 1000);

// ── Tab switching ──
function showTab(name) {{
  document.querySelectorAll('.tab-content').forEach(function(el) {{ el.classList.remove('active'); el.style.display='none'; }});
  var tab = document.getElementById('tab-' + name);
  tab.classList.add('active'); tab.style.display = 'block';
  document.querySelectorAll('.tab-btn').forEach(function(el) {{ el.classList.remove('active'); }});
  document.querySelector('[data-tab="' + name + '"]').classList.add('active');
  // Workshop banner only on course tab
  document.getElementById('ws-banner').style.display = name === 'course' ? 'flex' : 'none';
  // Sticky CTA only on workshop tab
  document.getElementById('ws-sticky').style.display = name === 'workshop' ? 'flex' : 'none';
  window.scrollTo(0, 0);
}}

// ── Workshop register modal ──
function openRegModal() {{
  document.getElementById('reg-modal').style.display = 'flex';
}}
function closeRegModal() {{
  document.getElementById('reg-modal').style.display = 'none';
  document.getElementById('reg-form').reset();
  var b = document.getElementById('reg-submit');
  if (b) {{ b.textContent = 'Proceed to Payment \u2192'; b.disabled = false; }}
}}

// ── Enroll modal ──
function openEnrollModal() {{
  document.getElementById('enroll-modal').style.display = 'flex';
}}
function closeEnrollModal() {{
  document.getElementById('enroll-modal').style.display = 'none';
  document.getElementById('enroll-form').style.display = 'block';
  document.getElementById('enroll-success').style.display = 'none';
  document.getElementById('enroll-form').reset();
  var b = document.getElementById('enroll-submit');
  if (b) {{ b.textContent = 'Submit Application \u2192'; b.disabled = false; }}
}}

document.addEventListener('DOMContentLoaded', function() {{
  // Init tab display
  showTab('workshop');

  // Backdrop close
  document.getElementById('reg-modal').addEventListener('click', function(e) {{ if (e.target===this) closeRegModal(); }});
  document.getElementById('enroll-modal').addEventListener('click', function(e) {{ if (e.target===this) closeEnrollModal(); }});

  // Workshop form submit
  document.getElementById('reg-form').addEventListener('submit', function(e) {{
    e.preventDefault();
    var btn = document.getElementById('reg-submit');
    btn.textContent = 'Saving\u2026'; btn.disabled = true;
    var body = 'name='   + encodeURIComponent(document.getElementById('reg-name').value.trim())
             + '&email=' + encodeURIComponent(document.getElementById('reg-email').value.trim())
             + '&phone=' + encodeURIComponent(document.getElementById('reg-phone').value.trim())
             + '&status='+ encodeURIComponent(document.getElementById('reg-status').value);
    fetch(APPS_SCRIPT_URL, {{ method:'POST', mode:'no-cors', headers:{{'Content-Type':'application/x-www-form-urlencoded'}}, body:body }})
    .finally(function() {{ closeRegModal(); window.open(PAYMENT_LINK,'_blank'); }});
  }});

  // Enroll form submit
  document.getElementById('enroll-form').addEventListener('submit', function(e) {{
    e.preventDefault();
    var btn = document.getElementById('enroll-submit');
    btn.textContent = 'Submitting\u2026'; btn.disabled = true;
    var body = 'formType=enroll'
             + '&name='     + encodeURIComponent(document.getElementById('enroll-name').value.trim())
             + '&email='    + encodeURIComponent(document.getElementById('enroll-email').value.trim())
             + '&phone='    + encodeURIComponent(document.getElementById('enroll-phone').value.trim())
             + '&status='   + encodeURIComponent(document.getElementById('enroll-status').value)
             + '&education='+ encodeURIComponent(document.getElementById('enroll-edu').value)
             + '&city='     + encodeURIComponent(document.getElementById('enroll-city').value.trim());
    fetch(APPS_SCRIPT_URL, {{ method:'POST', mode:'no-cors', headers:{{'Content-Type':'application/x-www-form-urlencoded'}}, body:body }})
    .finally(function() {{
      document.getElementById('enroll-form').style.display = 'none';
      document.getElementById('enroll-success').style.display = 'block';
      setTimeout(closeEnrollModal, 4000);
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
</html>"""

components.html(HTML_HEAD + page + HTML_FOOT, height=900, scrolling=True)
