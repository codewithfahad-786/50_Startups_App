import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("multiple_linear_regression_model.pkl")

# Title
st.title("📊 Startup Profit Prediction App")

st.write("Enter company investment details to predict profit")

# Inputs (FIXED 0.00 issue)
rd = st.number_input("R&D Spend", min_value=0.0, step=1000.0, format="%.2f")
admin = st.number_input("Administration", min_value=0.0, step=1000.0, format="%.2f")
marketing = st.number_input("Marketing Spend", min_value=0.0, step=1000.0, format="%.2f")

# State selection
state = st.selectbox("State", ["California", "Florida", "New York"])

# One-hot encoding (same as training: drop_first=True)
state_florida = 1 if state == "Florida" else 0
state_ny = 1 if state == "New York" else 0

# Predict button
if st.button("Predict Profit"):
    input_data = np.array([[rd, admin, marketing, state_florida, state_ny]])
    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Profit: {prediction[0]:.2f}")