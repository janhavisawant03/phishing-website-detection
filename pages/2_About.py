import streamlit as st
import pandas as pd

st.set_page_config(page_title="About Project", page_icon="📊", layout="wide")

# sidebar
with st.sidebar:
    st.markdown("## 🛡️ Phishing Detector")
    st.markdown("---")
    st.info("Use the top sidebar menu to move between pages.")
    st.success("About Page Loaded")
    st.info("This page shows project and dataset details.")
    st.success("Project Info Loaded")

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 28px;
}
.info-box {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 22px;
    border-radius: 18px;
    color: white;
    box-shadow: 0 4px 18px rgba(0,0,0,0.22);
    margin-bottom: 20px;
}
.small-box {
    background: #1e293b;
    padding: 18px;
    border-radius: 16px;
    color: white;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📊 About This Project</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Know the objective, dataset, model, and feature details of this phishing detection system</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h3>🎯 Project Objective</h3>
    <p>
        The main goal of this project is to detect whether a website is phishing or legitimate
        by using machine learning. This system helps users avoid fake websites and improves online safety.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h3>🧠 Model Information</h3>
    <p>
        This application uses a trained machine learning model and a scaler for preprocessing.
        The model checks website-related features and gives the final prediction.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
    <h3>📁 Dataset Information</h3>
    <p>
        The dataset contains multiple website and URL-related features used to identify
        whether a website is legitimate or phishing.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="small-box">
        <h3>✅ Legitimate Website</h3>
        <p>A normal and safe website with trusted behavior.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="small-box">
        <h3>⚠️ Phishing Website</h3>
        <p>A fake or suspicious website made to trick users and steal information.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

try:
    df = pd.read_csv("Phishing_Legitimate_full.csv")

    st.markdown("### 📌 Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Rows", df.shape[0])
    with c2:
        st.metric("Columns", df.shape[1])
    with c3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    st.markdown("### 🏷️ Column Names")
    st.write(list(df.columns))

except Exception:
    st.warning("Dataset file not found. Keep Phishing_Legitimate_full.csv in the main project folder.")

st.info("Use the Prediction page from the sidebar to test the model.")