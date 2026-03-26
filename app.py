import streamlit as st
from crew_setup import hospitality_crew

st.set_page_config(
    page_title="TravelCrew — AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,300;1,400&family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

:root {
    --bg:        #09090b;
    --bg2:       #0f0f12;
    --surface:   #131318;
    --surface2:  #1a1a22;
    --border:    rgba(255,255,255,0.07);
    --border2:   rgba(255,255,255,0.13);
    --text:      #f4f4f5;
    --muted:     #71717a;
    --dim:       #3f3f46;
    --amber:     #f59e0b;
    --amber-dim: rgba(245,158,11,0.12);
    --amber-glow:rgba(245,158,11,0.08);
    --green:     #4ade80;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg);
    color: var(--text);
    -webkit-font-smoothing: antialiased;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ════════════════════════════════
   HERO
════════════════════════════════ */
.tc-hero {
    min-height: 100vh;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 0 6vw 5rem;
}

.tc-hero::before {
    content: '';
    position: absolute;
    top: -20%;
    right: -10%;
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, rgba(245,158,11,0.06) 0%, transparent 65%);
    pointer-events: none;
}

.tc-hero::after {
    content: '';
    position: absolute;
    bottom: -15%;
    left: -5%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(99,102,241,0.05) 0%, transparent 65%);
    pointer-events: none;
}

.tc-grid-bg {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.018) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.018) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
}

.tc-nav {
    position: absolute;
    top: 0; left: 0; right: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.8rem 6vw;
    border-bottom: 1px solid var(--border);
    backdrop-filter: blur(8px);
    background: rgba(9,9,11,0.6);
    z-index: 10;
}

.tc-nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: white;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}
.tc-nav-logo-dot {
    width: 7px; height: 7px;
    background: var(--amber);
    border-radius: 50%;
    animation: pulse-amber 2.5s infinite;
}
.tc-nav-links {
    display: flex;
    gap: 2.5rem;
    align-items: center;
}
.tc-nav-link {
    font-size: 0.8rem;
    color: var(--muted);
    letter-spacing: 0.03em;
    text-decoration: none;
    transition: color 0.2s;
    font-weight: 500;
}
.tc-nav-link:hover { color: var(--text); }

.tc-nav-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--amber-dim);
    border: 1px solid rgba(245,158,11,0.25);
    color: var(--amber);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    padding: 0.4rem 1rem;
    border-radius: 999px;
}
.tc-nav-badge-dot {
    width: 5px; height: 5px;
    background: var(--amber);
    border-radius: 50%;
}

.tc-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: var(--amber);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 2rem;
    opacity: 0.9;
}
.tc-eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px;
    height: 1px;
    background: var(--amber);
    opacity: 0.6;
}

.tc-hero-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3.5rem, 9vw, 9rem);
    font-weight: 900;
    line-height: 0.92;
    color: white;
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
}
.tc-hero-title em {
    font-style: italic;
    font-weight: 400;
    background: linear-gradient(135deg, rgba(245,158,11,0.9), rgba(251,191,36,0.5));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.tc-hero-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 3.5rem;
    padding-top: 2.5rem;
    border-top: 1px solid var(--border);
    position: relative;
    z-index: 1;
}

.tc-hero-sub {
    font-size: 1rem;
    color: var(--muted);
    font-weight: 300;
    max-width: 400px;
    line-height: 1.9;
    letter-spacing: 0.01em;
}

.tc-hero-stats {
    display: flex;
    gap: 3rem;
    text-align: right;
}
.tc-stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 900;
    color: white;
    display: block;
    line-height: 1;
}
.tc-stat-num.amber { color: var(--amber); }
.tc-stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    color: var(--dim);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-top: 0.35rem;
}

/* ════════════════════════════════
   MARQUEE
════════════════════════════════ */
.tc-marquee-wrap {
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    overflow: hidden;
    padding: 0.9rem 0;
    background: var(--bg2);
}
.tc-marquee {
    display: flex;
    animation: marquee 28s linear infinite;
    white-space: nowrap;
}
.tc-marquee-item {
    font-family: 'DM Mono', monospace;
    font-size: 0.63rem;
    font-weight: 400;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--dim);
    padding: 0 3rem;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
.tc-marquee-accent { color: var(--amber); opacity: 0.6; }

