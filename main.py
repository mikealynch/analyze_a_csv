import streamlit as st

# Define the containers for Streamlit layout
header = st.container()
data = st.container()
features = st.container()
modelTraining = st.container()




st.title("Let's analyze a CSV")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

