import streamlit as st
from gtts import gTTS

st.title("Text-to-Speech Simple App")

text = st.text_area(label="Text Input", value="", placeholder="Enter your text here")

def convert():
    tts = gTTS(text, lang="id")
    tts.save("output.mp3")
    print(btn)

btn = st.button("Convert", on_click=convert)

if btn:
    st.audio("output.mp3")