import streamlit as st
import pandas as pd
import numpy as np

st.header("Header")
st.subheader('Subheader')
st.caption("Caption")

# dataset awal
df = pd.read_csv("https://raw.githubusercontent.com/PA-PDAB/CAPSTONEDIGIPRODUCT_PDAB_TEAM6/main/dataset.csv")
st.dataframe(data=df, width=500, height=500)

# dataset sudah clear
df = pd.read_csv("https://raw.githubusercontent.com/PA-PDAB/CAPSTONEDIGIPRODUCT_PDAB_TEAM6/main/Data%20Cleaned.csv")
st.dataframe(data=df, width=500, height=500)