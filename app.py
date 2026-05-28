import streamlit as st
import pandas as pd
import joblib

model = joblib.load("ChurnPrediction.joblib")

st.title("Customer Churn Prediction")

# Inputs (raw values only)
gender = st.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.selectbox("Senior Citizen", ["Yes", "No"])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No"])

InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"])
DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"])
TechSupport = st.selectbox("Tech Support", ["Yes", "No"])

StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"])
StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"])

Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

MonthlyCharges = st.number_input("Monthly Charges", 0.0)
TotalCharges = st.number_input("Total Charges", 0.0)

tenure_group = st.selectbox(
    "Tenure Group",
    ["1-12", "13-24", "25-36", "37-48", "49-60", "61-72"]
)

# Convert SeniorCitizen
SeniorCitizen = 1 if SeniorCitizen == "Yes" else 0

# Build input dataframe (RAW format!)
input_data = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": SeniorCitizen,
    "Partner": Partner,
    "Dependents": Dependents,
    "PhoneService": PhoneService,
    "MultipleLines": MultipleLines,
    "InternetService": InternetService,
    "OnlineSecurity": OnlineSecurity,
    "OnlineBackup": OnlineBackup,
    "DeviceProtection": DeviceProtection,
    "TechSupport": TechSupport,
    "StreamingTV": StreamingTV,
    "StreamingMovies": StreamingMovies,
    "Contract": Contract,
    "PaperlessBilling": PaperlessBilling,
    "PaymentMethod": PaymentMethod,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "tenure_group": tenure_group
}])

if st.button("Predict"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    if prediction[0] == 1:
        st.error(f"Customer likely to CHURN ({probability:.2f}%)")
    else:
        st.success(f"Customer likely to STAY ({100 - probability:.2f}%)")