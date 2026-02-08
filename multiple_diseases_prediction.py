# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 11:56:42 2026

@author: Roushan Kumar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models

diabetes_model = pickle.load(open('C:/Users/Roushan Kumar/OneDrive/Desktop/Multiple Diseases Prediction System/saved models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('C:/Users/Roushan Kumar/OneDrive/Desktop/Multiple Diseases Prediction System/saved models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('C:/Users/Roushan Kumar/OneDrive/Desktop/Multiple Diseases Prediction System/saved models/parkinsons_model.sav','rb'))



# sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Diseases Prediction System using ML',
                           ['Diabetes Prediction',
                            'Heart Diseases Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)

# Diabates prediction page

if(selected == 'Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using Ml')
    
    # getting data from the user 
    #colums from input field
    col1, col2, col3 = st.columns(3)
    
    with col1:
       pregnancies = st.text_input("Number of pregnancies")
    with col2:
       Glucose = st.text_input("Glucose level")
    with col3:
        
       BloodPressure = st.text_input('Blood pressure value')
    with col1:   
      SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
       Insulin = st.text_input("Insulin level")
    with col3:
      BMI = st.text_input('BMI value')
    with col1:
        
      DiabetesPedigreeFunction = st.text_input("Pedigree  Value")
    with col2:
      Age = st.text_input("Age")
    

# code for predictions
    diab_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis ='The Person is Diabatics'
        else:
            diab_diagnosis = 'The person is not diagnosis'
    st.success(diab_diagnosis)

if(selected == 'Heart Diseases Prediction'):
    
    st.title('heart Diseases Prediction using Ml')
    col1, col2, col3 = st.columns(3)
    with col1:
       pregnancies = st.text_input("Number of pregnancies")
    with col2:
       Glucose = st.text_input("Glucose level")
    with col3:
        
       BloodPressure = st.text_input('Blood pressure value')
    with col1:   
      SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
       Insulin = st.text_input("Insulin level")
    with col3:
      BMI = st.text_input('BMI value')
    with col1:
        
      DiabetesPedigreeFunction = st.text_input("Pedigree  Value")
    with col2:
      Age = st.text_input("Age")
    
if(selected == 'Parkinsons Prediction'):
    
    st.title('Parkinsons Prediction using Ml') 
    col1, col2, col3 = st.columns(3)
    with col1:
       pregnancies = st.text_input("Number of pregnancies")
    with col2:
       Glucose = st.text_input("Glucose level")
    with col3:
        
       BloodPressure = st.text_input('Blood pressure value')
    with col1:   
      SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
       Insulin = st.text_input("Insulin level")
    with col3:
      BMI = st.text_input('BMI value')
    with col1:
        
      DiabetesPedigreeFunction = st.text_input("Pedigree  Value")
    with col2:
      Age = st.text_input("Age")
    

