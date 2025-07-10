import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Portfolio', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Portfolio Performance')

# Display the last update date
st.markdown('#### Updated: 10/07/2025')

st.subheader('Portfolio Performance Analysis')
st.image('fig1_perf.png', use_container_width=True)

st.subheader('Portfolio Metrics & Analysis')
st.image('fig2_perf.png', use_container_width=True)
st.image('fig3_perf.png', use_container_width=True)

st.subheader('Portfolio Exposure Analysis')
st.image('fig4_perf.png', use_container_width=True)

