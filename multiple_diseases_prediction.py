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
# Load Models Safely
# -------------------------------

MODEL_DIR = "saved_models"

@st.cache_resource
def load_models():
    diabetes = pickle.load(open(os.path.join(MODEL_DIR, "diabetes_model.sav"), "rb"))
    heart = pickle.load(open(os.path.join(MODEL_DIR, "heart_disease_model.sav"), "rb"))
    parkinsons = pickle.load(open(os.path.join(MODEL_DIR, "parkinsons_model.sav"), "rb"))
    return diabetes, heart, parkinsons

diabetes_model, heart_disease_model, parkinsons_model = load_models()

# -------------------------------
# Sidebar Menu
# -------------------------------
with st.sidebar:
    st.title("🩺 Disease Prediction App")

    selected = option_menu(
        menu_title="Select Prediction",
        options=[
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinson's Prediction"
        ],
        icons=["activity", "heart", "person"],
        default_index=0
    )

# ======================================================
# Diabetes Prediction Page
# ======================================================
if selected == "Diabetes Prediction":

    st.header("🩸 Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Pregnancies", min_value=0)

    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0)

    with col3:
        BloodPressure = st.number_input("Blood Pressure", min_value=0)

    with col1:
        SkinThickness = st.number_input("Skin Thickness", min_value=0)

    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0)

    with col3:
        BMI = st.number_input("BMI", min_value=0.0)

    with col1:
        DPF = st.number_input("Diabetes Pedigree Function", min_value=0.0)

    with col2:
        Age = st.number_input("Age", min_value=1)

    if st.button("🔍 Predict Diabetes"):
        prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure,
              SkinThickness, Insulin, BMI, DPF, Age]]
        )

        if prediction[0] == 1:
            st.error("⚠️ Person is Diabetic")
        else:
            st.success("✅ Person is NOT Diabetic")

# ======================================================
# Heart Disease Prediction Page
# ======================================================
elif selected == "Heart Disease Prediction":

    st.header("❤️ Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1)

    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"])

    with col3:
        cp = st.number_input("Chest Pain Type (0–3)", min_value=0, max_value=3)

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value=0)

    with col2:
        chol = st.number_input("Cholesterol", min_value=0)

    with col3:
        thalach = st.number_input("Max Heart Rate", min_value=0)

    sex_val = 1 if sex == "Male" else 0

    if st.button("🔍 Predict Heart Disease"):
        prediction = heart_disease_model.predict(
            [[age, sex_val, cp, trestbps, chol, thalach]]
        )

        if prediction[0] == 1:
            st.error("⚠️ High Chance of Heart Disease")
        else:
            st.success("✅ No Heart Disease Detected")

# ======================================================
# Parkinson Prediction Page
# ======================================================
elif selected == "Parkinson's Prediction":

    st.header("🧠 Parkinson's Disease Prediction")

    col1, col2 = st.columns(2)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0)

    with col2:
        jitter = st.number_input("MDVP:Jitter(%)", min_value=0.0)

    with col1:
        shimmer = st.number_input("MDVP:Shimmer", min_value=0.0)

    with col2:
        hnr = st.number_input("HNR", min_value=0.0)

    if st.button("🔍 Predict Parkinson's"):
        prediction = parkinsons_model.predict([[fo, jitter, shimmer, hnr]])

        if prediction[0] == 1:
            st.error("⚠️ Parkinson's Detected")
        else:
            st.success("✅ No Parkinson's Detected")
