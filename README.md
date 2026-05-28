# Customer Churn Prediction App

This project is an end-to-end Machine Learning web application that predicts customer churn using a Decision Tree classifier with SMOTEENN imbalance handling.

## Features

* Customer churn prediction
* Streamlit interactive web app
* Machine Learning pipeline
* Automatic preprocessing with OneHotEncoder
* Imbalanced data handling using SMOTEENN
* Model serialization using Joblib

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* Streamlit
* Joblib

---

## Project Structure

```bash
customer-churn-app/
│
├── app.py
├── ChurnPrediction.joblib
├── requirements.txt
├── README.md
└── notebook.ipynb
```

---

## Dataset

The project uses the Telco Customer Churn dataset.

Target variable:

* Churn

  * Yes = customer leaves
  * No = customer stays

---

## Machine Learning Workflow

1. Data Cleaning
2. Feature Engineering
3. Train/Test Split
4. Preprocessing Pipeline
5. OneHotEncoding
6. SMOTEENN Resampling
7. Decision Tree Training
8. Model Evaluation
9. Streamlit Deployment

---

## Model Performance

Example classification report:

  precision    recall  f1-score   support

     0.83      0.91      0.87      1033
     0.65      0.48      0.55       374

---

## Installation

Clone repository:

```bash
git clone https://github.com/brahimazreg/customer_churn_app.git

cd customer-churn-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

## Future Improvements

* Random Forest / XGBoost models
* SHAP explainability
* Cloud deployment
* User authentication
* Dashboard analytics

---

## Author

Brahim Azreg