@keyframes marquee {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

/* ════════════════════════════════
   SECTIONS
════════════════════════════════ */
.tc-section {
    padding: 7rem 6vw;
}
.tc-section-inner {
    max-width: 1380px;
    margin: 0 auto;
}
.tc-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--amber);
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    opacity: 0.85;
}
.tc-label::before {
    content: '';
    display: inline-block;
    width: 20px;
    height: 1px;
    background: var(--amber);
    opacity: 0.5;
}
.tc-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.2rem, 4.5vw, 4.2rem);
    font-weight: 900;
    line-height: 1.05;
    color: white;
    margin-bottom: 4rem;
    letter-spacing: -0.015em;
}
.tc-heading em {
    font-style: italic;
    font-weight: 400;
    color: rgba(255,255,255,0.35);
}

/* ════════════════════════════════
   AGENT CARDS
════════════════════════════════ */
.tc-agents {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.tc-agent {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 2.5rem;
    transition: border-color 0.3s, background 0.3s, transform 0.25s;
    position: relative;
    overflow: hidden;
}
.tc-agent::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(245,158,11,0.3), transparent);
    opacity: 0;
    transition: opacity 0.3s;
}
.tc-agent:hover {
    border-color: rgba(245,158,11,0.2);
    background: var(--surface2);
    transform: translateY(-2px);
}
.tc-agent:hover::after { opacity: 1; }

.tc-agent-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    color: var(--amber);
    text-transform: uppercase;
    margin-bottom: 1.8rem;
    opacity: 0.7;
}

.tc-agent-icon {
    width: 52px; height: 52px;
    border: 1px solid var(--border2);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
    background: var(--amber-glow);
    box-shadow: 0 0 20px rgba(245,158,11,0.05);
}

.tc-agent-name {
    font-family: 'Playfair Display', serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: white;
    margin-bottom: 1rem;
    line-height: 1.25;
}

.tc-agent-desc {
    font-size: 0.85rem;
    color: var(--muted);
    line-height: 1.85;
    margin-bottom: 1.8rem;
    font-weight: 300;
}

.tc-chips { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.tc-chip {
    border: 1px solid var(--border2);
    color: var(--dim);
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    padding: 0.3rem 0.75rem;
    border-radius: 5px;
    text-transform: uppercase;
    background: rgba(255,255,255,0.02);
    transition: border-color 0.2s, color 0.2s;
}
.tc-agent:hover .tc-chip {
    border-color: rgba(245,158,11,0.18);
    color: rgba(245,158,11,0.6);
}

/* ════════════════════════════════
   HOW IT WORKS — STEPS
════════════════════════════════ */
.tc-steps {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 0;
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    background: var(--surface);
}
.tc-step {
    padding: 2.5rem;
    border-right: 1px solid var(--border);
    position: relative;
}
.tc-step:last-child { border-right: none; }
.tc-step-n {
    font-family: 'Playfair Display', serif;
    font-size: 3.5rem;
    font-weight: 900;
    color: rgba(255,255,255,0.06);
    line-height: 1;
    margin-bottom: 1.2rem;
}
.tc-step-title {
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 0.6rem;
    letter-spacing: 0.01em;
}
.tc-step-desc {
    font-size: 0.8rem;
    color: var(--muted);
    line-height: 1.8;
    font-weight: 300;
}

/* ════════════════════════════════
   FORM
════════════════════════════════ */
.tc-form-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 24px;
    overflow: hidden;
    box-shadow: 0 0 80px rgba(0,0,0,0.4);
}
.tc-form-top {
    padding: 2.8rem 3rem;
    border-bottom: 1px solid var(--border);
    background: var(--surface2);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.tc-form-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 900;
    color: white;
    line-height: 1.25;
    letter-spacing: -0.01em;
}
.tc-form-heading em {
    font-style: italic;
    font-weight: 400;
    color: var(--amber);
}
.tc-form-body { padding: 2.5rem 3rem; }

.tc-field-group {
    margin-bottom: 0;
}
.tc-field-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.58rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--amber);
    display: block;
    margin-bottom: 1rem;
    margin-top: 2.2rem;
    padding-top: 2.2rem;
    border-top: 1px solid var(--border);
    opacity: 0.8;
}
.tc-field-label:first-child { margin-top: 0; padding-top: 0; border-top: none; }

.tc-sub-label {
    font-size: 0.7rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.5rem;
    font-weight: 500;
}

