import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="user_email"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Enter your message")
    message = f"""\
Subject: New Email from {user_email}
            
From: {user_email}
{raw_message}
  """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your Email was sent")
