import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Student Performance Prediction")

st.title("🎓 Student Performance Prediction")
st.write("Predict final student grade (G3)")

# Load trained model
model = pickle.load(open("notebook/student_performance_model.pkl", "rb"))

# EXACT feature list used during training
FEATURES = [
    'age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
    'famrel', 'freetime', 'goout', 'Dalc', 'Walc',
    'health', 'absences', 'G1', 'G2'
]

# User inputs
studytime = st.slider("Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Failures (0–3)", 0, 3, 0)
absences = st.slider("Absences", 0, 50, 5)
G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

if st.button("Predict Final Grade"):
    # Create input row with default values
    input_data = pd.DataFrame([[0]*len(FEATURES)], columns=FEATURES)

    # Fill known values
    input_data["studytime"] = studytime
    input_data["failures"] = failures
    input_data["absences"] = absences
    input_data["G1"] = G1
    input_data["G2"] = G2

    prediction = model.predict(input_data)
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")