/* ── Streamlit form overrides ── */
.stTextInput > div > div > input {
    background: var(--bg) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 300 !important;
    padding: 0.9rem 1.2rem !important;
    transition: border-color 0.25s, box-shadow 0.25s !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(245,158,11,0.35) !important;
    box-shadow: 0 0 0 3px rgba(245,158,11,0.08) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder {
    color: var(--dim) !important;
    font-style: italic;
}
.stTextInput label { display: none !important; }

div[data-baseweb="select"] > div {
    background: var(--bg) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 300 !important;
    transition: border-color 0.25s !important;
}
div[data-baseweb="select"] > div:focus-within {
    border-color: rgba(245,158,11,0.35) !important;
    box-shadow: 0 0 0 3px rgba(245,158,11,0.08) !important;
}
div[data-baseweb="select"] svg { color: var(--dim) !important; }
.stSelectbox label { display: none !important; }

div[data-baseweb="popover"] {
    background: #18181f !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    box-shadow: 0 20px 60px rgba(0,0,0,0.6) !important;
}
li[role="option"] {
    color: var(--muted) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 300 !important;
}
li[role="option"]:hover {
    background: rgba(245,158,11,0.07) !important;
    color: var(--text) !important;
}

/* Slider */
.stSlider > div > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 4px !important;
}
.stSlider > div > div > div > div { background: var(--amber) !important; }
.stSlider label { display: none !important; }
[data-testid="stSliderThumb"] { background: var(--amber) !important; border: none !important; }
[data-testid="stSliderThumbValue"] { color: var(--amber) !important; }

/* Multiselect */
div[data-testid="stMultiSelect"] > div {
    background: var(--bg) !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important;
    transition: border-color 0.25s !important;
}
div[data-testid="stMultiSelect"] > div:focus-within {
    border-color: rgba(245,158,11,0.35) !important;
    box-shadow: 0 0 0 3px rgba(245,158,11,0.08) !important;
}
.stMultiSelect label { display: none !important; }
div[data-baseweb="tag"] {
    background: var(--amber-dim) !important;
    border: 1px solid rgba(245,158,11,0.25) !important;
    border-radius: 6px !important;
    color: var(--amber) !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}

/* ── PRIMARY BUTTON ── */
.stButton > button {
    background: var(--amber) !important;
    color: #09090b !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    padding: 1rem 2.5rem !important;
    width: 100% !important;
    margin-top: 2rem !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(245,158,11,0.25) !important;
}
.stButton > button:hover {
    background: #fbbf24 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(245,158,11,0.35) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 10px rgba(245,158,11,0.2) !important;
}

/* ── SUMMARY PILLS ── */
.tc-summary {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1.8rem;
    padding: 1.3rem 1.5rem;
    background: var(--amber-glow);
    border: 1px solid rgba(245,158,11,0.12);
    border-radius: 12px;
}
.tc-pill {
    background: rgba(245,158,11,0.1);
    border: 1px solid rgba(245,158,11,0.2);
    color: rgba(245,158,11,0.85);
    font-size: 0.73rem;
    font-weight: 500;
    padding: 0.3rem 0.9rem;
    border-radius: 999px;
    letter-spacing: 0.03em;
    font-family: 'DM Sans', sans-serif;
}

/* ── STATUS ── */
.tc-status {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(74,222,128,0.07);
    border: 1px solid rgba(74,222,128,0.2);
    color: var(--green);
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    padding: 0.45rem 1.1rem;
    border-radius: 999px;
    margin-bottom: 1.5rem;
}
.tc-status-dot {
    width: 5px; height: 5px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse-green 1.5s infinite;
}

/* ── RESULT ── */
.tc-result {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 3rem;
    margin-top: 1.5rem;
    position: relative;
    overflow: hidden;
}
.tc-result::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--amber), transparent);
    opacity: 0.5;
}
.tc-result-header {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.8rem, 3.5vw, 2.8rem);
    font-weight: 900;
    color: white;
    margin-bottom: 0.5rem;
    line-height: 1.15;
    letter-spacing: -0.015em;
}
.tc-result-header em {
    font-style: italic;
    font-weight: 400;
    color: var(--amber);
}
.tc-result-meta {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: var(--dim);
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border);
    margin-top: 0.8rem;
}
.tc-result-body {
    color: #a1a1aa;
    font-size: 0.95rem;
    line-height: 2;
    white-space: pre-wrap;
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
}

