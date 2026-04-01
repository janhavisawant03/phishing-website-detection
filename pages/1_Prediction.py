import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediction", page_icon="🔍", layout="wide")

# sidebar
with st.sidebar:
    st.markdown("## 🛡️ Phishing Detector")
    st.markdown("---")
    st.info("Use the top sidebar menu to move between pages.")
    st.success("Prediction Page Loaded")

# load model and scaler
model = joblib.load("phishing_model.pkl")
scaler = joblib.load("scaler.pkl")

# exact feature names used during training
feature_names = list(scaler.feature_names_in_)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}
.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 25px;
}
.card {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 18px;
    color: white;
    box-shadow: 0 4px 18px rgba(0,0,0,0.25);
    margin-bottom: 20px;
}
.result-good {
    background: #052e16;
    padding: 18px;
    border-radius: 16px;
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
}
.result-bad {
    background: #450a0a;
    padding: 18px;
    border-radius: 16px;
    color: white;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
}
.small-note {
    color: #cbd5e1;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🔍 Website Phishing Prediction</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Select feature values in grouped sections and predict whether the website is legitimate or phishing</div>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="card">
    <h3>Model Input</h3>
    <p>This model expects <b>{len(feature_names)} features</b>.</p>
    <p>All fields use dropdown values: <b>-1, 0, 1</b>.</p>
</div>
""", unsafe_allow_html=True)

choices = {
    -1: "Suspicious (-1)",
    0: "Neutral (0)",
    1: "Legitimate (1)"
}

# reset
if st.button("Reset All Values to 0"):
    for f in feature_names:
        st.session_state[f] = 0

# simple grouping by feature names
url_keywords = ["url", "path", "query", "domain", "hostname", "subdomain", "tld", "slash", "https", "ip", "atsymbol"]
count_keywords = ["num", "pct", "percent", "ampersand", "dash", "dot", "hash", "underscore"]
security_keywords = ["secure", "https", "insecure", "favicon", "form", "submit", "iframe", "popup", "window", "mailto"]
brand_keywords = ["brand", "phish", "suspicious", "fake", "redirect", "external", "ext", "hyperlink", "resource"]

group_1 = []
group_2 = []
group_3 = []
group_4 = []

for feature in feature_names:
    f = feature.lower()

    if any(k in f for k in url_keywords):
        group_1.append(feature)
    elif any(k in f for k in count_keywords):
        group_2.append(feature)
    elif any(k in f for k in security_keywords):
        group_3.append(feature)
    elif any(k in f for k in brand_keywords):
        group_4.append(feature)
    else:
        group_4.append(feature)

sections = [
    ("🌐 URL / Domain Features", group_1),
    ("🔢 Count / Structure Features", group_2),
    ("🔐 Security / Form Features", group_3),
    ("📎 External / Other Features", group_4),
]

input_data = {}

for section_name, features in sections:
    if features:
        with st.expander(section_name, expanded=False):
            cols = st.columns(3)

            for i, feature in enumerate(features):
                with cols[i % 3]:
                    default_value = st.session_state.get(feature, 0)
                    selected = st.selectbox(
                        feature,
                        options=[-1, 0, 1],
                        index=[-1, 0, 1].index(default_value if default_value in [-1, 0, 1] else 0),
                        format_func=lambda x: choices[x],
                        key=feature
                    )
                    input_data[feature] = selected

st.markdown('<p class="small-note">Open each section and select values for all features before prediction.</p>', unsafe_allow_html=True)

if st.button("🚀 Predict Website", use_container_width=True):
    df_input = pd.DataFrame([input_data])

    # make sure all expected columns exist in exact order
    df_input = df_input.reindex(columns=feature_names)

    scaled_features = scaler.transform(df_input)
    prediction = model.predict(scaled_features)[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(scaled_features)[0]
        confidence = float(max(probability) * 100)

    st.write("### Prediction Result")

    if prediction == 1:
        st.markdown(
            '<div class="result-good">✅ Legitimate Website</div>',
            unsafe_allow_html=True
        )
        st.balloons()
    else:
        st.markdown(
            '<div class="result-bad">⚠️ Phishing Website</div>',
            unsafe_allow_html=True
        )

    if confidence is not None:
        st.metric("Confidence", f"{confidence:.2f}%")

    st.write("### Input Summary")
    st.dataframe(df_input, use_container_width=True)