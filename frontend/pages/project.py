import streamlit as st
import requests
from time import sleep
from streamlit_cookies_manager import EncryptedCookieManager
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the password from environment variable
password = os.getenv("CQVOTING_COOKIE_PASSWORD")

# Check if password is not set
if password is None:
    st.error("The 'CQVOTING_COOKIE_PASSWORD' environment variable is not set.")
    st.stop()  # Stop further execution if the password is missing

# Initialize EncryptedCookieManager with the password
cookies = EncryptedCookieManager(prefix="cqvoting", password=password)

# Check if cookies are ready
if not cookies.ready():
    st.stop()  # Stop if cookies are not ready

BACKEND_URL = "http://localhost:8080"

# Function for the project page
def project_page():
    st.title("Your Project Details")

    # Get the project details from the user
    project_name = st.text_input("Project Name")
    project_description = st.text_area("Project Description")
    github_link = st.text_input("GitHub Repository URL")
    youtube_link = st.text_input("YouTube Link (optional)")

    if project_name and project_description and github_link:
        st.markdown(f"### YouTube Link: {youtube_link}")
        st.markdown(f"### GitHub Link: {github_link}")

        if st.button("Submit Project"):
            # Generate a unique ID for the project
            project_id = len(requests.get(f"{BACKEND_URL}/projects").json()) + 1

            # Prepare the request payload
            data = {
                "id": project_id,
                "name": project_name,
                "description": project_description,
                "github_url": github_link,
                "youtube_url": youtube_link,
            }

            # Send the data to the backend
            response = requests.post(f"{BACKEND_URL}/projects", json=data)
            if response.status_code == 200:
                project = response.json()
                st.success("Your project has been submitted successfully!")
                # Display the preview image and README content
                if project.get("preview_image_url"):
                    st.image(project["preview_image_url"], caption="GitHub Social Preview", use_container_width=True)
                if project.get("readme_content"):
                    st.markdown("### README Content")
                    st.text(project["readme_content"])
                if project.get("main_code_file"):
                    st.markdown("### Main Code File (main.py)")
                    st.code(project["main_code_file"], language='python')
            else:
                st.error(f"Error submitting project: {response.json().get('detail', 'Unknown error')}")
    else:
        st.warning("Please fill all the fields before submitting.")

# Check if user is logged in
if "logged_in" in cookies and cookies["logged_in"]:
    project_page()
else:
    # Redirect to the login page if the user is not logged in
    st.warning("You must be logged in to access this page.")
    sleep(1)
    st.switch_page("pages/login.py")
