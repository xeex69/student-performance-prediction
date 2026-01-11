import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Student Performance Prediction")

st.title("🎓 Student Performance Prediction")
st.write("Predict final student grade (G3)")

# Load dataset
data = pd.read_csv("data/student_data.xlsx")

# Select features for demo model
FEATURES = ["studytime", "failures", "absences", "G1", "G2"]
TARGET = "G3"

X = data[FEATURES]
y = data[TARGET]

# Train model (lightweight, fast)
model = LinearRegression()
model.fit(X, y)

# User inputs
studytime = st.slider("Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Failures (0–3)", 0, 3, 0)
absences = st.slider("Absences", 0, 50, 5)
G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

if st.button("Predict Final Grade"):
    input_data = pd.DataFrame([[studytime, failures, absences, G1, G2]],
                              columns=FEATURES)

    prediction = model.predict(input_data)
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")
