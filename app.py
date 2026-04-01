import streamlit as st

st.set_page_config(
    page_title="Phishing Website Detection",
    page_icon="🛡️",
    layout="wide"
)

# sidebar
with st.sidebar:
    st.markdown("## 🛡️ Phishing Detector")
    st.markdown("---")
    st.info("Use the top sidebar menu to move between pages.")
    st.success("Home Page Loaded")
    st.info("Use the sidebar to move between pages.")
    st.success("ML Based Security App")

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 30px;
}
.hero-box {
    background: linear-gradient(135deg, #0f172a, #1e293b, #1d4ed8);
    padding: 35px;
    border-radius: 24px;
    color: white;
    box-shadow: 0 6px 24px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}
.card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 24px;
    border-radius: 20px;
    color: white;
    box-shadow: 0 4px 18px rgba(0,0,0,0.22);
    min-height: 180px;
}
.section-title {
    font-size: 28px;
    font-weight: 700;
    color: white;
    margin-top: 10px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🛡️ Phishing Website Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">A smart machine learning web app to identify phishing and legitimate websites</div>', unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <h2>Stay Safe from Fake Websites</h2>
    <p style="font-size:18px;">
        This application predicts whether a website is <b>Phishing</b> or <b>Legitimate</b>
        using a trained machine learning model. It helps users understand website risk
        using important URL and domain related features.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">✨ Main Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🔍 Prediction</h3>
        <p>Enter website feature values and get instant prediction using the trained model.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📊 Project Info</h3>
        <p>Understand the dataset, features, model purpose, and how the phishing detection system works.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>⚡ Easy Interface</h3>
        <p>Clean design, multipage structure, and simple navigation from the sidebar.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col4, col5 = st.columns(2)

with col4:
    st.info("📌 Open the Prediction page from the sidebar to test the model.")

with col5:
    st.success("✅ Open the About page to see project and dataset details.")

st.write("")
st.markdown("### 🚀 Workflow")
st.write("1. Go to Prediction page")
st.write("2. Enter all feature values")
st.write("3. Click Predict Website")
st.write("4. Check the result")