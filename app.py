# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:24:05 2023

@author: ZMZM
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.markdown("<h2 style='text-align: center; color: yellow;'>نظام لمعرفة اذا كنت مصاب بمرض السكري أو غير مصاب</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: right; color: white;'>يرجى ادخال بيانات الفحوصات الاتية</h4>", unsafe_allow_html=True)

# getting the input data from the user
    
    
Pregnancies = st.text_input('عدد مرات الحمل للمرأة')
Glucose = st.text_input('مستوى الجلوكوز')
BloodPressure = st.text_input('ضغط الدم')
SkinThickness = st.text_input('سماكة الجلد')
Insulin = st.text_input('مستوى الانسولين')
BMI = st.text_input('مؤشر كتلة الجسم')
Age = st.text_input('العمر')
    
    
    # code for Prediction
diab_diagnosis = ''
    
    # creating a button for Prediction
    
if st.button('اختبار نتيجة الفحوصات'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'الشخص مصاب بمرض السكري'
        else:
          diab_diagnosis = 'الشخص غير مصاب بمرض السكري'
        
st.success(diab_diagnosis)
    
    
# Set a title with adjusted size
st.markdown("<h5style='text-align: center; color: red;'> Founded by Tariq Ibrahim </h5>", unsafe_allow_html=True)
