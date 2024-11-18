import streamlit as st
from gtts import gTTS
from langs import _langs

st.title("Simple Text-to-Speech App 🗣️")

input_placeholder = st.empty()
output_placeholder = st.empty()

# initiate session state variable
if "output_audio" not in st.session_state:
    st.session_state['output_audio'] = None
if "status_message" not in st.session_state:
    st.session_state['status_message'] = None

def convert():
    try:
        text = st.session_state['text_input']
        lang = st.session_state['lang_input']

        if not text.strip():
            st.session_state['status message'] = "Please enter some text! 🙏"

        with output_placeholder.container():
            with st.spinner("Converting... 🔄"):
                tts = gTTS(text, lang=lang)
                audio_file = "output.mp3"
                tts.save(audio_file)

                st.session_state['output_audio'] = audio_file
                st.session_state['status_message'] = "Completed! ✅"
    except Exception as e:
        st.session_state['status_message'] = f"An error occurred 💢: {e}"

with input_placeholder.container():
    lang = st.selectbox("Select Language", _langs.keys(), key="lang_input", index=25)
    text = st.text_area(label="Text Input", key="text_input", value="", placeholder="Enter your text here... 📝", height=200)
    btn = st.button("Convert", on_click=convert)

with output_placeholder.container():
    if st.session_state['status_message']:
        st.write(st.session_state['status_message'])
    if st.session_state['output_audio']:
        st.audio(st.session_state['output_audio'], format="audio/mp3", autoplay=True)
        with open(st.session_state['output_audio'], "rb") as f:
            st.download_button(label="Download Audio", data=f, file_name="output.mp3", mime="audio/mp3")

st.caption("Made with ❤️ by [damarss](https://github.com/damarss/simple-tts)")