/* ── FOOTER ── */
.tc-footer {
    padding: 2.5rem 6vw;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg2);
}
.tc-footer-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: white;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.tc-footer-logo-dot {
    width: 6px; height: 6px;
    background: var(--amber);
    border-radius: 50%;
    opacity: 0.7;
}
.tc-footer-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.62rem;
    color: var(--dim);
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* ── ANIMATIONS ── */
@keyframes pulse-amber {
    0%,100% { opacity: 1; box-shadow: 0 0 0 0 rgba(245,158,11,0.5); }
    50%      { opacity: 0.7; box-shadow: 0 0 0 5px rgba(245,158,11,0); }
}
@keyframes pulse-green {
    0%,100% { opacity: 1; box-shadow: 0 0 0 0 rgba(74,222,128,0.4); }
    50%      { opacity: 0.6; box-shadow: 0 0 0 5px rgba(74,222,128,0); }
}

/* ── SPINNER ── */
.stSpinner > div { border-top-color: var(--amber) !important; }

/* ── RESPONSIVE ── */
@media (max-width: 768px) {
    .tc-agents { grid-template-columns: 1fr; }
    .tc-steps  { grid-template-columns: 1fr; }
    .tc-step   { border-right: none; border-bottom: 1px solid var(--border); }
    .tc-step:last-child { border-bottom: none; }
    .tc-hero-bottom { flex-direction: column; gap: 2rem; }
    .tc-hero-stats  { text-align: left; }
    .tc-nav-links   { display: none; }
    .tc-form-top    { flex-direction: column; gap: 1rem; }
    .tc-form-body   { padding: 1.5rem; }
    .tc-result      { padding: 1.8rem; }
    .tc-footer      { flex-direction: column; gap: 1rem; text-align: center; }
}

.stWarning { border-radius: 10px !important; }
</style>
""")

# ══════════════════════════════
# HERO
# ══════════════════════════════
st.html("""
<div class="tc-hero">
    <div class="tc-grid-bg"></div>

    <div class="tc-nav">
        <div class="tc-nav-logo">
            <div class="tc-nav-logo-dot"></div>
            TravelCrew
        </div>
        <div class="tc-nav-links">
            <a class="tc-nav-link" href="#">How it works</a>
            <a class="tc-nav-link" href="#">Destinations</a>
            <a class="tc-nav-link" href="#">About</a>
        </div>
        <div class="tc-nav-badge">
            <div class="tc-nav-badge-dot"></div>
            AI Agents Live
        </div>
    </div>

    <div style="position:relative; z-index:1;">
        <div class="tc-eyebrow">AI-Powered Travel Planning</div>
        <h1 class="tc-hero-title">Your next<br><em>adventure</em><br>awaits.</h1>

        <div class="tc-hero-bottom">
            <p class="tc-hero-sub">Two specialized AI agents research your destination and craft a
            personalized, day-by-day itinerary — tailored exactly to how you want to travel.</p>
            <div class="tc-hero-stats">
                <div>
                    <span class="tc-stat-num amber">2</span>
                    <div class="tc-stat-label">AI Agents</div>
                </div>
                <div>
                    <span class="tc-stat-num">3</span>
                    <div class="tc-stat-label">Intel Layers</div>
                </div>
                <div>
                    <span class="tc-stat-num">&#8734;</span>
                    <div class="tc-stat-label">Destinations</div>
                </div>
            </div>
        </div>
    </div>
</div>
""")

# ── MARQUEE ──
st.html("""
<div class="tc-marquee-wrap">
    <div class="tc-marquee">
        <span class="tc-marquee-item">CrewAI Multi-Agent <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Groq LLaMA 3.3 70B <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">ChromaDB RAG <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Serper Web Search <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Sequential Hand-off <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Datagami AAI-08 <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">CrewAI Multi-Agent <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Groq LLaMA 3.3 70B <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">ChromaDB RAG <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Serper Web Search <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Sequential Hand-off <span class="tc-marquee-accent">&#10022;</span></span>
        <span class="tc-marquee-item">Datagami AAI-08 <span class="tc-marquee-accent">&#10022;</span></span>
    </div>
