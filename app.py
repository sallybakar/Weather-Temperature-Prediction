import streamlit as st

#st.title("Hello, Streamlit!")
#st.write("This is your first Streamlit app. 🚀")
import joblib
import numpy as np
import pandas as pd

# Load the best trained model
model = joblib.load("best_extratrees_model(4).pkl")

# Define input fields based on important features
important_features = [
    "feels_like_celsius", "humidity", "wind_kph", "air_quality_Carbon_Monoxide", 
    "air_quality_Ozone", "uv_index", "pressure_in", "cloud", "gust_kph"
]

# Streamlit app with custom styling
st.set_page_config(page_title="Weather Temperature Prediction", page_icon="🌤️")

st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6;
            color: #333333;
        }
        .stApp {
            background-color: #e6f7ff;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

st.title("🌡️ Weather Temperature Prediction")
st.write("Enter the weather conditions to predict the temperature.")

# User input fields
def user_input_features():
    inputs = {}
    for feature in important_features:
        inputs[feature] = st.number_input(f"{feature}", value=0.0, format="%.2f")
    return pd.DataFrame([inputs])

data_input = user_input_features()

if st.button("Predict Temperature", key="predict"):
    prediction = model.predict(data_input)[0]
    st.success(f"Predicted Temperature (°C): {prediction:.2f}")

# Option to display dataset preview
#if st.checkbox("Show Sample Data Format"):
    #sample_data = pd.DataFrame(columns=important_features, data=np.random.rand(5, len(important_features)) * 10)
    #st.write(sample_data)
