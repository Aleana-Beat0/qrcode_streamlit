import pandas as pd
import streamlit as st

st.set_page_config(page_title="Listening", layout="wide")

df = pd.read_csv("C:/Users/alean/OneDrive/Desktop/python/qrcode_streamlit/names.xlsx")

st.dataframe(df)