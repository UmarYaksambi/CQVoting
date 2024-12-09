import streamlit as st
from time import sleep
from st_pages import hide_pages

# Hide the login page in the sidebar
hide_pages(["login"])

# Function to handle login logic
def check_login(username, password):
    # Replace this logic with actual user authentication (e.g., database check)
    return username == "user" and password == "password"

# Streamlit UI
st.title("Login Page")

# Input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Handling login button click
if st.button("Login"):
    if check_login(username, password):
        # Set session state for login
        st.session_state["logged_in"] = True
        st.success("Logged in successfully!")
        sleep(1)
        st.switch_page("pages/project.py")  # Switch to the project page
    else:
        st.error("Invalid credentials!")

# Check if user is logged in and provide log out option
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    if st.button("Log out"):
        st.session_state["logged_in"] = False
        st.success("Logged out!")
        sleep(0.5)
        st.switch_page("login")  # Redirect to login page after log out
