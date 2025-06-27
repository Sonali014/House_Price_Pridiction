
import streamlit as st
import joblib

# Load model
model = joblib.load("mental_health_model.pkl")

st.set_page_config(page_title="Mental Health Alert System")

st.title("🧠 Mental Health Risk Prediction")

# User Inputs
emotional = st.slider("How emotional are you?", 0.0, 1.0, 0.5)
worry = st.slider("Do you worry too much?", 0.0, 1.0, 0.5)
lost = st.slider("Do you feel lost in public?", 0.0, 1.0, 0.5)
overthinking = st.slider("How much do you overthink?", 0.0, 1.0, 0.5)
religion = st.slider("Are you religious?", 0.0, 1.0, 0.5)

if st.button("Predict Risk"):
    input_data = [[religion, emotional, worry, lost, overthinking]]
    pred = model.predict(input_data)[0]

    if pred == "High":
        st.error("🔴 ALERT! High Mental Health Risk")
    elif pred == "Medium":
        st.warning("🟠 Caution: Needs Monitoring")
    else:
        st.success("🟢 Stable: No Immediate Concern")
