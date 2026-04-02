import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediction", page_icon="🔍", layout="wide")

# sidebar
with st.sidebar:
    st.markdown("## 🛡️ Phishing Detector")
    st.markdown("---")
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
    '<div class="sub-title">Enter values for all website features and predict whether the website is legitimate or phishing</div>',
    unsafe_allow_html=True
)

# features that really use -1, 0, 1
ternary_features = [
    "SubdomainLevelRT",
    "UrlLengthRT",
    "PctExtResourceUrlsRT",
    "AbnormalExtFormActionR",
    "ExtMetaScriptLinkRT",
    "PctExtNullSelfRedirectHyperlinksRT",
]

# features that use only 0 and 1
binary_features = [
    "AtSymbol",
    "TildeSymbol",
    "NoHttps",
    "RandomString",
    "IpAddress",
    "DomainInSubdomains",
    "DomainInPaths",
    "HttpsInHostname",
    "DoubleSlashInPath",
    "EmbeddedBrandName",
    "ExtFavicon",
    "InsecureForms",
    "RelativeFormAction",
    "ExtFormAction",
    "AbnormalFormAction",
    "FrequentDomainNameMismatch",
    "FakeLinkInStatusBar",
    "RightClickDisabled",
    "PopUpWindow",
    "SubmitInfoToEmail",
    "IframeOrFrame",
    "MissingTitle",
    "ImagesOnlyInForm",
]

# numeric features that should not be forced to -1,0,1
numeric_features = [f for f in feature_names if f not in ternary_features + binary_features]

# safe numeric ranges based on the dataset used for training
numeric_ranges = {
    "NumDots": (0, 20),
    "SubdomainLevel": (0, 10),
    "PathLevel": (0, 20),
    "UrlLength": (0, 300),
    "NumDash": (0, 20),
    "NumDashInHostname": (0, 10),
    "NumUnderscore": (0, 20),
    "NumPercent": (0, 20),
    "NumQueryComponents": (0, 20),
    "NumAmpersand": (0, 20),
    "NumHash": (0, 10),
    "NumNumericChars": (0, 100),
    "HostnameLength": (0, 120),
    "PathLength": (0, 250),
    "QueryLength": (0, 200),
    "NumSensitiveWords": (0, 10),
    "PctExtHyperlinks": (0.0, 1.0),
    "PctExtResourceUrls": (0.0, 1.0),
    "PctNullSelfRedirectHyperlinks": (0.0, 1.0),
}

feature_help = {
    "AtSymbol": "0 = no @ symbol, 1 = @ symbol present",
    "TildeSymbol": "0 = no ~ symbol, 1 = ~ symbol present",
    "NoHttps": "0 = HTTPS used, 1 = HTTPS not used",
    "RandomString": "0 = no random string, 1 = random string present",
    "IpAddress": "0 = domain name used, 1 = IP address used",
    "DoubleSlashInPath": "0 = normal path, 1 = double slash found in path",
    "PopUpWindow": "0 = no popup, 1 = popup present",
    "RightClickDisabled": "0 = right click allowed, 1 = disabled",
    "SubmitInfoToEmail": "0 = no email submit, 1 = submits info to email",
    "IframeOrFrame": "0 = no iframe/frame, 1 = iframe/frame present",
    "MissingTitle": "0 = title present, 1 = title missing",
    "ImagesOnlyInForm": "0 = normal form, 1 = images only in form",
    "SubdomainLevelRT": "-1 = suspicious, 0 = uncertain, 1 = safe",
    "UrlLengthRT": "-1 = suspicious, 0 = uncertain, 1 = safe",
    "PctExtResourceUrlsRT": "-1 = suspicious, 0 = uncertain, 1 = safe",
    "AbnormalExtFormActionR": "-1 = suspicious, 0 = uncertain, 1 = safe",
    "ExtMetaScriptLinkRT": "-1 = suspicious, 0 = uncertain, 1 = safe",
    "PctExtNullSelfRedirectHyperlinksRT": "-1 = suspicious, 0 = uncertain, 1 = safe",
}

st.markdown(f"""
<div class="card">
    <h3>Model Input</h3>
    <p>This model expects <b>{len(feature_names)} features</b>.</p>
    <p><b>Important:</b> only some features use <b>-1, 0, 1</b>. Many features are counts, lengths, or percentages and must be entered as numeric values.</p>
</div>
""", unsafe_allow_html=True)

# reset
if st.button("Reset All Values"):
    for f in feature_names:
        if f in ternary_features:
            st.session_state[f] = 0
        elif f in binary_features:
            st.session_state[f] = 0
        else:
            st.session_state[f] = 0.0

sections = [
    ("🔢 Numeric Count / Length Features", numeric_features),
    ("⚪ Binary Features (0 or 1)", binary_features),
    ("🟡 Ternary Risk Features (-1, 0, 1)", ternary_features),
]

input_data = {}

for section_name, features in sections:
    if features:
        with st.expander(section_name, expanded=(section_name == "🔢 Numeric Count / Length Features")):
            cols = st.columns(3)

            for i, feature in enumerate(features):
                with cols[i % 3]:
                    if feature in numeric_features:
                        min_val, max_val = numeric_ranges.get(feature, (0.0, 100.0))

                        if feature in ["PctExtHyperlinks", "PctExtResourceUrls", "PctNullSelfRedirectHyperlinks"]:
                            value = st.number_input(
                                feature,
                                min_value=float(min_val),
                                max_value=float(max_val),
                                value=float(st.session_state.get(feature, 0.0)),
                                step=0.01,
                                help=feature_help.get(feature, "Enter a numeric value"),
                                key=feature
                            )
                        else:
                            value = st.number_input(
                                feature,
                                min_value=float(min_val),
                                max_value=float(max_val),
                                value=float(st.session_state.get(feature, 0.0)),
                                step=1.0,
                                help=feature_help.get(feature, "Enter a numeric value"),
                                key=feature
                            )
                        input_data[feature] = value

                    elif feature in binary_features:
                        value = st.selectbox(
                            feature,
                            options=[0, 1],
                            index=0 if st.session_state.get(feature, 0) == 0 else 1,
                            help=feature_help.get(feature, "Select 0 or 1"),
                            key=feature
                        )
                        input_data[feature] = value

                    elif feature in ternary_features:
                        current = st.session_state.get(feature, 0)
                        if current not in [-1, 0, 1]:
                            current = 0
                        value = st.selectbox(
                        feature,
                        options=[-1, 0, 1],
                        key=feature
                        )
                        input_data[feature] = value

st.markdown(
    '<p class="small-note">Tip: numeric features are counts, lengths, and percentages. Binary features are 0/1. Only the RT features use -1, 0, 1.</p>',
    unsafe_allow_html=True
)

if st.button("🚀 Predict Website", use_container_width=True):
    df_input = pd.DataFrame([input_data])

    # exact column order
    df_input = df_input.reindex(columns=feature_names)

    scaled_features = scaler.transform(df_input)
    prediction = model.predict(scaled_features)[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(scaled_features)[0]
        confidence = float(max(probability) * 100)

    st.write("### Prediction Result")

    # your saved model predicts:
    # 1 = Legitimate
    # 0 = Phishing
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

    st.write("### Model Output")
    st.write(f"Raw class returned by model: {prediction}")

    st.write("### Input Summary")
    st.dataframe(df_input, use_container_width=True)
