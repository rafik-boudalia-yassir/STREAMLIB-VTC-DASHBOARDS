
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
rides_df = pd.read_csv('/home/ubuntu/Desktop/VTC_DASHBOARD_STREAMLIT//rides.csv')

# Scatter plot of earnings vs. tips
st.title("Earnings vs. Tips Scatter Plot")
plt.scatter(rides_df['Earnings'], rides_df['Tips'], alpha=0.5)
plt.xlabel('Earnings ($)')
plt.ylabel('Tips ($)')
plt.title('Earnings vs. Tips for Each Ride')
st.pyplot(plt.gcf())
