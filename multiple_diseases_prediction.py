# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction System (Streamlit + MySQL)
Author: Roushan Kumar
"""

import pickle
import streamlit as st
import mysql.connector
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
# MySQL Connection Function
# -------------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",   # <-- change this
        database="disease_prediction"
    )

# -------------------------------
# Save Prediction to MySQL
# -------------------------------
def save_to_mysql(name, dob, pincode, disease, result):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO predictions (name, dob, pincode, disease, result)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, dob, pincode, disease, result))
    conn.commit()

    cursor.close()
    conn.close()

# -------------------------------
# Show Records from MySQL
# -------------------------------
def fetch_records():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

# -------------------------------
# Load Models
# -------------------------------
@st.cache_resource
def load_models():
    diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))
    heart_model = pickle.load(open("heart_disease_model.sav", "rb"))
    parkinsons_model = pickle.load(open("parkinsons_model.sav", "rb"))

    return diabetes_model, heart_model, parkinsons_model

diabetes_model, heart_disease_model, parkinsons_model = load_models()

# -------------------------------
# Sidebar Menu
# -------------------------------
with st.sidebar:
    st.title("🩺 Disease Prediction App")

    selected = option_menu(
        "Select Prediction",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "View Database Records"],
        icons=["activity", "heart", "person", "database"],
        default_index=0
    )

# -------------------------------
# Common Patient Info
# -------------------------------
def patient_details():
    st.subheader("👤 Patient Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input("Patient Name")

    with col2:
        dob = st.date_input("Date of Birth")

    with col3:
        pincode = st.text_input("Pincode")

    return name, dob, pincode

# ======================================================
# Diabetes Prediction Page
# ======================================================
if selected == "Diabetes Prediction":

    st.header("🩸 Diabetes Prediction")

    name, dob, pincode = patient_details()

    st.subheader("🧪 Medical Inputs")

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
        prediction = diabetes_model.predict([[
            Pregnancies, Glucose, BloodPressure,
            SkinThickness, Insulin, BMI, DPF, Age
        ]])

        if prediction[0] == 1:
            result = "Diabetic"
            st.error("⚠️ The person is Diabetic")
        else:
            result = "Not Diabetic"
            st.success("✅ The person is NOT Diabetic")

        save_to_mysql(name, dob, pincode, "Diabetes", result)
        st.success("✅ Saved in MySQL Database")

# ======================================================
# Heart Disease Prediction Page
# ======================================================
elif selected == "Heart Disease Prediction":

    st.header("❤️ Heart Disease Prediction")

    name, dob, pincode = patient_details()

    st.subheader("🧪 Medical Inputs")

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
        prediction = heart_disease_model.predict([[
            age, sex_val, cp, trestbps, chol, thalach
        ]])

        if prediction[0] == 1:
            result = "Heart Disease Detected"
            st.error("⚠️ High Chance of Heart Disease")
        else:
            result = "No Heart Disease"
            st.success("✅ No Heart Disease Detected")

        save_to_mysql(name, dob, pincode, "Heart Disease", result)
        st.success("✅ Saved in MySQL Database")

# ======================================================
# Parkinson Prediction Page
# ======================================================
elif selected == "Parkinson's Prediction":

    st.header("🧠 Parkinson's Prediction")

    name, dob, pincode = patient_details()

    st.subheader("🧪 Voice Measurement Inputs")

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
            result = "Parkinson's Detected"
            st.error("⚠️ Parkinson's Detected")
        else:
            result = "No Parkinson's"
            st.success("✅ No Parkinson's Detected")

        save_to_mysql(name, dob, pincode, "Parkinson's", result)
        st.success("✅ Saved in MySQL Database")

# ======================================================
# View Database Records Page
# ======================================================
elif selected == "View Database Records":

    st.header("📋 Prediction History Stored in MySQL")

    records = fetch_records()

    if len(records) == 0:
        st.warning("No records found yet.")
    else:
        st.table(records)

