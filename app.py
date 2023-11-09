import streamlit as st
import pandas as pd
import plotly as pt

st.set_page_config(page_title="NISR Dashboard",layout="wide")
st.title("NISR Hackton Dashboard")
uploaded_file = st.sidebar.file_uploader("Upload a file")
@st.cache_data
def load_data(file):
    sheet_name1 = "Table B.1"
    sheet_name2 = "Table B.2"
    sheet_name3 = "Table B.3"
    sheet_name4 = "Table B.4"
    sheet_name5 = "Table B.5"
    sheet_name6 = "Table B.6"
    sheet_name7 = "Table B.7"
    sheet_name8 = "Table B.8"
    sheet_name9 = "Table B.9"
    sheet_name10 = "Table B.10"
    sheet_name11 = "Table B.11"
    sheet_name12 = "Table B.12"
    data = pd.read_excel(file, sheet_name=sheet_name1,sheet_name2)
    return data



if uploaded_file is None:   
    st.info("Upload a file through config")
    st.stop()
    
    
df = load_data(uploaded_file)
st.dataframe(df)