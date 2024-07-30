import pickle
import numpy as np
import pandas as pd
import streamlit as st


# Load the saved model
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
# Create a Streamlit app
st.title("Loan Prediction App")

# Create input fields for user data
st.subheader("Enter Your Details:")


gender = st.selectbox("Gender", [1, 0], help="1 for Male, 0 for Female")
married = st.selectbox("Married", [1, 0], help="1 for Yes, 0 for No")
dependents = st.selectbox("Dependents", [1, 0], help="1 for Yes, 0 for No")
education = st.selectbox("Education", [1, 0], help="1 for Graduate, 0 for Not Graduate")
self_employed = st.selectbox("Self Employed", [1, 0], help="1 for Yes, 0 for No")


applicant_income = st.number_input("Applicant Income", help="Monthly income of applicant")
coapplicant_income = st.number_input("Coapplicant Income", help="Monthly income of coapplicant")
loan_amount = st.number_input("Loan Amount", help="Amount of loan applied for")
loan_amount_term = st.number_input("Loan Amount Term", help="Term of loan in months")
credit_history = st.selectbox("Credit History", [1, 0], help="1 for Good credit history, 0 for Bad credit history")
property_area = st.selectbox("Property Area", [1, 2, 3], help="1 for Urban, 2 for Semiurban, 3 for Rural")

# Create a button to submit user data
if st.button("Get Prediction"):
    # Create a new DataFrame with user input
    new_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    # Get prediction from the loaded model
    predictions = loaded_model.predict(new_data)
    st.write('1 for applicable for LOAN')
    st.write('0 for not applicable for LOAN')

    # Display the prediction
    st.subheader("Prediction:")
    st.write(predictions)

#This updated app includes example input data below the input fields, which should help users understand what kind of data to enter.
