# ================================================================
# ULTRA SPAM SHIELD — Advanced AI Spam Detection
# ================================================================

import streamlit as st
import pickle
import re
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
import os
from collections import Counter

# ================================================================
# PAGE CONFIG
# ================================================================

st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================================================================
# BUNDLED STOPWORDS (no internet needed)
# ================================================================

STOPWORDS = set([
    'i','me','my','myself','we','our','ours','ourselves','you','your',
    'yours','yourself','yourselves','he','him','his','himself','she',
    'her','hers','herself','it','its','itself','they','them','their',
    'theirs','themselves','what','which','who','whom','this','that',
    'these','those','am','is','are','was','were','be','been','being',
    'have','has','had','having','do','does','did','doing','a','an',
    'the','and','but','if','or','because','as','until','while','of',
    'at','by','for','with','about','against','between','into','through',
    'during','before','after','above','below','to','from','up','down',
    'in','out','on','off','over','under','again','further','then',
    'once','here','there','when','where','why','how','all','both',
    'each','few','more','most','other','some','such','no','nor','not',
    'only','own','same','so','than','too','very','s','t','can','will',
    'just','don','should','now','d','ll','m','o','re','ve','y','ain',
    'aren','couldn','didn','doesn','hadn','hasn','haven','isn','ma',
    'mightn','mustn','needn','shan','shouldn','wasn','weren','won','wouldn'
])

# ================================================================
# STEM FUNCTION (no NLTK needed)
# ================================================================

def simple_stem(word):
    suffixes = ['ing','tion','ness','ment','able','ible','ful','less',
                'ous','ive','al','er','ed','ly','es','s']
    for sfx in suffixes:
        if word.endswith(sfx) and len(word) - len(sfx) >= 3:
            return word[:-len(sfx)]
    return word

# ================================================================
# TEXT CLEANING
# ================================================================

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [simple_stem(w) for w in words if w not in STOPWORDS and len(w) > 2]
    return " ".join(words)

# ================================================================
# LOAD MODEL
# ================================================================

@st.cache_resource
def load_model():
    model_paths = [
        'best_spam_model.pkl',
        '/mnt/user-data/uploads/best_spam_model.pkl',
    ]
    for path in model_paths:
        if os.path.exists(path):
            return pickle.load(open(path, 'rb'))
    return None

model = load_model()

# ================================================================
# SPAM KEYWORDS WITH CATEGORIES
# ================================================================

SPAM_KEYWORDS = {
    "💰 Financial Lure": ['win','winner','cash','prize','money','lottery','reward','million','dollar','earn','income','profit'],
    "🎁 Free Offers": ['free','offer','gift','bonus','discount','deal','coupon','voucher','sample'],
    "⚡ Urgency Triggers": ['urgent','immediately','expires','limited','hurry','act now','deadline','now','today only'],
    "🔗 Action Bait": ['click','claim','call','subscribe','register','verify','confirm','download','apply'],
    "🏆 Too-Good Claims": ['guaranteed','100%','no risk','no cost','selected','chosen','congratulations','exclusive'],
}

SAMPLE_MESSAGES = {
    "💰 Lottery Spam": "CONGRATULATIONS! You've been selected as our lucky winner! Claim your £1,000,000 prize NOW! Call 0800-FREE-CASH or click here immediately. Offer expires today!",
    "💊 Pharma Spam": "Buy cheap meds online! No prescription needed. Lowest prices guaranteed. Free shipping. Order now and get 70% off!",
    "🏦 Phishing": "Dear customer, your account has been suspended. Verify your details immediately to avoid permanent closure. Click here to confirm.",
    "👋 Ham (Normal)": "Hey! Just checking in — are we still on for coffee Thursday? Let me know if the time works for you.",
    "📅 Ham (Work)": "Hi team, the weekly sync is moved to 3 PM tomorrow. Please review the agenda I shared earlier and come prepared.",
}

# ================================================================
# MEGA CSS
# ================================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

