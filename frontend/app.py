# app.py
import streamlit as st

# Use Streamlit's multi-page functionality
st.set_page_config(page_title="CQVoting", layout="wide", page_icon="🚀")

# Sidebar for page navigation
page = st.sidebar.selectbox("Select a page", ["Your Project", "Vote", "Submitted"])

if page == "Login":
    import pages.login
elif page == "Your Project":
    import pages.project
elif page == "Vote":
    import pages.main
elif page == "Submitted":
    import pages.submitted
