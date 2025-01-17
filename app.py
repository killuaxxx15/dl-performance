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

def format_performance(row):
    """
    If the 'Port' column is 'CASH', format the 'Performance' value as a number
    with thousands separator and 2 decimals.
    Otherwise, convert it to a clickable link.
    """
    port_value = row.get('Port', None)           # Safely fetch the 'Port' column
    performance_value = row.get('Performance', None)
    
    # Check if performance_value is numeric or string:
    # (Assuming 'Performance' is numeric if Port == 'CASH')
    if port_value == 'CASH':
        # Safely convert to float and format with thousands separator, 2 decimals
        try:
            numeric_val = float(performance_value)
            return f"{numeric_val:,.2f}"
        except:
            # If conversion fails, return the raw value
            return performance_value 
    else:
        # Make it a clickable link
        return f'<a href="{performance_value}" target="_blank">{performance_value}</a>'

# Load the data from your Google Sheet
df = load_gsheet_data()

# Apply conditional formatting to the 'Performance' column
if 'Port' in df.columns and 'Performance' in df.columns:
    df['Performance'] = df.apply(format_performance, axis=1)

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