/* ── ROOT THEME ── */
:root {
    --bg-void:     #03050a;
    --bg-deep:     #070d16;
    --bg-card:     #0d1926;
    --bg-raised:   #112133;
    --border:      rgba(56,189,248,0.12);
    --border-glow: rgba(56,189,248,0.35);
    --cyan:        #38bdf8;
    --cyan-dim:    #0ea5e9;
    --green:       #4ade80;
    --red:         #f87171;
    --yellow:      #fbbf24;
    --purple:      #c084fc;
    --text:        #e2e8f0;
    --text-muted:  #64748b;
    --text-dim:    #94a3b8;
    --font-main:   'Space Grotesk', sans-serif;
    --font-mono:   'JetBrains Mono', monospace;
}

/* ── GLOBAL RESET ── */
html, body, [class*="st-"], .stApp {
    font-family: var(--font-main) !important;
    background: var(--bg-void) !important;
    color: var(--text) !important;
}

.stApp {
    background:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(56,189,248,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(192,132,252,0.06) 0%, transparent 60%),
        var(--bg-void) !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header { visibility: hidden !important; }
.block-container { padding: 2rem 2.5rem 3rem !important; max-width: 1400px !important; }

/* ── HERO HEADER ── */
.hero-wrap {
    position: relative;
    text-align: center;
    padding: 3rem 2rem 2rem;
    margin-bottom: 2rem;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(56,189,248,0.08);
    border: 1px solid var(--border-glow);
    border-radius: 100px;
    padding: 6px 18px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--cyan);
    margin-bottom: 1.5rem;
}
.hero-badge::before {
    content: '';
    width: 8px; height: 8px;
    background: var(--green);
    border-radius: 50%;
    box-shadow: 0 0 8px var(--green);
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%,100% { opacity:1; transform:scale(1); }
    50% { opacity:.5; transform:scale(1.4); }
}
.hero-title {
    font-size: clamp(2.4rem, 5vw, 4.5rem);
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -2px;
    background: linear-gradient(135deg, #fff 0%, var(--cyan) 50%, var(--purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
}
.hero-sub {
    font-size: 1.05rem;
    color: var(--text-dim);
    max-width: 540px;
    margin: 0 auto;
    line-height: 1.7;
    font-weight: 400;
}

/* ── CARDS ── */
.card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem;
    transition: border-color .25s;
}
.card:hover { border-color: var(--border-glow); }

.card-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: var(--cyan);
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.card-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

/* ── RESULT PANEL ── */
.result-spam {
    background: linear-gradient(135deg, rgba(248,113,113,0.12), rgba(248,113,113,0.04));
    border: 1px solid rgba(248,113,113,0.4);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    animation: fadeIn .4s ease;
}
.result-ham {
    background: linear-gradient(135deg, rgba(74,222,128,0.12), rgba(74,222,128,0.04));
    border: 1px solid rgba(74,222,128,0.4);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    animation: fadeIn .4s ease;
}
.result-idle {
    background: var(--bg-raised);
    border: 1px dashed var(--border);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    min-height: 220px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
@keyframes fadeIn {
    from { opacity:0; transform:translateY(8px); }
    to   { opacity:1; transform:translateY(0); }
}
.verdict-icon { font-size: 4rem; margin-bottom: 0.5rem; }
.verdict-title-spam { font-size: 2rem; font-weight: 700; color: var(--red); }
.verdict-title-ham  { font-size: 2rem; font-weight: 700; color: var(--green); }

/* ── STAT CARDS ── */
.stat-row { display: flex; gap: 12px; margin-bottom: 1rem; }
.stat-box {
    flex: 1;
    background: var(--bg-raised);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}
.stat-val { font-size: 2rem; font-weight: 700; font-family: var(--font-mono); }
.stat-lbl { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; margin-top: 2px; }

/* ── KEYWORD PILL ── */
.kw-pill {
    display: inline-block;
    background: rgba(251,191,36,0.12);
    border: 1px solid rgba(251,191,36,0.35);
    color: var(--yellow);
    border-radius: 100px;
    padding: 4px 14px;
    font-size: 12px;
    font-weight: 600;
    margin: 3px;
    font-family: var(--font-mono);
}
.kw-pill-safe {
    display: inline-block;
    background: rgba(74,222,128,0.08);
    border: 1px solid rgba(74,222,128,0.25);
    color: var(--green);
    border-radius: 100px;
    padding: 4px 14px;
    font-size: 12px;
    margin: 3px;
}

/* ── SECTION HEADING ── */
.section-head {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
    margin: 1.5rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-head::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, var(--border), transparent);
}

