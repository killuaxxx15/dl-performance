import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Set Streamlit page configuration
st.set_page_config(page_title='Performance', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Performance')

# Cache data loading function for better performance
@st.cache_data
def load_gsheet_data():
    # Initialize connection to Google Sheets
    conn = st.connection('gsheets', type=GSheetsConnection)
    # Read data from the "getquin" worksheet; adjust ttl or worksheet name as needed
    data = conn.read(worksheet='getquin', ttl=5)
    return data

# Function to convert URLs (or text) in a column to clickable links
def make_clickable(url):
    return f'<a href="{url}" target="_blank">{url}</a>'

# Load the data from your Google Sheet
df = load_gsheet_data()

# OPTIONAL: If you need to transform a specific column into clickable links,
# uncomment and adjust the column name below. 
# For example, if your sheet has a column named 'Performance':
df['Performance'] = df['Performance'].apply(make_clickable)

# Create custom CSS for left alignment and general styling
custom_css = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        text-align: left !important;
        padding: 8px;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
    }
</style>
"""

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Convert DataFrame to HTML (allowing clickable links) and display
st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
