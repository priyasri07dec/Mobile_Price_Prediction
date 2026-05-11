import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config()
st.markdown(
    """
    <style>
    .stApp {
        background-color: #D3D3D3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
   """<style>
   label{"
   color: white !important; 
   font-size: 24px !important; 
   font-weight: bold !important; 
   text-align: center; 
   margin-bottom: 20px;
   "}
   </style>""",
   unsafe_allow_html=True)

# Load the trained model and scaler
model = joblib.load("mobile_price_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")

# App Title
st.title("Mobile Price Prediction")

st.write("Enter the specifications of the mobile phone to predict its price")

# Input fields for user to enter mobile specifications
col1, col2 = st.columns([1,1], gap="large")
with col1:
 Sale = st.number_input("Sale", min_value=0)
 weight = st.number_input("Weight (g)", min_value=0)
 resolution = st.number_input("Resolution", min_value=0)
 ppi = st.number_input("PPI", min_value=0)
 cpu_core = st.number_input("CPU Cores", min_value=0)
 cpu_freq = st.number_input("CPU Frequency (GHz)", min_value=0.0, step=0.1)
with col2:
 internal_mem = st.number_input("Internal Memory (GB)", min_value=0)
 ram = st.number_input("RAM (GB)", min_value=0)
 RearCam = st.number_input("Rear Camera (MP)", min_value=0)
 Front_Cam = st.number_input("Front Camera (MP)", min_value=0)
 battery = st.number_input("Battery Capacity (mAh)", min_value=0)
 thickness = st.number_input("Thickness (mm)", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict Price", key="predict_button"):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        'Sale': [Sale],
        'weight': [weight],
        'resolution': [resolution],
        'ppi': [ppi],
        'cpu_core': [cpu_core],
        'cpu_freq': [cpu_freq],
        'internal_mem': [internal_mem],
        'ram': [ram],
        'RearCam': [RearCam],
        'Front_Cam': [Front_Cam],
        'battery': [battery],
        'thickness': [thickness]
    })

    # Apply same log transformation and scaling as during training

    skewed_cols = [
    "Sale",
    "weight",
    "resolution",
    "internal_mem",
    "Front_Cam",
    "battery",
    "thickness"
]
    
    for col in skewed_cols:
        input_data[col] = np.log1p(input_data[col])

    # Feature scaling
    scaled_data = scaler.transform(input_data)

    # Predict the price using the loaded model
    predicted_price = model.predict(scaled_data)
    
    #Display the predicted price
    st.success(f"Predicted Mobile Price: ₹ {predicted_price[0]:,.2f}")
