import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    email_box = st.text_input("Enter your Email here")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        print(button)