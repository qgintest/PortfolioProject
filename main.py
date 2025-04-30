import streamlit as st

st.set_page_config(layout="centered")

col1, col2= st.columns(2)


with col1:
    st.image("images/photo.png")

with col2:
    st.title("Abe Endale")
    contents = """
        My name is Abe, I am a Father, Educator, QA Tester, Real Estate Agent, and Crossfit Enthusiast
         practicing on developing small apps as part of my long 
        term effort to break into the pentesting/ethical hacking world
    """

    st.info(contents)

st.write("Please see some apps below I have developed in Python to help keep your systems and devices safe")