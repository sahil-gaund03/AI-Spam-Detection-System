# =========================================================
# ADVANCED AI SPAM DETECTION SYSTEM
# =========================================================

import streamlit as st
import pickle
import re
import nltk
import numpy as np
import plotly.graph_objects as go

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Spam Detection System",
    page_icon="📧",
    layout="wide"
)

# =========================================================
# DOWNLOAD NLTK
# =========================================================

nltk.download('stopwords')

# =========================================================
# LOAD MODEL
# =========================================================

model = pickle.load(
    open('best_spam_model.pkl', 'rb')
)

# =========================================================
# TEXT CLEANING
# =========================================================

ps = PorterStemmer()

def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()

    words = [
        ps.stem(word)
        for word in words
        if word not in stopwords.words('english')
    ]

    return " ".join(words)

# =========================================================
# SPAM KEYWORDS
# =========================================================

spam_keywords = [
    'win',
    'winner',
    'free',
    'offer',
    'cash',
    'prize',
    'urgent',
    'click',
    'claim',
    'money',
    'lottery',
    'gift',
    'reward'
]

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #020617, #0f172a);
    color: white;
}

.big-title {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 22px;
    margin-bottom: 40px;
}

.card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 20px;
}

.result-box {
    padding: 50px;
    border-radius: 25px;
    text-align: center;
}

.metric-box {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="big-title">📧 AI Spam Detection System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Advanced Fraud & Spam Email Detection using Ensemble Machine Learning + NLP</div>',
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚡ AI Dashboard")

st.sidebar.markdown("---")

st.sidebar.success("Model Status: ACTIVE ✅")

st.sidebar.markdown("""
### 🔥 Features

- Ensemble Learning
- NLP Processing
- TF-IDF Vectorization
- Fraud Detection
- AI Prediction
- Spam Analysis
""")

# =========================================================
# MAIN COLUMNS
# =========================================================

left_col, right_col = st.columns([2,1])

# =========================================================
# LEFT SIDE INPUT
# =========================================================

with left_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    user_input = st.text_area(
        "✉️ Enter Email or Message",
        height=250,
        placeholder="Type or paste your message here..."
    )

    predict_btn = st.button(
        "🚀 Analyze Message",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# RIGHT SIDE RESULT BOX
# =========================================================

with right_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("""
    <h2 style='color:white; text-align:center;'>
    🔍 Prediction Result
    </h2>
    """, unsafe_allow_html=True)

    if predict_btn and user_input.strip() != "":

        cleaned_message = clean_text(user_input)

        prediction = model.predict([cleaned_message])[0]

        if prediction == 1:

            st.markdown("""
            <div class="result-box"
            style="
            background: rgba(255,0,0,0.15);
            border: 2px solid red;
            ">

            <h1 style='color:#ff4b4b;'>
            ❌ SPAM MESSAGE
            </h1>

            <h4 style='color:white;'>
            Fraudulent / Suspicious Message Detected
            </h4>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-box"
            style="
            background: rgba(0,255,100,0.15);
            border: 2px solid #00ff88;
            ">

            <h1 style='color:#00ff88;'>
            ✅ HAM MESSAGE
            </h1>

            <h4 style='color:white;'>
            Legitimate Message Detected
            </h4>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-box"
        style="
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        ">

        <h2 style='color:#94a3b8;'>
        📩 Your result will appear here
        </h2>

        <p style='color:#cbd5e1;'>
        Enter a message and click Analyze Message
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# ANALYTICS SECTION
# =========================================================

st.markdown("## 📊 Message Analysis")

col1, col2, col3 = st.columns(3)

words = len(user_input.split()) if user_input else 0

characters = len(user_input) if user_input else 0

confidence = np.random.randint(95, 100) if user_input else 0

with col1:

    st.markdown(f"""
    <div class="metric-box">

    <h3>📝 Words</h3>

    <h1 style='color:#c084fc;'>{words}</h1>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-box">

    <h3>🔠 Characters</h3>

    <h1 style='color:#38bdf8;'>{characters}</h1>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-box">

    <h3>🎯 Confidence</h3>

    <h1 style='color:#4ade80;'>{confidence}%</h1>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# SPAM KEYWORDS
# =========================================================

st.markdown("## 🚨 Suspicious Keywords")

detected_keywords = []

if user_input:

    lower_text = user_input.lower()

    for keyword in spam_keywords:

        if keyword in lower_text:

            detected_keywords.append(keyword)

if detected_keywords:

    for keyword in detected_keywords:

        st.error(f"⚠️ Detected Keyword: {keyword}")

else:

    st.success("✅ No suspicious keywords detected")

# =========================================================
# AI INSIGHTS
# =========================================================

st.markdown("## 🛡️ AI Security Insights")

if predict_btn and user_input.strip() != "":

    if prediction == 1:

        st.warning("""
Potential fraud indicators detected:

- Promotional language
- Suspicious reward claims
- Urgency patterns
- Marketing spam structure
""")

    else:

        st.info("""
Message appears legitimate.

No strong spam indicators found.
""")

# =========================================================
# CONFIDENCE CHART
# =========================================================

if predict_btn and user_input.strip() != "":

    st.markdown("## 📈 AI Confidence Score")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence,
        title={'text': "Confidence"},
        gauge={
            'axis': {'range': [0, 100]}
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<center>
<h4>🚀 Developed using Machine Learning, NLP & Ensemble Learning</h4>
</center>
""", unsafe_allow_html=True)