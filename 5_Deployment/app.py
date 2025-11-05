import streamlit as st
import joblib
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore", message=".*ScriptRunContext.*")

# Load trained model and scaler
model = joblib.load("../4_Feature_selection_and_Model_creation/linear_regression_exam_score.pkl")
scaler = joblib.load("../4_Feature_selection_and_Model_creation/scaler.pkl")

# App title
st.title("🎓 Student Exam Score Predictor")
st.write("Enter student details below to predict the expected exam score.")

# Input fields
hours_studied = st.number_input("Hours Studied", min_value=0.0, max_value=24.0, value=6.0)
sleep_hours = st.number_input("Sleep Hours per Day", min_value=0.0, max_value=24.0, value=7.0)
attendance_percent = st.slider("Attendance (%)", 0, 100, 80)
previous_scores = st.number_input("Previous Exam Score", min_value=0.0, max_value=100.0, value=75.0)

# Create dataframe for prediction
input_data = pd.DataFrame({
    'hours_studied': [hours_studied],
    'sleep_hours': [sleep_hours],
    'attendance_percent': [attendance_percent],
    'previous_scores': [previous_scores]
})

# Predict button
if st.button("Predict Exam Score"):
    scaled = scaler.transform(input_data)
    prediction = model.predict(scaled)
    st.success(f"📈 Predicted Exam Score: {prediction[0]:.2f}")
