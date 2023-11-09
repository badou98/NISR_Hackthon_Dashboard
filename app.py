import streamlit as st
import pandas as pd

st.set_page_config(page_title="NISR Dashboard", layout="wide")
st.title("NISR Hackton Dashboard")

df = pd.read_excel("RWLFS2023Q2.xlsx")
print(df)
