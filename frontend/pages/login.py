import streamlit as st
from time import sleep
from streamlit_cookies_manager import EncryptedCookieManager
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv(dotenv_path='../.env')

# Get the password from the environment variable
password = os.getenv("CQVOTING_COOKIE_PASSWORD")

# Ensure the password is loaded correctly
if password is None:
    st.error("The 'CQVOTING_COOKIE_PASSWORD' environment variable is not set.")
    st.stop()

# Initialize the cookie manager with the correct password
cookies = EncryptedCookieManager(prefix="cqvoting", password=password)

# Ensure the cookie manager is ready
if not cookies.ready():
    st.stop()

# Function to handle login logic
def check_login(username, password):
    # Replace this logic with actual user authentication (e.g., database check)
    return username == "user" and password == "password"

# Streamlit UI for login
st.title("Login Page")

# Input fields for username and password
username = st.text_input("Username")
password_input = st.text_input("Password", type="password")

# Handling login button click
if st.button("Login"):
    if check_login(username, password_input):
        # Set login state in cookies
        cookies["logged_in"] = "true"
        cookies["username"] = username
        cookies.save()  # Save the cookies
        st.success("Logged in successfully!")
        st.switch_page("pages/project.py")
    else:
        st.error("Invalid credentials!")

# Check if user is logged in using cookies
logged_in = cookies.get("logged_in", "false") == "true"

if logged_in:
    st.success(f"Welcome, {cookies.get('username')}!")
    if st.button("Log out"):
        # Clear the login state from cookies
        cookies["logged_in"] = "false"
        cookies["username"] = ""
        cookies.save()  # Save the cleared cookies
        st.success("Logged out!")
        sleep(0.5)
        st.switch_page("pages/login.py")
