
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
rides_df = pd.read_csv('/home/ubuntu/Desktop/VTC_DASHBOARD_STREAMLIT//rides.csv')

# Histogram of driver ratings
st.title("Driver Ratings Histogram")
ratings = rides_df['Rating']
plt.hist(ratings, bins=20, edgecolor='k')
plt.xlabel('Rating')
plt.ylabel('Number of Rides')
plt.title('Distribution of Driver Ratings')
st.pyplot(plt.gcf())
