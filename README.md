<div align="center">

<!-- HERO BANNER TEXT -->
<h1>
  <img src="https://readme-typing-svg.demolab.com?font=Syne&weight=700&size=36&pause=1000&color=06B6D4&center=true&vCenter=true&width=600&lines=🛡️+SpamShield+AI;Spam+%26+Fraud+Detection;Powered+by+Ensemble+ML+%2B+NLP" alt="SpamShield AI" />
</h1>

<p>
  <b>Enterprise-grade email & SMS spam detection — built with Ensemble Machine Learning,<br>
  NLP preprocessing, TF-IDF Vectorization, and an interactive Streamlit dashboard.</b>
</p>

<!-- BADGES -->
<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3b82f6?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge&logo=xgboost&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLTK-NLP-8b5cf6?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge"/>
</p>

<!-- QUICK LINKS -->
<p>
  <a href="https://ai-spam-detection-system0310.streamlit.app/"><img src="https://img.shields.io/badge/🚀 Live Demo-Click Here-06b6d4?style=for-the-badge"/></a>
  &nbsp;
  <a href="https://github.com/sahil-gaund03/AI-Spam-Detection-System/issues"><img src="https://img.shields.io/badge/🐛 Report Bug-issues-ef4444?style=for-the-badge"/></a>
  &nbsp;
  <a href="https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset"><img src="https://img.shields.io/badge/📦 Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"/></a>
</p>

---
<h3>Live Demo: https://ai-spam-detection-system-03.streamlit.app/</h3>
</div>

## 📌 Table of Contents

