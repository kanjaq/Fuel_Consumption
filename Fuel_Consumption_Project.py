import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
from PIL import Image
#Color
#load trained model
model = joblib.load("best_model1.pkl")

# Define the app title and layout
st.title("Fuel Consumption -2023")
st.text('Fuel consumption ratings and estimated carbon dioxide emissions for vehicles')

image = Image.open('dataset-cover.jpg')
st.sidebar.image(image, caption='Fuel')
Vehicle_make = st.sidebar.selectbox ('Make',('Ford','Ram','Land Rover' ,'Nissan','Chevrolet','BMW','Aston Martin','Infiniti','Bentley','Dodge','Maserati','Bugatti','Mercedes-Benz','Cadillac','GMC','Audi','Rolls-Royce','Lamborghini','Jeep'))
Vehicle_Models= st.sidebar.selectbox('Model',())

# Define input fields for features
CO2_Emmissions = st.selectbox("CO2 Emmissions", range(50,300,20))
Engine_size = st.number_input("Engine Size", min_value=0, max_value=10, value=5, step=1)
Cylinders = st.number_input("Cylinders", min_value=0.0, max_value=30.0, value=10.0, step=1.0)
Fuel_Consumption = st.number_input("City Fuel Consumption Litres per 100KM ",min_value =5, max_value=30, step=2)
Highway_Fuel_Consumption = st.number_input("Highway Fuel Consumption Litres per 100KM ",min_value =5, max_value=30, step=2)
Comb_Fuel_Consumption = st.number_input("City/ Highway Fuel Consumption Litres per 100KM ",min_value =5, max_value=30, step=2)
CO2_Rating = st.selectbox("CO2 Ratings", range(0,10,1))
SMOG_Rating = st.selectbox("SMOG Ratings", range(0,10,1))
Fuel_Type = st.selectbox("Fuel Type", [0, 1 , 1])


#prediction
if st.button('predict'):
    Make_Prediction = model.predict([[Engine_size,CO2_Emmissions,Cylinders,Fuel_Consumption,Highway_Fuel_Consumption,Comb_Fuel_Consumption,CO2_Rating,SMOG_Rating,Fuel_Type]])
    output = round(Make_Prediction[0],2)
    st.success('Your Vehicle Carbon Emmission is {}'.format(output))