/* ── SIDEBAR OVERRIDES ── */
[data-testid="stSidebar"] {
    background: var(--bg-deep) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ── TEXTAREA ── */
textarea, .stTextArea textarea {
    background: var(--bg-raised) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: var(--font-mono) !important;
    font-size: 0.9rem !important;
    resize: vertical !important;
}
textarea:focus {
    border-color: var(--border-glow) !important;
    box-shadow: 0 0 0 3px rgba(56,189,248,0.08) !important;
}

/* ── BUTTON ── */
.stButton > button {
    background: linear-gradient(135deg, var(--cyan-dim), var(--cyan)) !important;
    color: #000 !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    padding: 0.75rem 1.5rem !important;
    letter-spacing: 0.5px;
    transition: all .2s !important;
    font-family: var(--font-main) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(56,189,248,0.3) !important;
}

/* ── SELECTBOX / RADIO ── */
.stSelectbox > div > div, .stSelectbox label {
    background: var(--bg-raised) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    border-radius: 10px !important;
}

/* ── PLOTLY BG ── */
.js-plotly-plot { background: transparent !important; }

/* ── PROGRESS ── */
.stProgress > div > div { background: var(--cyan) !important; }

/* ── HISTORY ITEM ── */
.hist-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 14px;
    background: var(--bg-raised);
    border-radius: 10px;
    margin-bottom: 8px;
    border: 1px solid var(--border);
    font-size: 0.85rem;
}
.hist-verdict { font-weight: 700; min-width: 60px; font-family: var(--font-mono); font-size: 11px; }
.hist-preview { color: var(--text-dim); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; }
</style>
""", unsafe_allow_html=True)

# ================================================================
# SESSION STATE
# ================================================================

if "history" not in st.session_state:
    st.session_state.history = []
if "scan_count" not in st.session_state:
    st.session_state.scan_count = 0
if "spam_caught" not in st.session_state:
    st.session_state.spam_caught = 0

# ================================================================
# HERO
# ================================================================

st.markdown("""
<div class="hero-wrap">
    <div class="hero-badge">🛡️ SpamShield AI &nbsp;·&nbsp; v2.0</div>
    <div class="hero-title">Detect Spam<br>Before It Strikes</div>
    <div class="hero-sub">
        Stacking Ensemble · TF-IDF · Logistic Regression · SVM · XGBoost · NLP
    </div>
