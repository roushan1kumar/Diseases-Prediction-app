# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction System (Streamlit App)
Author: Roushan Kumar
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

# -------------------------------
# Load Models (Deploy Friendly)
# -------------------------------

diabetes_model = pickle.load(
    open(r"saved_models\diabetes_model.sav", "rb")
)




heart_disease_model = pickle.load(
    open(r"saved_models\heart_disease_model.sav", "rb")
)

parkinsons_model = pickle.load(
    open(r"saved_models\parkinsons_model.sav", "rb")
)



# -------------------------------
# Sidebar Menu
# -------------------------------
with st.sidebar:
    selected = option_menu(
        "🩺 Multiple Disease Prediction",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
        icons=["activity", "heart", "person"],
        default_index=0
    )

# ======================================================
# Diabetes Prediction Page
# ======================================================
if selected == "Diabetes Prediction":

    st.title("🩸 Diabetes Prediction using Machine Learning")
    st.write("Enter the patient details below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0)

    with col2:
        glucose = st.number_input("Glucose Level", min_value=0)

    with col3:
        bp = st.number_input("Blood Pressure", min_value=0)

    with col1:
        skin = st.number_input("Skin Thickness", min_value=0)

    with col2:
        insulin = st.number_input("Insulin Level", min_value=0)

    with col3:
        bmi = st.number_input("BMI Value", min_value=0.0)

    with col1:
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)

    with col2:
        age = st.number_input("Age", min_value=1)

    # Prediction Button
    if st.button("🔍 Diabetes Test Result"):
        diab_prediction = diabetes_model.predict(
            [[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]]
        )

        if diab_prediction[0] == 1:
            st.error("⚠️ The person is Diabetic")
        else:
            st.success("✅ The person is NOT Diabetic")


# ======================================================
# Heart Disease Prediction Page
# ======================================================
elif selected == "Heart Disease Prediction":

    st.title("❤️ Heart Disease Prediction using Machine Learning")
    st.write("Enter patient heart details:")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1)

    with col2:
        sex = st.number_input("Sex (1 = Male, 0 = Female)", min_value=0, max_value=1)

    with col3:
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0)

    with col2:
        chol = st.number_input("Cholesterol Level", min_value=0)

    with col3:
        thalach = st.number_input("Max Heart Rate Achieved", min_value=0)

    if st.button("🔍 Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, thalach]]
        )

        if heart_prediction[0] == 1:
            st.error("⚠️ High chance of Heart Disease")
        else:
            st.success("✅ No Heart Disease Detected")


# ======================================================
# Parkinson's Prediction Page
# ======================================================
elif selected == "Parkinson's Prediction":

    st.title("🧠 Parkinson's Disease Prediction using ML")
    st.write("Enter voice measurement values:")

    col1, col2 = st.columns(2)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0)

    with col2:
        jitter = st.number_input("MDVP:Jitter(%)", min_value=0.0)

    with col1:
        shimmer = st.number_input("MDVP:Shimmer", min_value=0.0)

    with col2:
        hnr = st.number_input("HNR Value", min_value=0.0)

    if st.button("🔍 Parkinson's Test Result"):
        park_prediction = parkinsons_model.predict(
            [[fo, jitter, shimmer, hnr]]
        )

        if park_prediction[0] == 1:
            st.error("⚠️ Parkinson's Disease Detected")
        else:
            st.success("✅ No Parkinson's Detected")
