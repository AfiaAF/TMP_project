

import streamlit as st
import joblib

# Loading model
model = joblib.load("sub_pred_model.pkl")

# App title
st.title("Bank Term Deposit Subscription Predictor")

# User inputs
age = st.slider("Age", 18, 95, 30)
job = st.selectbox("Job", ['admin.', 'technician', 'services', 'management', 'retired', 'blue-collar', 'unemployed', 'entrepreneur', 'housemaid', 'self-employed', 'student', 'unknown'])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Has Credit Default?", ['yes', 'no'])
housing = st.selectbox("Has Housing Loan?", ['yes', 'no'])
loan = st.selectbox("Has Personal Loan?", ['yes', 'no'])

# Assembling input for model
input_dictionary = {
    "age": age,
    "job": job,
    "marital": marital,
    "education": education,
    "default": default,
    "housing": housing,
    "loan": loan
}

input_bankdata = pd.DataFrame([input_dictionary])

# Encoding and prediction

if st.button("Predict"):
    prediction = model.predict(input_bankdata)
    result = "Yes" if prediction[0] == 1 else "No"
    st.success(f"Will the client subscribe? {result}")
