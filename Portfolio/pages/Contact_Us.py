import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        with_subject = f"""
        Subject: New email from {user_email}
        {message}
        """
        send_email(with_subject)
        st.info("Your email was sent successfully")