</div>
""", unsafe_allow_html=True)

# ================================================================
# SIDEBAR
# ================================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem;">
        <div style="font-size: 2.5rem;">🛡️</div>
        <div style="font-size: 1.2rem; font-weight:700; color:#38bdf8; letter-spacing:-0.5px;">SpamShield AI</div>
        <div style="font-size: 11px; color:#64748b; letter-spacing:2px; text-transform:uppercase; margin-top:2px;">Threat Detection Console</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Live session stats
    st.markdown("**📊 Session Stats**")
    c1, c2 = st.columns(2)
    c1.metric("Scanned", st.session_state.scan_count)
    c2.metric("Blocked", st.session_state.spam_caught)
    if st.session_state.scan_count > 0:
        rate = int(100 * st.session_state.spam_caught / st.session_state.scan_count)
        st.progress(rate / 100)
        st.caption(f"Spam rate: {rate}%")

    st.markdown("---")

    # Model info
    st.markdown("**🧠 Model Architecture**")
    model_info = [
        ("Logistic Regression", "✅"),
        ("Linear SVM", "✅"),
        ("Naive Bayes", "✅"),
        ("XGBoost (depth=7)", "✅"),
        ("Meta: LogReg (5-fold CV)", "✅"),
        ("TF-IDF (5k feat, bigrams)", "✅"),
    ]
    for name, status in model_info:
        st.markdown(f"<div style='display:flex;justify-content:space-between;font-size:12px;padding:3px 0;'><span style='color:#94a3b8;'>{name}</span><span style='color:#4ade80;'>{status}</span></div>", unsafe_allow_html=True)

    st.markdown("---")

    # Quick load samples
    st.markdown("**⚡ Quick Load Sample**")
    sample_choice = st.selectbox("Choose a sample", ["— select —"] + list(SAMPLE_MESSAGES.keys()), label_visibility="collapsed")

    st.markdown("---")
    st.markdown("<div style='font-size:11px;color:#334155;text-align:center;'>Stacking Ensemble · NLP Pipeline<br>Built with ❤️ on scikit-learn</div>", unsafe_allow_html=True)

# ================================================================
# MAIN LAYOUT
# ================================================================

left_col, right_col = st.columns([3, 2], gap="large")

# ─── LEFT: INPUT ─────────────────────────────────────────────────
with left_col:

    st.markdown('<div class="card-label">✉️ &nbsp;Message Input</div>', unsafe_allow_html=True)

    # Pre-fill if sample chosen
    prefill = ""
    if sample_choice and sample_choice != "— select —":
        prefill = SAMPLE_MESSAGES[sample_choice]

    user_input = st.text_area(
        "Message",
        value=prefill,
        height=220,
        placeholder="Paste or type any email / SMS / message here…",
        label_visibility="collapsed"
    )

    col_btn, col_clear = st.columns([4, 1])
    with col_btn:
        analyze_btn = st.button("🚀  Analyze Message", use_container_width=True)
    with col_clear:
        clear_btn = st.button("🗑️", use_container_width=True, help="Clear input")

    if clear_btn:
        st.rerun()

    # ── MESSAGE STATISTICS ──
    if user_input.strip():
        words = user_input.split()
        chars = len(user_input)
        sentences = len(re.findall(r'[.!?]+', user_input)) or 1
        avg_word_len = round(np.mean([len(w) for w in words]), 1) if words else 0
        caps_ratio = round(sum(1 for c in user_input if c.isupper()) / max(len(user_input),1) * 100, 1)
        exclaim = user_input.count('!')
        urls = len(re.findall(r'http[s]?://', user_input))

        st.markdown('<div class="section-head">📐 Message Fingerprint</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="stat-row">
            <div class="stat-box">
                <div class="stat-val" style="color:#38bdf8;">{len(words)}</div>
                <div class="stat-lbl">Words</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color:#c084fc;">{chars}</div>
                <div class="stat-lbl">Chars</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color:#fbbf24;">{exclaim}</div>
                <div class="stat-lbl">Exclamations</div>
            </div>
            <div class="stat-box">
                <div class="stat-val" style="color:#f87171;">{caps_ratio}%</div>
                <div class="stat-lbl">CAPS Ratio</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Spam risk indicators bar chart
        indicator_scores = {
            "CAPS Usage": min(caps_ratio / 30 * 100, 100),
            "Exclamations": min(exclaim / 3 * 100, 100),
            "URLs Detected": min(urls / 2 * 100, 100),
            "Message Length": min(len(words) / 80 * 100, 100),
        }

        fig_bar = go.Figure()
        colors = ['#f87171','#fbbf24','#c084fc','#38bdf8']
        for i, (label, val) in enumerate(indicator_scores.items()):
            fig_bar.add_trace(go.Bar(
                y=[label], x=[val], orientation='h',
                marker_color=colors[i],
                marker_line_width=0,
                name=label,
                showlegend=False,
            ))
        fig_bar.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0),
            height=130,
            xaxis=dict(range=[0,100], showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, tickfont=dict(size=11, color='#94a3b8'), tickfont_family='JetBrains Mono'),
            barmode='group',
        )
        st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

    # ── KEYWORD ANALYSIS ──
    st.markdown('<div class="section-head">🚨 Keyword Analysis</div>', unsafe_allow_html=True)

    if user_input.strip():
        lower_text = user_input.lower()
        found_any = False
        for category, keywords in SPAM_KEYWORDS.items():
            hits = [kw for kw in keywords if kw in lower_text]
            if hits:
                found_any = True
                st.markdown(f"<div style='font-size:12px;color:#94a3b8;margin-bottom:4px;'>{category}</div>", unsafe_allow_html=True)
                pills = " ".join([f'<span class="kw-pill">{kw}</span>' for kw in hits])
                st.markdown(pills, unsafe_allow_html=True)
        if not found_any:
            st.markdown('<span class="kw-pill-safe">✅ No suspicious keywords found</span>', unsafe_allow_html=True)
    else:
        st.markdown("<div style='color:#334155;font-size:13px;'>Enter a message to scan for suspicious keywords…</div>", unsafe_allow_html=True)

# ─── RIGHT: RESULT ────────────────────────────────────────────────
with right_col:

    st.markdown('<div class="card-label">🔍 &nbsp;Detection Result</div>', unsafe_allow_html=True)

    if analyze_btn and user_input.strip():
        if model is None:
            st.error("❌ Model not loaded. Place `best_spam_model.pkl` in the app directory.")
        else:
            with st.spinner("Analyzing…"):
                time.sleep(0.4)

            cleaned = clean_text(user_input)
            prediction = model.predict([cleaned])[0]
            proba = model.predict_proba([cleaned])[0]
            spam_prob = round(proba[1] * 100, 1)
            ham_prob  = round(proba[0] * 100, 1)

            # Update history
            st.session_state.scan_count += 1
            if prediction == 1:
                st.session_state.spam_caught += 1

            label = "SPAM" if prediction == 1 else "HAM"
            st.session_state.history.insert(0, {
                "label": label,
                "preview": user_input[:60],
                "spam_prob": spam_prob
            })
            st.session_state.history = st.session_state.history[:10]

            if prediction == 1:
                st.markdown(f"""
                <div class="result-spam">
                    <div class="verdict-icon">🚫</div>
                    <div class="verdict-title-spam">SPAM DETECTED</div>
                    <div style="color:#f87171;font-size:0.85rem;margin-top:4px;font-weight:600;">
                        Fraudulent / Suspicious Message
                    </div>
                    <div style="margin-top:16px;font-size:2.2rem;font-weight:700;font-family:'JetBrains Mono',mono;color:#f87171;">
                        {spam_prob}%
                    </div>
                    <div style="font-size:11px;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;">Spam Confidence</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-ham">
                    <div class="verdict-icon">✅</div>
                    <div class="verdict-title-ham">LEGITIMATE</div>
                    <div style="color:#4ade80;font-size:0.85rem;margin-top:4px;font-weight:600;">
                        Ham · Safe Message
                    </div>
                    <div style="margin-top:16px;font-size:2.2rem;font-weight:700;font-family:'JetBrains Mono',mono;color:#4ade80;">
                        {ham_prob}%
                    </div>
                    <div style="font-size:11px;color:#94a3b8;letter-spacing:1px;text-transform:uppercase;">Ham Confidence</div>
                </div>
                """, unsafe_allow_html=True)

            # ── CONFIDENCE GAUGE ──
            gauge_color = "#f87171" if prediction == 1 else "#4ade80"
            gauge_val   = spam_prob if prediction == 1 else ham_prob
            gauge_label = "Spam Probability" if prediction == 1 else "Ham Probability"

            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=gauge_val,
                number={'suffix': '%', 'font': {'size': 32, 'family': 'JetBrains Mono', 'color': gauge_color}},
                title={'text': gauge_label, 'font': {'size': 12, 'color': '#64748b', 'family': 'Space Grotesk'}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 0, 'tickcolor': 'transparent', 'tickfont': {'color': '#334155', 'size': 10}},
                    'bar': {'color': gauge_color, 'thickness': 0.25},
                    'bgcolor': '#0d1926',
                    'borderwidth': 0,
                    'steps': [
                        {'range': [0, 40], 'color': 'rgba(74,222,128,0.08)'},
                        {'range': [40, 70], 'color': 'rgba(251,191,36,0.08)'},
                        {'range': [70, 100], 'color': 'rgba(248,113,113,0.08)'},
                    ],
                    'threshold': {
                        'line': {'color': gauge_color, 'width': 2},
                        'thickness': 0.75,
                        'value': gauge_val
                    }
                }
            ))
            fig_gauge.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=40, b=20, l=20, r=20),
                height=200,
                font={'family': 'Space Grotesk'}
            )
            st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})

            # ── PROBABILITY BREAKDOWN ──
            st.markdown('<div class="section-head">📊 Probability Breakdown</div>', unsafe_allow_html=True)

            fig_donut = go.Figure(data=[go.Pie(
                labels=['Ham (Safe)', 'Spam'],
                values=[ham_prob, spam_prob],
                hole=0.65,
                marker_colors=['#4ade80', '#f87171'],
                textinfo='none',
                hovertemplate='%{label}: %{value}%<extra></extra>',
            )])
            fig_donut.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=10, b=10, l=10, r=10),
                height=180,
                showlegend=True,
                legend=dict(
                    orientation='h', x=0.5, xanchor='center', y=-0.05,
                    font=dict(color='#94a3b8', size=11, family='Space Grotesk'),
                )
            )
            st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})

            # ── AI SECURITY BRIEF ──
            st.markdown('<div class="section-head">🛡️ AI Security Brief</div>', unsafe_allow_html=True)

            if prediction == 1:
                insights = [
                    ("🎯 Threat Level", "HIGH", "#f87171"),
                    ("🔴 Action", "Block & Report", "#f87171"),
                    ("⚠️ Pattern", "Promotional / Phishing", "#fbbf24"),
                ]
            else:
                insights = [
                    ("🎯 Threat Level", "NONE", "#4ade80"),
                    ("🟢 Action", "Allow", "#4ade80"),
                    ("📋 Pattern", "Normal Communication", "#38bdf8"),
                ]
            for icon_label, val, col in insights:
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;align-items:center;
                            padding:8px 12px;background:#112133;border-radius:8px;margin-bottom:6px;">
                    <span style="font-size:12px;color:#64748b;">{icon_label}</span>
                    <span style="font-size:12px;font-weight:700;color:{col};font-family:'JetBrains Mono',mono;">{val}</span>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="result-idle">
            <div style="font-size:3rem;margin-bottom:1rem;">📩</div>
            <div style="color:#475569;font-size:0.95rem;">Enter a message and click<br><strong style="color:#38bdf8;">Analyze Message</strong></div>
        </div>
        """, unsafe_allow_html=True)

# ================================================================
# SCAN HISTORY
# ================================================================

if st.session_state.history:
    st.markdown('<div class="section-head">🕐 Scan History</div>', unsafe_allow_html=True)
    for item in st.session_state.history:
        color = "#f87171" if item["label"] == "SPAM" else "#4ade80"
        st.markdown(f"""
        <div class="hist-item">
            <div class="hist-verdict" style="color:{color};">{item['label']}</div>
            <div class="hist-preview">{item['preview']}…</div>
            <div style="font-size:11px;color:{color};font-family:'JetBrains Mono',mono;white-space:nowrap;">{item['spam_prob']}% spam</div>
        </div>
        """, unsafe_allow_html=True)

# ================================================================
# FOOTER
# ================================================================

st.markdown("""
<div style="margin-top:3rem;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,0.05);
            text-align:center;color:#1e293b;font-size:12px;font-family:'JetBrains Mono',mono;">
    SPAMSHIELD AI &nbsp;·&nbsp; Stacking Ensemble (LR · SVM · NB · XGB) &nbsp;·&nbsp; TF-IDF Bigrams
</div>
""", unsafe_allow_html=True)
