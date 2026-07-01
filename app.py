import streamlit as st
import joblib
import numpy as np

model = joblib.load("multiple_linear_regression_model.pkl")

st.title("📊 Startup Profit Prediction App")

rd = st.number_input("R&D Spend")
admin = st.number_input("Administration")
marketing = st.number_input("Marketing Spend")

state = st.selectbox("State", ["California", "Florida", "New York"])

# One-hot encoding (same as training drop_first=True)
state_florida = 1 if state == "Florida" else 0
state_ny = 1 if state == "New York" else 0

if st.button("Predict Profit"):
    input_data = np.array([[rd, admin, marketing, state_florida, state_ny]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Profit: {prediction[0]:.2f}")