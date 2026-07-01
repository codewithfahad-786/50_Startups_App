import streamlit as st
import joblib
import numpy as np

model = joblib.load("multiple_linear_regression_model.pkl")

st.title("📊 Multiple Linear Regression App")

st.write("Enter values to predict Profit")

# Inputs
rd_spend = st.number_input("R&D Spend")
admin = st.number_input("Administration")
marketing = st.number_input("Marketing Spend")

state = st.selectbox("State", ["New York", "California", "Florida"])

# Convert State (example encoding)
state_map = {
    "New York": 0,
    "California": 1,
    "Florida": 2
}

state_val = state_map[state]

# Predict
if st.button("Predict Profit"):
    input_data = np.array([[rd_spend, admin, marketing, state_val]])
    prediction = model.predict(input_data)

    st.success(f"Predicted Profit: {prediction[0]:.2f}")