</div>
""")

# ══════════════════════════════
# AGENTS SECTION
# ══════════════════════════════
st.html("""
<div class="tc-section">
<div class="tc-section-inner">
    <div class="tc-label">Meet The Crew</div>
    <h2 class="tc-heading">Two agents.<br><em>One perfect itinerary.</em></h2>
    <div class="tc-agents">
        <div class="tc-agent">
            <div class="tc-agent-num">Agent 01 — Research</div>
            <div class="tc-agent-icon">&#128269;</div>
            <div class="tc-agent-name">Research Specialist</div>
            <div class="tc-agent-desc">Queries the ChromaDB travel knowledge base first, then supplements with live Google Search via Serper API. Returns hotels, restaurants, attractions, weather, transport, and insider tips.</div>
            <div class="tc-chips">
                <span class="tc-chip">ChromaDB RAG</span>
                <span class="tc-chip">Serper Search</span>
                <span class="tc-chip">Groq LLaMA 3.3</span>
            </div>
        </div>
        <div class="tc-agent">
            <div class="tc-agent-num">Agent 02 — Writer</div>
            <div class="tc-agent-icon">&#9997;</div>
            <div class="tc-agent-name">Itinerary Writer</div>
            <div class="tc-agent-desc">Receives the full research report via CrewAI's context hand-off protocol and synthesizes it into a beautifully structured, day-by-day itinerary with budget estimates and practical tips.</div>
            <div class="tc-chips">
                <span class="tc-chip">CrewAI Context</span>
                <span class="tc-chip">Hand-off Protocol</span>
                <span class="tc-chip">Groq LLaMA 3.3</span>
            </div>
        </div>
    </div>

    <div class="tc-steps">
        <div class="tc-step">
            <div class="tc-step-n">01</div>
            <div class="tc-step-title">You describe your trip</div>
            <div class="tc-step-desc">Enter your destination, duration, travel style, and interests. Takes 30 seconds.</div>
        </div>
        <div class="tc-step">
            <div class="tc-step-n">02</div>
            <div class="tc-step-title">AI agents go to work</div>
            <div class="tc-step-desc">The Research Specialist gathers intel. The Writer synthesizes it into a full plan.</div>
        </div>
        <div class="tc-step">
            <div class="tc-step-n">03</div>
            <div class="tc-step-title">Your itinerary is ready</div>
            <div class="tc-step-desc">Get a personalized day-by-day schedule with hotels, dining, and budget breakdowns.</div>
        </div>
    </div>
</div>
</div>
""")

# ══════════════════════════════
# FORM SECTION — HEADING
# ══════════════════════════════
st.html("""
<div class="tc-section" style="padding-top:0; padding-bottom:2rem;">
<div class="tc-section-inner">
    <div class="tc-label">Plan Your Trip</div>
    <h2 class="tc-heading">Tell us how<br><em>you want to travel.</em></h2>
