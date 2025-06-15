

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("rf_model.pkl")  # Make sure this matches your actual model path

# App title
st.title("Bank Term Deposit Prediction App")

# User input fields
st.header("Client Information")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
job = st.selectbox("Job", [
    'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
    'retired', 'self-employed', 'services', 'student', 'technician',
    'unemployed', 'unknown'
])
marital = st.selectbox("Marital Status", ['married', 'single', 'divorced'])
education = st.selectbox("Education", ['primary', 'secondary', 'tertiary', 'unknown'])
default = st.selectbox("Has credit in default?", ['yes', 'no'])
balance = st.number_input("Account Balance", value=0)
housing = st.selectbox("Has housing loan?", ['yes', 'no'])
loan = st.selectbox("Has personal loan?", ['yes', 'no'])
contact = st.selectbox("Contact Communication Type", ['cellular', 'telephone'])
month = st.selectbox("Last Contact Month", [
    'jan', 'feb', 'mar', 'apr', 'may', 'jun', 
    'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
])
day = st.number_input("Day of Month Contacted", min_value=1, max_value=31, value=15)
campaign = st.number_input("Number of Contacts During Campaign", min_value=1, value=1)
previous = st.number_input("Number of Contacts Before Campaign", min_value=0, value=0)
poutcome = st.selectbox("Outcome of Previous Campaign", ['failure', 'success', 'other', 'unknown'])

# Create input DataFrame
input_data = pd.DataFrame({
    'age': [age],
    'job': [job],
    'marital': [marital],
    'education': [education],
    'default': [default],
    'balance': [balance],
    'housing': [housing],
    'loan': [loan],
    'contact': [contact],
    'month': [month],
    'day': [day],
    'campaign': [campaign],
    'previous': [previous],
    'poutcome': [poutcome]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "Yes" if prediction[0] == 1 else "No"
    st.success(f"Will the client subscribe to a term deposit? {result}")

