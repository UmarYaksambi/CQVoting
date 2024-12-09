import streamlit as st
import requests

# Initialize session state
if "credits" not in st.session_state:
    st.session_state["credits"] = 100
if "votes" not in st.session_state:
    st.session_state["votes"] = {}

# Function to calculate quadratic cost
def quadratic_cost(votes):
    return votes ** 2

# Fetch project details from backend
try:
    response = requests.get("http://localhost:8080/projects")
    response.raise_for_status()
    projects = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Unable to fetch project details: {e}")
    projects = []

# Set up the page layout
st.set_page_config(page_title="Quadratic Voting", layout="wide")

# Main title
st.title("🎉 Collaborative Quadratic Voting 🎉")

# Layout: Main content and sidebar
col1, col2 = st.columns([3, 1])

# Sidebar for credits (always visible)
with col2:
    st.markdown("## Your Credits 💰")
    st.metric(label="Credits Remaining", value=st.session_state["credits"])
    st.markdown("---")

# Main content area for projects
with col1:
    for project in projects:
        st.write(f"### {project['name']} 📌")
        st.image(project["image_url"], width=200)
        st.write(project["description"])
        st.markdown(f"[GitHub Link]({project['github_url']})")

        # Slider for votes
        votes = st.number_input(f"Votes for {project['name']}", min_value=0, step=1, key=project["id"])
        
        # Calculate credits
        st.session_state["votes"][project["id"]] = votes
        total_cost = sum(quadratic_cost(v) for v in st.session_state["votes"].values())
        st.session_state["credits"] = max(0, 100 - total_cost)

# Sticky submit button at the bottom
st.markdown("### 🗳️ Submit Your Votes")
if st.button("Submit Votes"):
    if st.session_state["credits"] >= 0:
        try:
            response = requests.post("http://localhost:8080/submit-votes", json={"votes": st.session_state["votes"]})
            response.raise_for_status()
            st.success("Votes submitted successfully! 🎉")
        except requests.exceptions.RequestException as e:
            st.error(f"Error submitting votes: {e}")
    else:
        st.error("Not enough credits to submit votes!")

# Footer
st.markdown("---")
st.markdown("📢 **Quadratic Voting** is a fair voting method for allocating limited resources to the projects you care about.")
