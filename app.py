import pandas as pd
import plotly as pt
import streamlit as st

st.set_page_config(page_title="NISR Dashboard", layout="wide")
st.title(" :bar_chart: NISR Hackton Dashboard")
uploaded_file = st.sidebar.file_uploader("Upload a file")

def load_data(file, sheet_names):
    data_dict = pd.read_excel(file, sheet_name=sheet_names)
    data_combined = pd.concat(data_dict.values(), ignore_index=True)

  
    data_combined = pd.DataFrame(data_combined)

    
    data_combined.fillna('', inplace=True)

    
    data_combined = data_combined.applymap(lambda x: '{:,.0f}'.format(x) if pd.notna(x) and pd.api.types.is_numeric_dtype(x) else x)

    return data_combined

if uploaded_file is not None:
    all_sheet_names = pd.read_excel(uploaded_file, sheet_name=None).keys()
    selected_sheets = st.sidebar.multiselect("select sheets", all_sheet_names)

    df_combined = load_data(file=uploaded_file, sheet_names=selected_sheets)
    with st.expander("Data Analysis"):
        st.dataframe(df_combined)
else:
    st.info("Upload a file through config")
    st.stop()
