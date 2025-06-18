# app.py
import streamlit as st

st.image("header.png", use_column_width=True)

import pandas as pd
import numpy as np
import pickle

st.markdown("---")
st.markdown("Made with ❤️ by Dr. MOhamad Fattouh", unsafe_allow_html=True)

# Load model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🩺 Diabetes Predictor")
st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
    }
    .result-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dbeafe;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)


# Input fields
st.markdown("## 👤 Enter Patient Information")

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.number_input("Pregnancies", 0, 20)
    Glucose = st.number_input("Glucose", 0, 200)
    BloodPressure = st.number_input("Blood Pressure", 0, 150)
    SkinThickness = st.number_input("Skin Thickness", 0, 100)

with col2:
    Insulin = st.number_input("Insulin", 0, 900)
    BMI = st.number_input("BMI", 0.0, 70.0)
    DiabetesPedigreeFunction = st.number_input("Pedigree Function", 0.0, 3.0)
    Age = st.number_input("Age", 1, 120)

if st.button("🔍 Predict"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DiabetesPedigreeFunction, Age]])
    prediction = model.predict(input_data)
    result = "🟥 Diabetic" if prediction[0] == 1 else "🟩 Not Diabetic"
    st.markdown(f"""
    <div class='result-box'>
        <p class='big-font'>🧾 <strong>Prediction:</strong> {result}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 💡 Health Advice Chatbot")

user_input = st.text_input("Describe your symptoms:")

st.markdown("## 💬 Health Advice Chatbot")

user_input = st.text_input("Describe your symptoms (e.g., 'I have nausea and headache'):")

def get_advice(symptoms):
    symptoms = symptoms.lower()
    if "headache" in symptoms and "nausea" in symptoms:
        return "🧠 You might be dehydrated or have a migraine. Drink water and rest. If it persists, consult a doctor."
    elif "fever" in symptoms and "cough" in symptoms:
        return "🤒 Possible flu or infection. Stay hydrated and monitor your temperature. Consider a COVID test."
    elif "chest pain" in symptoms:
        return "⚠️ Chest pain can be serious. Seek immediate medical attention!"
    elif "fatigue" in symptoms:
        return "😴 Get enough rest, check your diet, and drink plenty of water."
    elif "diarrhea" in symptoms or "vomiting" in symptoms:
        return "🥴 You may have food poisoning or a stomach bug. Stay hydrated. If symptoms persist, consult a doctor."
    elif symptoms.strip() == "":
        return None
    else:
        return "📌 Please consult a healthcare professional for detailed advice."

# Show response if user typed something
if user_input.strip():
    advice = get_advice(user_input)
    if advice:
        st.success(advice)


