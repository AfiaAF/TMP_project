

import streamlit as st
import joblib
import pandas as pd

## Loading model
model = joblib.load("sub_pred_model.pkl")


## App title
st.title("📊 Bank Deposit Subscription Predictor")

## User inputs
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", ['admin.', 'technician', 'services', 'management', 'retired',
                           'blue-collar', 'unemployed', 'entrepreneur', 'housemaid',
                           'self-employed', 'student', 'unknown'])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Has Credit Default?", ['yes', 'no'])
balance = st.number_input("Account Balance", step=100)
housing = st.selectbox("Has Housing Loan?", ['yes', 'no'])
loan = st.selectbox("Has Personal Loan?", ['yes', 'no'])
contact = st.selectbox("Contact Communication Type", ['cellular', 'telephone', 'unknown'])
month = st.selectbox("Last Contact Month", ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
                                            'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
campaign = st.number_input("Number of Contacts During Campaign", min_value=1, max_value=50, value=1)
previous = st.number_input("Number of Previous Contacts", min_value=0, max_value=100, value=0)
poutcome = st.selectbox("Previous Outcome", ['success', 'failure', 'nonexistent'])

## Feature engineering
age_group = (
    "young" if age < 30 else
    "adult" if age < 60 else
    "senior"
)
balance_level = (
    "low" if balance < 0 else
    "medium" if balance < 1000 else
    "high"
)
campaign_efficiency = previous / campaign if campaign else 0

##  Input assembly
input_dictionary = {
    "age": age,
    "job": job,
    "marital": marital,
    "education": education,
    "default": default,
    "balance": balance,
    "housing": housing,
    "loan": loan,
    "contact": contact,
    "month": month,
    "campaign": campaign,
    "previous": previous,
    "previous_outcome": poutcome,
    "age_group": age_group,
    "balance_level": balance_level,
    "campaign_efficiency": campaign_efficiency
}

## Converting to DataFrame
input_frame = pd.DataFrame([input_dictionary])


## Prediction
if st.button("Predict"):
    try:
        prediction = model.predict(input_frame)
        result = "✅ Yes" if prediction[0] == 1 else "❌ No"
        st.success(f"Will the client subscribe? {result}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

