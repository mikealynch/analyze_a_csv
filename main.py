import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import openai


api_key = st.secrets["API_KEY"]


openai.api_key = api_key


openai_llm = OpenAI(api_token=openai.api_key)


st.title("Let's analyze a CSV")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("First three rows:")
    st.write(df.head(3))
    
    prompt = st.text_area("Ask me a question about your file.")
    
    if st.button("GO"):
        if prompt:
            st.write("Let me think about that for a minute.")
            
            openai_llm = OpenAI(api_token=openai.api_key)

            sdf=SmartDataframe(df, config={"llm": openai_llm})

            ai_response = sdf.chat(prompt)
            st.write(ai_response)

        else:
            st.warning("Ask me a question about your file.")
