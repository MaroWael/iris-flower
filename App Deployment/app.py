from controller.LoadModel import LoadModel
from controller.GetPrediction import GetPrediction
import streamlit as st

st.title("Flowers App Prediction")

sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Sepal width (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Petal width (cm)', min_value=0.0, max_value = 10.0, step=0.1)

model = LoadModel("model/iris_model.pkl")

if st.button("Predict"):
    prediction = GetPrediction(model, [sepal_length, sepal_width, petal_length, petal_width])
    st.write(f"Your flower is: {prediction}")