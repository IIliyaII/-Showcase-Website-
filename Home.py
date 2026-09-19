import streamlit as st
import pandas
import os



st.set_page_config(layout="wide")

column1, column2= st.columns(2)

with column1:
    st.image('images/GitHub-logo.png')

with column2:
    st.title(f"Hello , I am Iliya! \n")
    st.info(f" Computer Engineering student, an aspiring back-end developer, and a cybersecurity enthusiast.\n"
                f"Here, you can explore some of my projects and their GitHub repositories.")

df=pandas.read_csv("images/data.csv",sep=";")
column3 ,empty_column, column4 = st.columns([1.5,0.5,1.5])
with column3:

        for index, row in df[:10].iterrows():
            st.header(row['title'])
            st.image(f"images/{row['image']}")
            st.info(row['description'])
            st.write(f"[Source code]({row['url']})")
with column4:


        for index, row in df[10:].iterrows():
            st.header(row['title'])
            st.image(f"images/{row['image']}")
            st.info(row['description'])
            st.write(f"[Source code]({row['url']})")

