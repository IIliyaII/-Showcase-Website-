import streamlit as st
import smtplib
from email.message import EmailMessage
import os
from pathlib import Path
from dotenv import load_dotenv


st.header("Contact Me")


env_path = Path(__file__).resolve().parent.parent/ ".env"
load_dotenv(env_path)

Password = os.getenv("Password")
email = os.getenv("email")
mail= os.getenv("mail")

s = smtplib.SMTP("smtp.gmail.com", 587)

with st.form(key="contact",clear_on_submit=True):
    massage = st.text_area("Enter your message")
    name = st.text_input("Enter your name")
    user = st.text_input("Enter your email")
    submit = st.form_submit_button("Submit")


msg = EmailMessage()
msg.set_content(massage)

if submit:
    if not massage.strip() and name.strip() and user.strip() :
        st.warning("Please fill in all of the fields")

    else:
        msg['Subject'] = f"Massage from {user}"
        msg['From'] = email
        msg['To'] = mail
        msg.set_content(massage)
        try:
            s.starttls()
            s.login(email, Password)
            s.send_message(msg)
            st.success(f"Your message has been sent ")
            s.quit()

        except smtplib.SMTPException as e :
            st.error(f"An error occured while sending email")




