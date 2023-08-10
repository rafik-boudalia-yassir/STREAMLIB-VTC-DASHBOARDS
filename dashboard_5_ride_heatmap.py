
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
rides_df = pd.read_csv('/home/ubuntu/Desktop/VTC_DASHBOARD_STREAMLIT//rides.csv')

# Simulate heatmap data
heatmap_data = rides_df['Earnings'].values.reshape(100, 100)
plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Earnings ($)')
plt.title('Heatmap of Ride Earnings (Simulated)')
st.pyplot(plt.gcf())
