import streamlit as st
from streamlit_gsheets import GSheetsConnection
import logging

# Initialize connection to Google Sheets
conn = st.connection('gsheets', type=GSheetsConnection)

logging.basicConfig(level=logging.DEBUG)

try:
    # Attempt to read the worksheet
    data = conn.read(worksheet='getquin', ttl=5)
    st.dataframe(data)
except Exception as e:
    st.error(f"An error occurred: {e}")
    logging.exception("Debugging error with GSheets connection.")
