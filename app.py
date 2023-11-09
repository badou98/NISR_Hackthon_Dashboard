import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NISR Dashboard", layout="wide")
st.title("NISR Hackton Dashboard")
uploaded_file = st.sidebar.file_uploader("Upload a file")

@st.cache
def load_data(file, sheet_names=None):
    if sheet_names is None:
        data_combine = pd.read_excel(file)
    else:
        data_dict = pd.read_excel(file, sheet_name=sheet_names)
        data_combine = pd.concat(data_dict.values(), ignore_index=True)
    return data_combine

if uploaded_file is None:
    st.info("Upload a file through config")
    st.stop()

all_sheet_names = pd.read_excel(uploaded_file, sheet_name=None).keys()
selected_sheets = st.sidebar.multiselect("Select sheets", all_sheet_names)

df_combined = load_data(file=uploaded_file, sheet_names=selected_sheets)

st.dataframe(df_combined)

# Filter data based on user selection
years = st.sidebar.slider("Select Years", min_value=df_combined['Year'].min(), max_value=df_combined['Year'].max(), value=(df_combined['Year'].min(), df_combined['Year'].max()))
selected_countries = st.sidebar.multiselect("Select Countries", df_combined['Country'].unique())

filtered_data = df_combined[(df_combined['Year'].between(years[0], years[1])) & (df_combined['Country'].isin(selected_countries))]

# Visualizations
st.header("Visualizations")

# GDP Visualization
if 'GDP' in filtered_data.columns:
    fig_gdp = px.line(filtered_data, x='Year', y='GDP', color='Country', title='GDP Over Years')
    st.plotly_chart(fig_gdp)

# CPI Visualization
if 'CPI' in filtered_data.columns:
    fig_cpi = px.bar(filtered_data, x='Year', y='CPI', color='Country', title='Consumer Price Index Over Years')
    st.plotly_chart(fig_cpi)

# LFS Visualization
if 'Labour Force' in filtered_data.columns:
    fig_lfs = px.scatter(filtered_data, x='Year', y='Labour Force', color='Country', title='Labour Force Survey Over Years')
    st.plotly_chart(fig_lfs)
