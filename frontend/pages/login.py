import streamlit as st
from time import sleep
from streamlit_cookies_manager import EncryptedCookieManager
import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from the .env file
load_dotenv(dotenv_path='../.env')

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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
def check_login(user_id, password_input):
    # Query Supabase to check if the user_id exists in the 'users' table
    response = supabase.table("users").select("user_id", "password").eq("user_id", user_id).execute()

    if len(response.data) > 0:
        # Assuming the password is stored as plaintext in the 'password' field (for demo purposes)
        user = response.data[0]
        stored_password = user["password"]

        # Check if the provided password matches the stored password
        if password_input == stored_password:    # Demo purpose, avoid in production
            return True  # Password matches, login successful
        else:
            return False  # Incorrect password
    else:
        # User not found
        return False

# Streamlit UI for login
st.title("Login Page")

# Input fields for user ID and password
user_id = st.text_input("User ID")
password_input = st.text_input("Password", type="password")

# Handling login button click
if st.button("Login"):
    if user_id.strip() == "":
        st.error("User ID cannot be empty!")
    elif check_login(user_id, password_input):
        # Set login state in cookies
        cookies["logged_in"] = "true"
        cookies["user_id"] = user_id
        cookies.save()  # Save the cookies
        print(f"Logged in {user_id}")
        st.success("Logged in successfully!")

        # Retrieve username after login
        response = supabase.table("users").select("username").eq("user_id", user_id).execute()

        # Retrieve username directly without error handling
        if len(response.data) > 0:
            username = response.data[0]["username"]
            st.success(f"Welcome, {username}!")
        else:
            st.error("No user found with the provided user_id.")

        # Redirect to the project page
        st.experimental_rerun()
    else:
        st.error("Invalid credentials!")

# Check if user is logged in using cookies
logged_in = cookies.get("logged_in", "false") == "true"

if logged_in:
    user_id = cookies.get('user_id')

    # Check for empty user_id
    if user_id.strip() == "":
        st.error("User ID is missing!")
    else:
        # Retrieve username after login without error handling
        response = supabase.table("users").select("username").eq("user_id", user_id).execute()

        # Directly retrieve the username
        if len(response.data) > 0:
            username = response.data[0]["username"]
            st.success(f"Welcome back, {username}!")
        else:
            st.error("No user found with the provided user_id.")

    if st.button("Log out"):
        # Clear the login state from cookies
        cookies["logged_in"] = "false"
        cookies["user_id"] = ""
        cookies.save()  # Save the cleared cookies
        st.success("Logged out!")
        sleep(0.5)
        st.switch_page("pages/login.py")
