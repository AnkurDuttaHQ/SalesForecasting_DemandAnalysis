import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 Sales Forecasting & Demand Intelligence Dashboard")

st.markdown("""
## Welcome 👋

This dashboard contains:

- 📊 Sales Overview
- 🔮 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments

Use the **sidebar** to navigate between pages.
""")