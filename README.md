# 🛡️ Phishing Website Detection System

A machine learning-based web application that detects whether a website is **Phishing** or **Legitimate** using URL and domain-related features. The app is built using **Streamlit** and deployed online.

---

## 🚀 Live Demo

👉 https://phishing-website-detection-by-janhavi-szcffkiplrusqqcpguewfg.streamlit.app/

---

## 📌 Project Overview

Phishing attacks are one of the most common cybersecurity threats.  
This project helps users identify fake websites using a trained machine learning model.

The application takes website-related feature inputs and predicts whether the website is:
- ✅ Legitimate  
- 🚨 Phishing  

---

## ✨ Features

- 🔍 Real-time prediction using ML model  
- 📊 Clean and user-friendly UI  
- 📁 Multipage Streamlit app (Home, Prediction, About)  
- ⚡ Fast and simple interaction  
- 🛡️ Helps improve cybersecurity awareness  

---

## 🧠 Machine Learning Details

- Algorithm Used: Random Forest Classifier  
- Target Variable: `Phishing / Legitimate`  
- Feature Values: -1, 0, 1 (based on website properties)  

---

## 📂 Project Structure
phishing-website-detection/
│
├── app.py
├── requirements.txt
├── phishing_model.pkl
├── scaler.pkl
├── Phishing_Legitimate_full.csv
└── pages/
├── 1_Prediction.py
└── 2_About.py


---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- Joblib  

---

## ▶️ How to Run Locally

1. Clone the repository

```bash
git clone https://github.com/janhavisawant03/phishing-website-detection

2. Navigate to the project folder
cd phishing-website-detection

3. Install dependencies
pip install -r requirements.txt

4. Run the app
streamlit run app.py

📊 Dataset

The dataset contains website features such as:

URL structure
Domain properties
Security indicators
Traffic and behavior features

These features are used to train the machine learning model.

🎯 Use Cases
Cybersecurity awareness
Educational projects
ML model deployment practice
Real-world phishing detection demo

💡 Future Improvements
Auto URL input instead of manual feature entry
Better UI with graphs and insights
Model accuracy improvement
API integration

🙋‍♀️ Author

Janhavi Sawant
Aspiring Data Analyst | BSc Computer Science

⭐ Support

If you like this project, give it a ⭐ on GitHub!


---

## 🔥 IMPORTANT (Do this now)

```markdown
👉 https://phishing-website-detection-by-janhavi-szcffkiplrusqqcpguewfg.streamlit.app/
