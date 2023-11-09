import streamlit as st
import pandas as pd

st.set_page_config(page_title="NISR Dashboard", layout="wide")
st.title("NISR Hackton Dashboard")

@st.cache
def load_data(file):
    data = pd.read_excel(file)
    return data

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info("Upload a file through the file uploader.")
    st.stop()

df = load_data(uploaded_file)
st.dataframe(df)
