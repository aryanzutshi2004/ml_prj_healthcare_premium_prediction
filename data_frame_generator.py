import pandas as pd
import streamlit as st
from joblib import load
from risk_cal import calculate_risk

#Loading scaler object
scaler_rest_dict = load("./artifacts/scaler_rest.joblib")
scaler_young_dict = load("./artifacts/scaler_young.joblib")

scaler_young, cols_to_scale_young = scaler_young_dict.get("scaler"),scaler_young_dict.get("columns")
scaler_rest, cols_to_scale_rest = scaler_rest_dict.get("scaler"),scaler_rest_dict.get("columns")

data_frame_columns = ['age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
       'genetical_risk', 'total_risk', 'gender_Male', 'region_Northwest',
       'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
       'bmi_category_Obesity', 'bmi_category_Overweight',
       'bmi_category_Underweight', 'employment_status_Salaried',
       'employment_status_Self-Employed', 'smoking_status_Occasional',
       'smoking_status_Regular']

def generate_df(df):
    df_encoded = df.copy()

    # Ordinal encoding
    df_encoded["insurance_plan"] = df["insurance_plan"].map({"Bronze":0, "Silver":1,
                                                             "Gold":2})
    # Nominal Encoding
    nominal_cols = ["gender", "region", "marital_status",
                  "bmi_category", "smoking_status", "employment_status"]
    df_encoded = pd.get_dummies(df_encoded,columns= nominal_cols, dtype="int64")
    #  Calculating Total risk
    disease = df_encoded["medical_history"][0]
    df_encoded["total_risk"] = calculate_risk(disease)
    df_encoded = df_encoded.reindex(columns=data_frame_columns, fill_value=0)

    #  Scaling num features
    df_encoded["income_level"] = -1
    if df_encoded["age"][0]>26:
        df_encoded[cols_to_scale_rest] = scaler_rest.transform(df_encoded[cols_to_scale_rest])
    elif df_encoded["age"][0]<=26:
        df_encoded[cols_to_scale_young] = scaler_young.transform(df_encoded[cols_to_scale_young])
    df_encoded = df_encoded.drop("income_level", axis="columns")
    return df_encoded
