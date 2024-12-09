import streamlit as st
import requests

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


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"] == True:
    project_page()
else:
    st.switch_page("pages/login.py")