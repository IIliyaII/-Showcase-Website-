import streamlit as st

column1, column2 = st.columns(2)

with column1:
    st.image('images/GitHub-logo.png')

with column2:
    st.title(f"Hello, World!\n"
                f"I am Iliya, a Computer Engineering student, an aspiring back-end developer, and a cybersecurity enthusiast.\n"
                f"Here, you can explore some of my projects and their GitHub repositories.")