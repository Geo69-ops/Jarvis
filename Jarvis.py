import speech_recognition as sr
import pyttsx3

import os
import pyaudio
from dotenv import load_dotenv
load_dotenv()

keyy = "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"

# OPENAI_KEY = os.getenv('OPENAI_KEY')

OPENAI_KEY = keyy

import openai
openai.api_key = OPENAI_KEY

def SpeakText(command):
    engine= pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r= sr.Recognizer()

def record_text():
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=0.2)
                print ("i'm listening")
                
                audio2= r.listen(source)

                MyText = r.recognize_google(audio2)
                print(MyText)
                return MyText
                
            
        except sr.RequestError as e:
            print("could not request results; {0}", format(e))
        
        except sr.UnknownValueError:
            print("Unknow error ocurred")
record_text()

# def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
#     response= openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )    

#     message = response.choice[0].message.content
#     messages.append(response.choices[0].message)
#     return message

# messages= []
# while(1):
#     text = record_text()
#     messages.append({"role":"user","content": text})
#     response = send_to_chatGPT(messages)
#     SpeakText(response)

#     print(response)