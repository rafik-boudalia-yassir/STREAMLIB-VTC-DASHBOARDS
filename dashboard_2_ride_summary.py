
import streamlit as st
import pandas as pd

# Load data
drivers_df = pd.read_csv('/home/ubuntu/Desktop/VTC_DASHBOARD_STREAMLIT/drivers.csv')
rides_df = pd.read_csv('/home/ubuntu/Desktop/VTC_DASHBOARD_STREAMLIT//rides.csv')

# Select driver
driver_id = st.selectbox("Choose a driver", drivers_df['Driver_ID'].unique())
selected_rides = rides_df[rides_df['Driver_ID'] == driver_id]

# Display rides
st.write(selected_rides[['Date', 'Distance_km', 'Earnings', 'Tips', 'Rating']])
