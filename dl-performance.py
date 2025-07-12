import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title='Portfolio', page_icon=':bar_chart:')

# Display header for the dashboard
st.header('Portfolio Performance')

# Display the last update date
st.markdown('##### Updated: 12/07/2025')

portfolios = ["TAA_AlvaroSleeve", "TAA_1", "TAA_Aggregate"]

selected_portfolio = st.selectbox('Select Portfolio', portfolios, index=0)

st.subheader('Portfolio Performance Analysis')
st.image(f'fig1_{selected_portfolio}.png', use_container_width=True)

st.subheader('Portfolio Metrics & Analysis')
st.image(f'fig2_{selected_portfolio}.png', use_container_width=True)
st.image(f'fig3_{selected_portfolio}.png', use_container_width=True)

st.subheader('Portfolio Exposure Analysis')
st.image(f'fig4_{selected_portfolio}.png', use_container_width=True)

