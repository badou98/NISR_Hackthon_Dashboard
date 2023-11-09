import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache
def load_data(file_url, sheet_names=None):
    if sheet_names is None:
        data_dict = pd.read_excel(file_url, sheet_name=None)
    else:
        data_dict = pd.read_excel(file_url, sheet_name=sheet_names)
    data_combine = pd.concat(data_dict.values(), ignore_index=True)
    return data_combine


def create_line_chart(data, y_column, title):
    fig = px.line(data, x='Year', y=y_column, title=title)
    return fig


uploaded_file = st.sidebar.file_uploader("Upload a file", type=["xlsx"])


st.set_page_config(page_title="NISR Dashboard", layout="wide")
st.title("NISR Hackton Dashboard")


if uploaded_file:
    st.warning("Please ignore the file upload. Data will be loaded from the provided URL.")
    st.stop()


all_sheet_names = pd.read_excel("https://github.com/badou98/NISR_Hackton_Dashboard/raw/main/RWLFS2023Q2.xlsx", sheet_name=None).keys()
selected_sheets = st.sidebar.multiselect("Select sheets", all_sheet_names)

df_combined = load_data("https://github.com/badou98/NISR_Hackton_Dashboard/raw/main/RWLFS2023Q2.xlsx", sheet_names=selected_sheets)


st.subheader("Data Table")
st.dataframe(df_combined)

if selected_sheets:
    st.subheader("Selected Sheets")
    for sheet_name in selected_sheets:
        st.write(f"- {sheet_name}")


st.subheader("Line Charts")
columns = st.columns(len(selected_sheets))

for i, sheet_name in enumerate(selected_sheets):
    y_column = st.selectbox(f"Select Y-axis for {sheet_name}", df_combined.columns, index=i)
    title = f"{sheet_name} - {y_column}"
    fig = create_line_chart(df_combined, y_column, title)
    columns[i].plotly_chart(fig)
