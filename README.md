<div align="center">

<img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>

# 🛡️ AI-Powered Spam & Fraud Detection System

**An advanced Machine Learning + NLP system that detects whether an Email or SMS is Spam or Ham — powered by Ensemble Learning, XGBoost, TF-IDF Vectorization, and a real-time Streamlit dashboard.**

[⭐ Star this repo](https://github.com/sahil-gaund03/AI-Spam-Detection-System) &nbsp;·&nbsp; [🐛 Report Bug](https://github.com/sahil-gaund03/AI-Spam-Detection-System/issues) &nbsp;·&nbsp; [📦 Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

</div>

---
<h3> Live demo : https://ai-spam-detection-system0310.streamlit.app/</h3>
## 📊 Model Performance

| Metric | Score |
|--------|-------|
| ✅ Accuracy | 97% – 99% |
| 🎯 Precision | 96% – 99% |
| 🔍 Recall | 95% – 99% |
| ⚡ F1 Score | 96% – 99% |

---

## 🚀 Live Features

- ✅ Advanced NLP Text Cleaning
- ✅ TF-IDF Feature Engineering
- ✅ Ensemble Machine Learning
- ✅ Stacking Classifier
- ✅ Spam Keyword Detection
- ✅ AI Confidence Score
- ✅ Real-Time Prediction
- ✅ Interactive Streamlit Dashboard
- ✅ Fraud & Security Insights
- ✅ Downloadable Analysis Report

---

## 🧠 ML Pipeline

```
Dataset
   ↓
Text Cleaning
   ↓
NLP Preprocessing (NLTK)
   ↓
TF-IDF Vectorization
   ↓
Ensemble Learning Models
   ↓
Stacking Classifier (Meta-Learner)
   ↓
Prediction + Confidence Score
```

---

## 🔥 Algorithms Used

| Algorithm | Role |
|-----------|------|
| Multinomial Naive Bayes | Base classifier |
| Logistic Regression | Base classifier |
| Linear SVM | Base classifier |
| XGBoost | Base classifier |
| Stacking Ensemble Classifier | Meta-learner (final prediction) |

---

## 📂 Project Structure

```bash
AI-Spam-Detection-System/
│
├── app.py                    # Streamlit web app
├── train_model.py            # Model training script
├── best_spam_model.pkl       # Saved trained model
├── spam.csv                  # SMS Spam Collection dataset
├── requirements.txt          # Python dependencies
├── README.md
│
└── notebooks/
    └── spam_detection.ipynb  # EDA + model exploration
```

---

## 🧪 Example Predictions

| Message | Prediction |
|---------|-----------|
| Congratulations! You won a free iPhone | ❌ Spam |
| Hey, are we meeting tomorrow? | ✅ Ham |
| Claim your reward now — limited time offer! | ❌ Spam |
| Please send the report by evening | ✅ Ham |
| URGENT: Verify your account or it will be suspended | ❌ Spam |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sahil-gaund03/AI-Spam-Detection-System.git
cd AI-Spam-Detection-System
```

### 2. Create & activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train_model.py
```

This generates `best_spam_model.pkl` in the project root.

### 5. Launch the Streamlit app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
nltk
xgboost
plotly
```

---

## 🧰 Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Core backend |
| Streamlit | Interactive web app |
| Scikit-learn | ML model pipeline |
| XGBoost | Gradient boosting model |
| NLTK | NLP text preprocessing |
| Plotly | Interactive visualizations |
| Pandas | Data manipulation |
| NumPy | Numerical computation |

---

## 📊 Dataset

**SMS Spam Collection Dataset** (UCI Machine Learning Repository)

- 5,574 messages labeled as Spam or Ham
- Available on Kaggle: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

---

## 🛡️ AI Security Features

- Fraud pattern detection
- Suspicious keyword analysis
- Spam probability scoring
- AI confidence gauge
- Real-time message classification

---

## 📸 Streamlit Dashboard Features

- Modern dark UI with glassmorphism design
- Interactive analytics charts
- AI prediction result card
- Confidence gauge visualization
- Downloadable analysis reports
- Security insights panel

---

## 🌟 Future Roadmap

- [ ] Gmail API integration for live email monitoring
- [ ] Deep learning with BERT transformer
- [ ] Phishing URL detection
- [ ] Explainable AI with SHAP
- [ ] Docker containerization
- [ ] AWS cloud deployment
- [ ] Multi-language spam detection
- [ ] Real-time SMS monitoring

---

## 👨‍💻 Author

**Sahil Gaund**

- GitHub: [@sahil-gaund03](https://github.com/sahil-gaund03)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

If you found this project useful, please consider giving it a ⭐ on GitHub!

</div>
