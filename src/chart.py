import pandas as pd
import plotly.express as px
import streamlit as st

# the path to your Excel file
file_path = './data/labour_force_data.xlsx'
sheet_name = 'Table B.1'

# Read the Excel file, skipping the first two rows
df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=2)
df = df.dropna(axis=1, how='all')  # Drop empty columns
df = df.dropna(axis=0, how='all')  # Drop empty rows

# Function to create and display the graph


def g(df):
    st.header("General Labour Force Statistics")

    # Sidebar widget for area of residence selection
    area = st.sidebar.radio('Select Sex', ['Total', 'Male', 'Female'])

    # Adjust the DataFrame to match the required structure
    df_slice = df.iloc[2:5]
    df_adjusted = pd.DataFrame({
        'Indicators': df_slice['Unnamed: 0'],
        'Total': df_slice['Total'],
        'Male': df_slice['Male'],
        'Female': df_slice['Female'],
        # 'Urban': df_slice['Urban'],
        # 'Rural': df_slice['Rural']
    })

    filtered_df = df_adjusted[['Indicators', area]]
   

    fig_dot = px.scatter(df_adjusted, x='Indicators', y=area, title=f'Labour Force Distribution - {area}', color='Indicators', size_max=10)
    fig_dot.update_traces(marker=dict(size=15))

   
    st.plotly_chart(fig_dot)

    st.markdown("------------------------------------------------------------")


# Run the app
if __name__ == '__main__':
    g(df)
    
