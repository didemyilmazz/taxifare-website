import streamlit as st
import numpy as np
import pandas as pd

from datetime import datetime
import requests

st.title ("NY Taxi")
st.markdown("""# Taxifare Model
## Select your ride
""")

date = st.date_input("Select Date", value=datetime.today())
time = st.time_input("Select Time", value=datetime.now().time())

pickup_longitude = st.number_input("Pickup Longitude", value=0)
pickup_latitude = st.number_input("Pickup Latitude", value=0)

dropoff_longitude = st.number_input("Dropoff Longitude", value=0)
dropoff_latitude = st.number_input("Dropoff Latitude", value=0)

passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

st.write(f"Date and Time: {date} {time}")
st.write(f"Pickup coordinates: ({pickup_latitude}, {pickup_longitude})")
st.write(f"Dropoff coordinates: ({dropoff_latitude}, {dropoff_longitude})")
st.write(f"Passenger count: {passenger_count}")

pickup_datetime = datetime.combine(date, time)

params = {"pickup_datetime": pickup_datetime,
"pickup_longitude": pickup_longitude,
"pickup_latitude": pickup_latitude,
"dropoff_longitude": dropoff_longitude,
"dropoff_latitude": dropoff_latitude,
"passenger_count": passenger_count
}

url = 'https://taxifare.lewagon.ai/predict'

response = requests.get(url, params=params)
prediction = response.json()

st.header("Prediction")
st.write("The estimated fare is:", prediction["fare"])
