import streamlit as st
import pandas as pd
import plotly as pt

st.set_page_config(page_title="NISR Dashboard",layout="wide")
st.title("NISR Hackton Dashboard")
@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data

uploaded_load = st.file_uploader("choose a file")

if uploaded_file is None:
    st.info(" Upload a file through config", icon="i")
    st.stop()
    
    
df = load_data(uploaded_file)
st.dataframe(df)