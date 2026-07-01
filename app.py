import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("multiple_linear_regression_model.pkl")

# Title
st.title("📊 Multiple Linear Regression App")

st.write("Enter values to predict Profit")

# Input fields
rd_spend = st.number_input("R&D Spend")
admin = st.number_input("Administration")
marketing = st.number_input("Marketing Spend")

# Predict button
if st.button("Predict Profit"):
    input_data = np.array([[rd_spend, admin, marketing]])
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Profit: {prediction[0]:.2f}")
