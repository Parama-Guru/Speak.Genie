from setuptools import find_packages, setup

setup(
    name="multilingual assistant",
    version="0.0.1",
    author="paramaguru",
    author_email="paramaguruvh@gmail.com",
    packages=find_packages(),
    install_requires=["SpeechRecognition","pipwin","pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"]

)