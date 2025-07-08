import pandas as pd
import streamlit as st
from data_frame_generator import generate_df
from joblib import load
import math

st.title("Insurance Premium Prediction")

# Dictionary to store user inputs
user_input = {}

# Options for dropdowns
gender_options = ["Male", "Female"]
region_options = ["Northwest", "Southeast", "Northeast", "Southwest"]
marital_status_options = ["Unmarried", "Married"]
bmi_options = ["Normal", "Underweight", "Overweight", "Obesity"]
smoking_options = ["No Smoking", "Regular", "Occasional"]
employment_options = ["Salaried", "Freelancer", "Self-Employed"]
insurance_plan_options = ["Bronze", "Silver", "Gold"]
disease_options = [
    'No Disease', 'High blood pressure', 'Diabetes',
    'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
    'High blood pressure & Heart disease', 'Diabetes & Thyroid',
    'Diabetes & Heart disease'
]

# Arranged in 3-column grid
features = ['age', 'gender','genetical_risk', 'region', 'marital_status', 'number_of_dependants','bmi_category',
            'smoking_status', 'employment_status','income_lakhs', 'medical_history',
            'insurance_plan']

for i in range(0, len(features), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j >= len(features):
            break
        feature = features[i + j]
        with cols[j]:
            if feature == 'age':
                user_input[feature] = st.number_input("Age", 18, 100, 30)
            elif feature == 'gender':
                user_input[feature] = st.selectbox("Gender", gender_options)
            elif feature == 'genetical_risk':
                user_input[feature] = st.number_input("Genetical Risk", 0, 5, 0)
            elif feature == 'region':
                user_input[feature] = st.selectbox("Region", region_options)
            elif feature == 'marital_status':
                user_input[feature] = st.selectbox("Marital Status", marital_status_options)
            elif feature == 'number_of_dependants':
                user_input[feature] = st.number_input("Number of Dependants", 0, 5, 0)
            elif feature == 'bmi_category':
                user_input[feature] = st.selectbox("BMI Category", bmi_options)
            elif feature == 'smoking_status':
                user_input[feature] = st.selectbox("Smoking Status", smoking_options)
            elif feature == 'employment_status':
                user_input[feature] = st.selectbox("Employment Status", employment_options)
            elif feature == 'income_lakhs':
                user_input[feature] = st.number_input("Income (Lakhs)", 0.0, 100.0, 5.0)
            elif feature == 'medical_history':
                user_input[feature] = st.selectbox("Medical History", disease_options)
            elif feature == 'insurance_plan':
                user_input[feature] = st.selectbox("Insurance Plan", insurance_plan_options)

# Convert the user_input dictionary to a single-row DataFrame
input_df = pd.DataFrame([user_input])
df_to_predict = generate_df(input_df)

# Loading model
model_young = load("./artifacts/model_young.joblib")
model_rest = load("./artifacts/model_rest.joblib")

# Making Predictions
premium_amount = 0
if df_to_predict["age"][0] >26:
    premium_amount = model_rest.predict(df_to_predict)
elif df_to_predict["age"][0]<=26:
    premium_amount = model_young.predict(df_to_predict)
st.success(f"The Premium Amount is ₹{math.floor(premium_amount[0])}")