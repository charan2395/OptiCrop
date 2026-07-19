import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(
    page_title="OptiCrop",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 OptiCrop")
st.subheader("Smart Agricultural Production Optimization Engine")

st.write("Enter the soil and environmental details.")

N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorous (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Level")
rainfall = st.number_input("Rainfall (mm)")

if st.button("Predict Crop"):

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Recommended Crop: **{prediction[0]}**")
