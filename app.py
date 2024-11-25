import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech
import pyttsx3 # type: ignore
import os
import atexit


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted.")
    else:
        print(f"{filename} not found.")

# Register the cleanup function with atexit
atexit.register(delete_file, "speech.mp3")
def main():
    st.title("Voice Assistant")
    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            if text:  # Ensure text is not None or empty
                response = llm_model_object(text)
                if response:  # Ensure response is not None or empty
                    text_to_speech(response)
                    
                    audio_file = open("speech.mp3", "rb")
                    audio_bytes = audio_file.read()
                    
                    st.text_area(label="Response:", value=response, height=350)
                    st.audio(audio_bytes)
                    st.download_button(label="Download Speech",
                                       data=audio_bytes,
                                       file_name="speech.mp3",
                                       mime="audio/mp3")
                    

                else:
                    st.error("Failed to get a response from the model.")
            else:
                st.error("Failed to capture voice input.")
            
if __name__ == '__main__':
    main()