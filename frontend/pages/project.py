import streamlit as st

# Function for the project page
def project_page():
    st.title("Your Project Details")
    
    # Get the project details from the user
    project_name = st.text_input("Project Name")
    project_description = st.text_area("Project Description")
    project_image = st.file_uploader("Upload an image of your project", type=["jpg", "png", "jpeg"])
    youtube_link = st.text_input("YouTube Link")
    github_link = st.text_input("GitHub Link")

    # Check if the user has filled all fields
    if project_name and project_description and project_image and youtube_link and github_link:
        st.image(project_image, caption="Project Image", use_container_width=True)
        st.markdown(f"### YouTube Link: {youtube_link}")
        st.markdown(f"### GitHub Link: {github_link}")
        st.markdown("Please make sure your GitHub repository has a complete README file.")

        # Save the project details when submitted
        if st.button("Submit Project"):
            # Handle submission logic here (e.g., save to database or backend)
            st.success("Your project has been submitted successfully!")
    else:
        st.warning("Please fill all the fields before submitting.")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"] == True:
    project_page()
else:
    st.switch_page("pages/login.py")
