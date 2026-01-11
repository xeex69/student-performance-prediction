import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("notebook/student_performance_model.pkl", "rb"))

st.title("🎓 Student Performance Prediction")

st.write("Enter student details to predict final grade (G3)")

# Input fields (basic ones)
studytime = st.slider("Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Failures (0–3)", 0, 3, 0)
absences = st.slider("Absences", 0, 50, 5)
G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

# Create input DataFrame (dummy for other features)
input_data = pd.DataFrame({
    "studytime": [studytime],
    "failures": [failures],
    "absences": [absences],
    "G1": [G1],
    "G2": [G2]
})

# Predict
if st.button("Predict Final Grade"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")
