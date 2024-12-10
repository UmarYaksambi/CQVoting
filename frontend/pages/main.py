import streamlit as st
import requests
from time import sleep
from streamlit_cookies_manager import EncryptedCookieManager
import os
from dotenv import load_dotenv

# Load environment variables for cookie password
load_dotenv(dotenv_path='../.env')

# Retrieve the cookie password from the environment
password = os.getenv("CQVOTING_COOKIE_PASSWORD")

if password is None:
    st.error("The 'CQVOTING_COOKIE_PASSWORD' environment variable is not set.")
    st.stop()

# Initialize cookie manager
cookies = EncryptedCookieManager(prefix="cqvoting", password=password)

# Ensure cookies are ready
if not cookies.ready():
    st.stop()

# Function to calculate the quadratic cost for a vote incrementally
def quadratic_cost(votes):
    return sum(i ** 2 for i in range(1, votes + 1))

# Fetch project details from backend
try:
    response = requests.get("http://localhost:8080/projects")
    response.raise_for_status()
    projects = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Unable to fetch project details: {e}")
    projects = []

# Set up the page layout
# st.set_page_config(page_title="CQVoting/Vote", layout="wide", page_icon="🚀")

def main():
    # Main title
    st.title("Collaborative Quadratic Voting 🗳️")

    # Layout: Main content and sidebar
    col1, col2 = st.columns([3, 1.1])

    with col2:
        # Display Credits Information
        st.markdown("## Your Credits 💰")
        credits = cookies.get("credits", 100)  # Default to 100 credits if not available
        st.metric(label="Credits Remaining", value=credits)
        st.markdown("---")

        # About Quadratic Voting
        st.markdown("### About Quadratic Voting 📜")
        st.markdown(
            """
            Each participant starts with **100 credits**. Voting works as follows:
            - **1 vote** costs **1 credit**.
            - **2 votes** cost **4 credits** (1 + 4 = 5 total).
            - **3 votes** cost **9 credits** (1 + 4 + 9 = 14 total).
            
            Cumulative costs apply only to votes for the same project, encouraging expression of preference.
            """
        )

        # Voting Instructions
        st.markdown("### Instructions ✅")
        st.markdown(
            """
            - Review each project's details before voting.
            - Allocate credits based on genuine preference and project value.
            - Vote fairly and strategically—this ensures the best projects get recognized.
            """
        )
        st.markdown("---")

    # Main content area for projects
    with col1:
        total_cost = 0  # Initialize total cost outside the loop to track total votes' cost

        # If votes are not stored in cookies, initialize them as an empty dictionary
        votes = cookies.get("votes", {})

        for project in projects:
            with st.expander(f"Project: {project['name']} 📌", expanded=True):
                col1_1, col1_2 = st.columns([1, 3])  # Two-column layout for project image and details

                with col1_1:
                    # Safely access and display preview image
                    preview_image = project.get('preview_image_url', '')
                    if preview_image:
                        st.image(preview_image, width=200)
                    else:
                        st.write("No image available")

                with col1_2:
                    # Project description
                    st.markdown(f"### Description: \n{project['description']}")

                    # Display links to GitHub and YouTube if available
                    st.markdown(f"[GitHub Link]({project['github_url']})")

                    youtube_link = project.get('youtube_url', '')  # Safely access youtube_link
                    if youtube_link:
                        st.markdown(f"[YouTube Link]({youtube_link})")
                    else:
                        st.markdown("No YouTube link available")

                    # Display README content
                    st.markdown("#### README 📖")
                    # Generate a unique key for each readme using either project['id'] or fallback to the loop index if id is None
                    unique_readme_key = f"readme_{project['id']}" if project['id'] else f"readme_{projects.index(project)}"
                    st.text_area("README FROM GITHUB", value=project["readme_content"], height=300, disabled=True, key=unique_readme_key)

                    # Ensure a unique key for each number_input element
                    unique_vote_key = f"vote_{project['id']}" if project['id'] else f"vote_{projects.index(project)}"
                    project_votes = st.number_input(f"Votes for {project['name']}", min_value=0, step=1, key=unique_vote_key)

                    # Update the votes dictionary
                    votes[project["id"]] = project_votes

                    # Calculate the total cost for this project's votes and add to the global total cost
                    total_cost += quadratic_cost(project_votes)

        # Update credits in cookies after calculating the total cost
        cookies["credits"] = max(0, 100 - total_cost)
        cookies["votes"] = votes  # Store the updated votes dictionary
        cookies.save()  # Save the changes to cookies

    # Display the Submit button and submit votes if clicked
    st.markdown("### 🗳️ Submit Your Votes")
    if st.button("Submit Votes"):
        if cookies["credits"] >= 0:
            try:
                # Submit the votes to the backend
                response = requests.post("http://localhost:8080/submit-votes", json={"votes": cookies["votes"]})
                response.raise_for_status()  # Ensure a successful response

                cookies["submitted"] = True  # Mark as submitted
                cookies.save()  # Save the submission status in cookies
                st.success("Votes submitted successfully! 🎉")
                sleep(1)  # Add delay before navigating to the next page
                st.switch_page("pages/submitted.py")

            except requests.exceptions.RequestException as e:
                st.error(f"Error submitting votes: {e}")
        else:
            st.error("Not enough credits to submit votes!")

    # Footer with additional information
    st.markdown("---")
    st.markdown("📢 **Quadratic Voting** is a fair voting method for allocating limited resources to the projects you care about.")

# Handle login check
if "logged_in" in cookies and cookies["logged_in"]:
    main()
else:
    st.switch_page("pages/login.py")
