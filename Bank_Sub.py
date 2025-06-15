

import streamlit as st
import joblib
import pandas as pd
import numpy as np

## Loading model
model = joblib.load("sub_pred_model.pkl")

## App title
st.title("Bank Deposit Subscription Predictor")

if model is not None:
    ## User inputs
    age = st.slider("Age", 18, 95, 30)
    job = st.selectbox("Job", ['admin.', 'technician', 'services', 'management', 'retired', 'blue-collar', 
                               'unemployed', 'entrepreneur', 'housemaid', 'self-employed', 'student', 'unknown'])
    marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
    education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
    default = st.selectbox("Has Credit Default?", ['yes', 'no'])
    balance = st.number_input("Account Balance (€)", step=100)
    housing = st.selectbox("Has Housing Loan?", ['yes', 'no'])
    loan = st.selectbox("Has Personal Loan?", ['yes', 'no'])

    ## Assemble user input into DataFrame
    input_dictionary = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "balance": balance,
        "housing": housing,
        "loan": loan
    }

    input_frame = pd.DataFrame([input_dictionary])

    # Prediction
    if st.button("Predict"):
        try:
            prediction = model.predict(input_frame)
            result = "Yes!" if prediction[0] == 1 else "No"
            st.success(f"Will the client subscribe? **{result}**")
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")
