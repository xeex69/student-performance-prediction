# Load model
model = pickle.load(open("notebook/student_performance_model.pkl", "rb"))

# IMPORTANT: feature names used during training
feature_names = model.feature_names_in_

# User inputs
studytime = st.slider("Study Time (1–4)", 1, 4, 2)
failures = st.slider("Past Failures (0–3)", 0, 3, 0)
absences = st.slider("Absences", 0, 50, 5)
G1 = st.slider("First Period Grade (G1)", 0, 20, 10)
G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

if st.button("Predict Final Grade"):
    # Create empty input with all features
    input_data = pd.DataFrame(0, index=[0], columns=feature_names)

    # Fill only known features
    input_data["studytime"] = studytime
    input_data["failures"] = failures
    input_data["absences"] = absences
    input_data["G1"] = G1
    input_data["G2"] = G2

    prediction = model.predict(input_data)
    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")
