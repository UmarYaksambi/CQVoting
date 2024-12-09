import streamlit as st
import requests
from time import sleep

def main():
    # Initialize session state
    if "credits" not in st.session_state:
        st.session_state["credits"] = 100
    if "votes" not in st.session_state:
        st.session_state["votes"] = {}

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
    st.set_page_config(page_title="CQVoting", layout="wide", page_icon="🚀")

    # Main title
    st.title("Collaborative Quadratic Voting 🗳️")

    # Layout: Main content and sidebar
    col1, col2 = st.columns([3, 1.1])

    with col2:
        # Display Credits Information
        st.markdown("## Your Credits 💰")
        st.metric(label="Credits Remaining", value=st.session_state["credits"])
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
        for project in projects:
            st.write(f"### {project['name']} 📌")
            st.image(project["image_url"], width=200)
            st.write(project["description"])
            st.markdown(f"[GitHub Link]({project['github_url']})")

            # Number input for votes
            votes = st.number_input(f"Votes for {project['name']}", min_value=0, step=1, key=project["id"])

            # Update session state with the new vote count
            st.session_state["votes"][project["id"]] = votes

            # Calculate the total cost for this project's votes
            total_cost = 0
            for project_id, vote_count in st.session_state["votes"].items():
                total_cost += quadratic_cost(vote_count)

            # Update credits by deducting the total cost from 100
            st.session_state["credits"] = max(0, 100 - total_cost)

    st.markdown("### 🗳️ Submit Your Votes")
    if st.button("Submit Votes"):
        if st.session_state["credits"] >= 0:
            try:
                response = requests.post("http://localhost:8080/submit-votes", json={"votes": st.session_state["votes"]})
                response.raise_for_status()
                st.session_state["submitted"] = True
                st.success("Votes submitted successfully! 🎉")
                sleep(1)
                st.switch_page("pages/submitted.py")

            except requests.exceptions.RequestException as e:
                st.error(f"Error submitting votes: {e}")
        else:
            st.error("Not enough credits to submit votes!")

    # Footer
    st.markdown("---")
    st.markdown("📢 **Quadratic Voting** is a fair voting method for allocating limited resources to the projects you care about.")


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"] == True:
    main()
else:
    st.switch_page("pages/login.py")