import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NISR Dashboard", layout="wide")
st.title("NISR Hackton Dashboard")
uploaded_file = st.sidebar.file_uploader("Upload a file")
<<<<<<< HEAD
=======
@st.cache_data
def load_data(file, sheet_names=None):
    
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
    if sheet_names is None:
      data_dict = pd.read_excel(file, sheet_names=None)
      
    else:
        

       data_dict = pd.read_excel(file, sheet_name=[sheet_name1, sheet_name2, sheet_name3, sheet_name4, sheet_name5, sheet_name6, sheet_name7,sheet_name8,sheet_name9,sheet_name10,sheet_name11,sheet_name12,])
       data_combine = pd.concat(data_dict.values(), ignore_index=True)
    return data_combine
>>>>>>> 3ae1a897f903f891f60559965761f6b48bd50776

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
<<<<<<< HEAD

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
=======
    
all_sheet_names = pd.read_excel(uploaded_file, sheet_name=None).keys()
selected_sheets = st.sidebar.multiselect("select sheets", all_sheet_names)


    
    
df_combined = load_data(file=uploaded_file, sheet_names=selected_sheets)

st.dataframe(df_combined,width=800, height=600)
>>>>>>> 3ae1a897f903f891f60559965761f6b48bd50776
