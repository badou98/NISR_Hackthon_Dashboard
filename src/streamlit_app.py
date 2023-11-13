import streamlit as st
import pandas as pd

# Import your graph functions.
from first import graph1


# Set page configuration
st.set_page_config(layout="wide", page_title="NISR Hackton Dashboard",
                   page_icon=":bar_chart:", initial_sidebar_state="expanded")

# Load your data here for each graph
df_b1 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.1', skiprows=2)
df_b1.dropna(axis=1, how='all', inplace=True)
df_b1.dropna(axis=0, how='all', inplace=True)

df_b5 = pd.read_excel('./data/labour_force_data.xlsx',
                      sheet_name='Table B.5', skiprows=1)
df_b5.dropna(axis=1, how='all', inplace=True)
df_b5.dropna(axis=0, how='all', inplace=True)



# Title container
with st.container():
    st.title(" :bar_chart: NISR Hackthon Dashboard")

# Graph container
with st.container():


    # Define a list of graph functions
    graph_functions = [graph1,graph2]
    dataframes = [df_b1, df_b5]

    # Initialize session state for the index of the current graph
    if 'current_graph_index' not in st.session_state:
        st.session_state.current_graph_index = 0

    # Display the current graph
    current_graph_index = st.session_state.current_graph_index
    graph_functions[current_graph_index](dataframes[current_graph_index])

