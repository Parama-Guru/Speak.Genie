import speech_recognition as sr # type: ignore
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts  import gTTS # type: ignore
from pydub import AudioSegment
from pydub.playback import play

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY



def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source,timeout=3, phrase_time_limit=5)
        print("Audio captured.")
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    

def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")
    # Play the text using pydub and simpleaudio
    sound = AudioSegment.from_mp3("speech.mp3")
    play(sound)

def llm_model_object(user_text):
    #model = "models/gemini-pro"
    genai.configure(api_key=GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        prompt=f'''u are a assistant to answer the question the output all must be in lower case not with bold or any styling as it will be converted into speech the output token is 100 so bee consise 
          Question:{user_text}  '''
        response = model.generate_content(prompt, generation_config=genai.GenerationConfig(
        max_output_tokens=100,
        temperature=0.5,
    ))
        result = response.text
        return result
    except TypeError as e:
        print(f"Error generating content: {e}")
    return   # or handle the error as needed
    
    
    
    