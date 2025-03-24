# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PoAU_0KOD-Jq3HTQv_29jMe49K-pf3p3
"""

import streamlit as st
import requests

st.title("Educational Intervention Impact Predictor")

# User Inputs
hours = st.slider("Hours Studied", 0, 50, 10)
attendance = st.slider("Attendance (%)", 50, 100, 90)
engagement = st.slider("Engagement Level", 1, 5, 3)
intervention = st.selectbox("Intervention Used", [0, 1])
homework = st.slider("Homework Completed (%)", 50, 100, 80)
peer_interaction = st.slider("Peer Interaction Level", 1, 5, 3)
class_participation = st.slider("Class Participation Level", 1, 10, 7)
internet_access = st.selectbox("Internet Access", [0, 1])
family_support = st.slider("Family Support Level", 1, 5, 3)
learning_resources = st.slider("Learning Resources Available", 1, 10, 6)
past_performance = st.slider("Past Performance (%)", 50, 100, 85)
study_env = st.slider("Study Environment Score", 1, 5, 4)
motivation = st.slider("Motivation Level", 1, 5, 3)
teacher_feedback = st.slider("Teacher Feedback Score", 1, 10, 8)

# Prediction Button
if st.button("Predict Performance"):
    input_features = [hours, attendance, engagement, intervention, homework, peer_interaction,
                      class_participation, internet_access, family_support, learning_resources,
                      past_performance, study_env, motivation, teacher_feedback]

    response = requests.post("http://127.0.0.1:5000/predict", json={"features": input_features})

    if response.status_code == 200:
        prediction = response.json()['prediction']
        result = "Pass" if prediction == 1 else "Fail"
        st.success(f"Predicted Performance: {result}")
    else:
        st.error("Error in prediction service")

!pip install streamlit