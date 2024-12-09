import streamlit as st

def submitted():
    st.title("Thank You for Voting!")
    st.markdown(
        """
        Thank you for casting your votes. Your votes have been successfully submitted.
        
        Please wait while the results are being compiled. The results will be declared soon.
        """
    )
    st.info("We'll notify you once the results are ready!")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

if st.session_state["logged_in"] == True:
    if st.session_state["submitted"] == True:
        submitted()
    else:
        st.write("Please Submit your project and votes first")
else:
    st.switch_page("pages/login.py")
