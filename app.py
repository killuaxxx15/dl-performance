import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Initialize connection to Google Sheets
conn = st.connection('gsheets', type=GSheetsConnection)

data = conn.read(worksheet='getquin', ttl=5)

st.dataframe(data)
