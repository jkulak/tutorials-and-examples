import langchain_helper as lch
import streamlit as st

LOGO_IMAGE_PATH = "app/static/logo.png"
LOGO_IMAGE_WIDTH = 100

st.image(
    LOGO_IMAGE_PATH,
    width=LOGO_IMAGE_WIDTH,
)

st.title("Get insights from your data")
st.write("This app will help you to get insights from your data.")

director_name = st.chat_input("What do you want to know?")

if director_name:
    title = lch.generate_movie_title(name=director_name)
    st.write(title)
