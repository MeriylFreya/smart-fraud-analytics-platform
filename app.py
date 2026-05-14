import streamlit as st

st.set_page_config(
    page_title="Fraud Operations Dashboard",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Fraud Operations Dashboard")

st.markdown("""
Welcome to the AI-powered fraud detection and risk intelligence dashboard.

Use the sidebar to navigate between:
- Overview Analytics
- Transaction Explorer
- SHAP Explainability
""")