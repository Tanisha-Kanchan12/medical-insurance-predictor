import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Medical Insurance Predictor")

st.title("Medical Insurance Cost Predictor")
st.write("App is running successfully ✅")

# Load model
model = pickle.load(open("linear_regression_model.pkl", "rb"))

age = st.slider("Age", 18, 100, 25)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
gender = st.selectbox("Gender", ["male", "female"])
children = st.selectbox("Children", [0, 1, 2, 3, 4, 5])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

gender = 1 if gender == "male" else 0
smoker = 1 if smoker == "yes" else 0

region_map = {
    "southwest": 0,
    "southeast": 1,
    "northwest": 2,
    "northeast": 3
}
region = region_map[region]

if st.button("Predict"):
    data = np.array([[age, gender, bmi, children, smoker, region]])
    prediction = model.predict(data)
    st.success(f"Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")
