import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Initialize connection to Google Sheets
conn = st.connection('gsheets', type=GSheetsConnection)

try:
    # Read data from the Google Sheet
    data = conn.read(worksheet='getquin', ttl=5)
    st.dataframe(data)
except Exception as e:
    st.error(f"An error occurred: {e}")
