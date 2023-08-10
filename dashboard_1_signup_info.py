
import streamlit as st
import pandas as pd

# Load data
drivers_df = pd.read_csv('/home/ubuntu/Desktop/VTC_DASHBOARD_STREAMLIT/drivers.csv')

# Filter based on signup date
start_date = st.date_input("Start date", drivers_df['Signup_Date'].min())
end_date = st.date_input("End date", drivers_df['Signup_Date'].max())
filtered_df = drivers_df[(drivers_df['Signup_Date'] >= start_date) & (drivers_df['Signup_Date'] <= end_date)]

# Display data
st.write(filtered_df)
