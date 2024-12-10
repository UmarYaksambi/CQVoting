import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import os
from time import sleep
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='../.env')
print(os.getenv("CQVOTING_COOKIE_PASSWORD"))
# Retrieve the cookie password from the environment
password = os.getenv("CQVOTING_COOKIE_PASSWORD")  # Make sure this is set in your .env file

if password is None:
    st.error("The 'CQVOTING_COOKIE_PASSWORD' environment variable is not set.")
    st.stop()

# Initialize the cookie manager
cookies = EncryptedCookieManager(prefix="cqvoting", password=password)

# Ensure cookies are ready
if not cookies.ready():
    st.stop()

# Set page config
# st.set_page_config(page_title="CQVoting/Results", layout="wide", page_icon="🚀")

# Function to display the submission confirmation
def submitted():
    st.title("Thank You for Voting!")
    st.markdown(
        """
        Thank you for casting your votes. Your votes have been successfully submitted.
        
        Please wait while the results are being compiled. The results will be declared soon.
        """
    )
    st.info("We'll notify you once the results are ready!")

# Check if user is logged in and whether the project has been submitted
if "logged_in" in cookies and cookies["logged_in"]:
    if "submitted" in cookies and cookies["submitted"]:
        submitted()
    else:
        st.write("Please Submit your project and votes first.")
else:
    # Redirect to the login page if the user is not logged in
    st.warning("You must be logged in to view this page.")
    sleep(1)
    st.switch_page("pages/login.py")