- [✨ Overview](#-overview)
- [📊 Model Performance](#-model-performance)
- [🔥 Features](#-features)
- [🧠 ML Pipeline](#-ml-pipeline)
- [⚙️ Algorithms Used](#️-algorithms-used)
- [📂 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [🧪 Example Predictions](#-example-predictions)
- [🧰 Tech Stack](#-tech-stack)
- [📊 Dataset](#-dataset)
- [🌟 Roadmap](#-roadmap)
- [👨‍💻 Author](#-author)
- [📜 License](#-license)

---

## ✨ Overview

**SpamShield AI** is a full-stack machine learning application that classifies messages as **Spam** or **Ham (Legitimate)** with 97–99% accuracy. It combines classical NLP techniques with an ensemble of powerful classifiers, wrapped in a sleek real-time Streamlit dashboard.

> Built for developers, data scientists, and security researchers who want a production-ready spam detection system they can extend, deploy, and learn from.

```
Input Message  →  NLP Preprocessing  →  TF-IDF  →  Ensemble Model  →  Prediction + Insights
```

---

## 📊 Model Performance

<div align="center">

| Metric | Score |
|:-------|:-----:|
| ✅ **Accuracy** | `97% – 99%` |
| 🎯 **Precision** | `96% – 99%` |
| 🔍 **Recall** | `95% – 99%` |
| ⚡ **F1 Score** | `96% – 99%` |

> Evaluated on the **SMS Spam Collection Dataset** (5,574 messages) with stratified k-fold cross-validation.

</div>

---

## 🔥 Features

<table>
<tr>
<td width="50%">

**🤖 AI & ML**
- Stacking Ensemble Classifier (meta-learner)
- TF-IDF Vectorization for feature extraction
- NLTK stemming + stopword removal
- Real-time confidence scoring (gauge chart)
- Suspicious keyword pattern analysis

</td>
<td width="50%">

**🎨 UI & Dashboard**
- Professional dark UI (glassmorphism design)
- Live word/character/sentence counter
- Word frequency bar chart with spam highlights
- AI Security Insights panel
- One-click sample Spam / Ham loader

</td>
</tr>
</table>

---

## 🧠 ML Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                   Raw Input Message                     │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│              NLP Text Preprocessing (NLTK)              │
│  • Lowercase  • Remove special chars  • Tokenization    │
│  • Stopword removal  • Porter Stemming                  │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│               TF-IDF Vectorization                      │
│       Converts cleaned text → numerical features        │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────────────────────┐
│                    Base Classifiers                            │
│  ┌──────────────┐  ┌───────────────────┐  ┌────────────────┐  │
│  │ Naive Bayes  │  │ Logistic Regress. │  │  Linear SVM    │  │
│  └──────────────┘  └───────────────────┘  └────────────────┘  │
│                   ┌──────────────────┐                         │
│                   │    XGBoost       │                         │
│                   └──────────────────┘                         │
└────────────────────────┬───────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│           Stacking Ensemble (Meta-Learner)               │
│         Combines base predictions intelligently          │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│         Final Prediction + Confidence Score             │
│              ✅ HAM  /  🚨 SPAM                         │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Algorithms Used

| Algorithm | Type | Role |
|:----------|:-----|:-----|
| **Multinomial Naive Bayes** | Probabilistic | Base classifier — fast & strong on text |
| **Logistic Regression** | Linear | Base classifier — high precision |
| **Linear SVM** | Kernel | Base classifier — robust boundary detection |
| **XGBoost** | Gradient Boosting | Base classifier — handles complex patterns |
| **Stacking Ensemble** | Meta-Learner | Combines all predictions for final output |

---

## 📂 Project Structure

```bash
AI-Spam-Detection-System/
│
├── 📄 app.py                      # Streamlit web app (enhanced UI)
├── 🧠 best_spam_model.pkl         # Pre-trained stacking ensemble model
├── 📋 requirements.txt            # Python dependencies
├── 📖 README.md                   # You are here
│
├── 📁 data/
│   └── spam.csv                   # SMS Spam Collection dataset (5,574 msgs)
│
└── 📁 notebook/
    └── spam_detection.ipynb       # EDA, model training & evaluation
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip

### 1 · Clone the Repository

```bash
git clone https://github.com/sahil-gaund03/AI-Spam-Detection-System.git
cd AI-Spam-Detection-System
```

### 2 · Create & Activate a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python -m venv venv
source venv/bin/activate
```

### 3 · Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 · Launch the App

```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser. That's it! 🎉

> **Note:** The pre-trained model (`best_spam_model.pkl`) is included in the repo — no retraining needed. To retrain from scratch, run `spam_detection.ipynb` end-to-end.

---

## 🧪 Example Predictions

| Message | Prediction | Reason |
|:--------|:----------:|:-------|
| `Congratulations! You've won a FREE iPhone — claim now!` | 🚨 **SPAM** | Prize claim + urgency language |
| `Hey, are we still meeting tomorrow at 3pm?` | ✅ **HAM** | Normal conversational tone |
| `URGENT: Your account will be suspended. Verify now!` | 🚨 **SPAM** | Urgency + fear-based manipulation |
| `Please send the updated report by Friday evening.` | ✅ **HAM** | Legitimate business request |
| `You have been SELECTED for an exclusive limited offer!` | 🚨 **SPAM** | Promotional + exclusivity trigger words |

---

## 🧰 Tech Stack

<div align="center">

| Technology | Purpose |
|:-----------|:--------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Core backend & ML |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) | Interactive web dashboard |
| ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white) | ML pipeline & ensemble |
| ![XGBoost](https://img.shields.io/badge/XGBoost-189AB4) | Gradient boosting classifier |
| ![NLTK](https://img.shields.io/badge/NLTK-8b5cf6) | NLP preprocessing |
| ![Plotly](https://img.shields.io/badge/Plotly-3D4DB7?logo=plotly&logoColor=white) | Interactive visualizations |
| ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) | Data manipulation |
| ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white) | Numerical computation |

</div>

---

## 📊 Dataset

**SMS Spam Collection Dataset** — UCI Machine Learning Repository

- **5,574** labeled messages (747 spam · 4,827 ham)
- Binary labels: `spam` / `ham`
- Source: [Kaggle — SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

```
spam    747   ████░░░░░░░░░░░░░░░░░  13.4%
ham    4827   ████████████████████░  86.6%
```

---

## 🌟 Roadmap

- [x] Ensemble ML model (Stacking Classifier)
- [x] Interactive Streamlit dashboard
- [x] Real-time confidence scoring
- [x] Suspicious keyword analysis
- [x] Word frequency visualization
- [ ] Gmail API integration for live inbox monitoring
- [ ] BERT / transformer fine-tuning
- [ ] Phishing URL detection module
- [ ] Explainable AI with SHAP values
- [ ] Docker containerization
- [ ] REST API endpoint (FastAPI)
- [ ] Multi-language spam detection
- [ ] AWS / GCP cloud deployment

---

## 👨‍💻 Author

<div align="center">

**Sahil Gaund**

[![GitHub](https://img.shields.io/badge/GitHub-@sahil--gaund03-181717?style=for-the-badge&logo=github)](https://github.com/sahil-gaund03)

*If this project helped you, please consider giving it a ⭐ — it really helps!*

</div>

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<sub>Built with ❤️ using Machine Learning · NLP · Ensemble Learning · Streamlit</sub>

</div>
