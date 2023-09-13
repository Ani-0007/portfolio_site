import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    email_box = st.text_input("Enter your Email here")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New mail form {email_box}

From: {email_box}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Your email is sent successfully!!")