</div>
</div>
""")

# ══════════════════════════════
# FORM CARD — TOP HEADER
# (fully self-contained, no open divs)
# ══════════════════════════════
_, col, _ = st.columns([1, 10, 1])
with col:

    # Card top header — fully closed
    st.html("""
    <div class="tc-form-card">
        <div class="tc-form-top">
            <div class="tc-form-heading">Your travel <em>preferences</em></div>
        </div>
    </div>
    """)

    # ── 01 Destination & Duration ──
    st.html('<p class="tc-field-label" style="padding:1.5rem 0 0.5rem; margin:0 0 0.5rem; border:none; opacity:0.8; font-family:\'DM Mono\',monospace; font-size:0.58rem; letter-spacing:0.22em; text-transform:uppercase; color:#f59e0b;">01 — Destination &amp; Duration</p>')

    d_col, days_col = st.columns([3, 2])
    with d_col:
        destination = st.text_input("dest", placeholder="Tokyo, Paris, Bali, Rajasthan…", label_visibility="collapsed")
    with days_col:
        st.html("<p class='tc-sub-label'>Number of days</p>")
        num_days = st.slider("days", 1, 14, 5, label_visibility="collapsed")

    # ── 02 Travel Style ──
    st.html('<p style="padding-top:1.5rem; margin-bottom:0.5rem; border-top:1px solid rgba(255,255,255,0.07); font-family:\'DM Mono\',monospace; font-size:0.58rem; letter-spacing:0.22em; text-transform:uppercase; color:#f59e0b; opacity:0.8;">02 — Travel Style</p>')

    t_col, b_col = st.columns(2)
    with t_col:
        st.html("<p class='tc-sub-label'>Who is travelling?</p>")
        travel_type = st.selectbox("who",
            ["Solo", "Couple", "Family with kids", "Group of friends", "Business trip"],
            label_visibility="collapsed")
    with b_col:
        st.html("<p class='tc-sub-label'>Budget range</p>")
        budget = st.selectbox("budget",
            ["Budget (₹0–₹3,000/day)", "Mid-range (₹3,000–₹8,000/day)", "Luxury (₹8,000+/day)"],
            label_visibility="collapsed")

    # ── 03 Interests ──
    st.html('<p style="padding-top:1.5rem; margin-bottom:0.5rem; border-top:1px solid rgba(255,255,255,0.07); font-family:\'DM Mono\',monospace; font-size:0.58rem; letter-spacing:0.22em; text-transform:uppercase; color:#f59e0b; opacity:0.8;">03 — Interests &amp; Activities</p>')
    st.html("<p class='tc-sub-label'>What excites you?</p>")
    interests = st.multiselect("interests",
        ["Food & Dining", "Culture & History", "Adventure & Outdoor", "Shopping",
         "Nightlife", "Nature & Wildlife", "Art & Museums", "Relaxation & Wellness",
         "Photography Spots", "Local Markets"],
        default=["Food & Dining", "Culture & History"],
        label_visibility="collapsed")

    # ── 04 Special Requirements ──
    st.html('<p style="padding-top:1.5rem; margin-bottom:0.5rem; border-top:1px solid rgba(255,255,255,0.07); font-family:\'DM Mono\',monospace; font-size:0.58rem; letter-spacing:0.22em; text-transform:uppercase; color:#f59e0b; opacity:0.8;">04 — Special Requirements <span style="opacity:0.4; font-style:italic; letter-spacing:0; text-transform:none;">(optional)</span></p>')
    special = st.text_input("special",
        placeholder="Vegetarian, halal, wheelchair accessible, avoid spicy food…",
        label_visibility="collapsed")

    # ── Live preview summary ──
    if destination:
        interests_display = " · ".join(interests) if interests else "General"
        budget_short = budget.split("(")[0].strip()
        special_pill = f"<span class='tc-pill'>&#9889; {special}</span>" if special.strip() else ""
        st.html(f"""
        <div class="tc-summary">
            <span class="tc-pill">&#128205; {destination}</span>
            <span class="tc-pill">&#128197; {num_days} days</span>
            <span class="tc-pill">&#128101; {travel_type}</span>
            <span class="tc-pill">&#128176; {budget_short}</span>
            <span class="tc-pill">&#127919; {interests_display}</span>
            {special_pill}
        </div>
        """)

    plan_clicked = st.button("✦ Generate My Itinerary")

# ══════════════════════════════
# RUN CREW
# ══════════════════════════════
if plan_clicked:
    if not destination.strip():
        st.warning("Please enter a destination to get started.")
    else:
        interests_str = ", ".join(interests) if interests else "general sightseeing"
        special_str   = f" Special requirements: {special}." if special.strip() else ""
        budget_clean  = budget.split("(")[0].strip()

        travel_request = (
            f"{num_days} days in {destination} for {travel_type.lower()}. "
            f"Budget: {budget_clean}. Interests: {interests_str}.{special_str} "
            f"Provide hotels, restaurants, attractions, day-by-day schedule, transport tips, and budget breakdown."
        )

        with st.spinner(f"Crafting your {num_days}-day {destination} itinerary…"):
            result = hospitality_crew.kickoff(inputs={"travel_request": travel_request})

        interests_display = " · ".join(interests) if interests else "General"
        budget_short = budget.split("(")[0].strip()

        _, res_col, _ = st.columns([1, 10, 1])
        with res_col:
            st.html(f"""
            <div class="tc-status"><div class="tc-status-dot"></div> Itinerary Ready</div>
            <div class="tc-result">
                <div class="tc-result-header">Your <em>{destination}</em> Itinerary</div>
                <div class="tc-result-meta">
                    {num_days} days &nbsp;&middot;&nbsp; {travel_type} &nbsp;&middot;&nbsp; {budget_short} &nbsp;&middot;&nbsp; {interests_display}
                </div>
                <div class="tc-result-body">{str(result)}</div>
            </div>
            """)

# ══════════════════════════════
# FOOTER
# ══════════════════════════════
st.html("""
<div class="tc-footer">
    <div class="tc-footer-logo">
        <div class="tc-footer-logo-dot"></div>
        TravelCrew
    </div>
    <div class="tc-footer-sub">CrewAI &middot; Groq LLaMA 3.3 &middot; ChromaDB &middot; Serper &middot; Datagami AAI-08</div>
</div>
""")

    


