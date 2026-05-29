import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ChurnPrediction.joblib")

# Page config
st.set_page_config(
    page_title="Customer Churn Prediction",
    #page_icon="📊",
    layout="centered"
)

col1, col2 = st.columns([1, 5])
with col1:
    st.image("customer-churn-image.webp", width=90)

with col2:
    st.markdown(
        """
        <h1 style='padding-top:0px;'>
            Customer Churn Prediction
        </h1>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown("""
### Enter Customer Information
Fill in the customer details below to predict churn probability.
""")

# -------------------------
# CUSTOMER INPUTS
# -------------------------

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", ["Yes", "No"])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])

    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No"])

    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No"])

    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No"])

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)

tenure_group = st.selectbox(
    "Tenure Group",
    ["1-12", "13-24", "25-36", "37-48", "49-60", "61-72"]
)



# -------------------------
# BUILD INPUT DATAFRAME
# -------------------------

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

# -------------------------
# PREDICTION
# -------------------------

if st.button("Predict Churn"):

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] * 100

    st.markdown("---")
    st.markdown("## Prediction Result")

    if prediction[0] == 1:
        st.error(
            f"⚠️ Customer likely to CHURN ({probability:.2f}%)"
        )
    else:
        st.success(
            f"✅ Customer likely to STAY ({100 - probability:.2f}%)"
        )