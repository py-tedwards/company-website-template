import streamlit as st
import pandas
import emailbutton

st.header("Get in touch")

dropdown_topics = pandas.read_csv("topics.csv")


with st.form(key='form'):
    user_email = st.text_input("Enter your email")
    user_topic = st.selectbox("Enter topic to discuss", dropdown_topics)
    user_subject = st.text_input("Enter subject")
    user_message = st.text_area("Enter message")
    button = st.form_submit_button("Submit")

message = f"""\
Subject: {user_subject}

from: {user_email}
topic: {user_topic}
{user_message}
"""

if button:
    emailbutton.email_me(message)

