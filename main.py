# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:50:16 2024

@author: MIke Lynch
"""


from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import openai


load_dotenv()
api_key = os.getenv("API_KEY")

openai.api_key = api_key


openai_llm = OpenAI(api_token=openai.api_key)


st.title("Let's analyze a CSV")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=['csv'])

