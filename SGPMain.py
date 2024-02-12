import pyttsx3 as ptt             # This module is use for convert text-to-speech 
import datetime                   # This module is use for import date and time   
import speech_recognition as sr   # This module is use for convert spoken word into text 
import wikipedia                  # This module is use for searching and retrieving information from Wikipedia.
import webbrowser                 # This module is use for automating web browsing tasks in Python
import os                         # This module is use for for interacting with the operating system
from PIL import Image, ImageGrab  # This module is use for taking screen shot
import pyautogui as pauto         # This module is use for automate keybord and mouse with python programm
import time
#===================================================================================================================================

engine = ptt.init('sapi5')  # Make instence of pyttsx3 module 
voices = engine.getProperty('voices')   # Get voice from system 
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)   # Set voice 

#===================================================================================================================================
# This function speak given audio string 
def speak(audio):
    engine.say(audio)   # use for speak given string
    engine.runAndWait() # Run and wait for outpout

#===================================================================================================================================
# It's wish base on time 
def wishMe(VAName):
    hour = int(datetime.datetime.now().hour)    # Get current hour from date and time moudle
    if hour >= 0 and hour < 12:
        speak("good Morning sir")
    elif hour >= 12 and hour <18:
        speak("good Afternoon sir")
    elif hour >= 18 and hour <= 24:
        speak("Good evening sir")

    speak(f"I am {VAName}, How can i help you?")

#===================================================================================================================================
# It's take microphone input from the user and return output
def takeCommand():
    
    r = sr.Recognizer() # Create instence of speech_recognintion 

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        # r.energy_threshold = 100
        audio = r.listen(source,timeout=60,phrase_time_limit=60)    # for convert voice to text
        

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio)   
        print(f"User said : {query}\n")

    except Exception as e :
        print(e)
        print("Say that again please.")
        print("Somthing want's wrong.")
        speak("Please say that again.")
        return "None"
    
    engine.runAndWait()
    return query 

#===================================================================================================================================
def Recogniting(query, VAName):
    if "wikipedia" in query:
        print(f"{VAName} : Serching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,2)
        print(results)
        speak(f"Accoding to wikipedia {results}")
    
    elif "open youtube" in query:
        print(f"{VAName} : Opening youtube")
        speak("Opening youtube")
        webbrowser.open('http://www.youtube.com')

    elif "open google" in query:
        print(f"{VAName} : Opening google")
        speak("Opening google")
        webbrowser.open('http://www.google.com')
    
    elif "open brave" in query:
        print(f"{VAName} : Opening brave")
        speak("Opening brave")
        webbrowser.open('http://www.brave.com')
#===================================================================================================================================
# ------------------------------ Main part ---------------------------
if __name__ == '__main__':
    VAName = "RDX".lower()
    wishMe(VAName)
    query = takeCommand().lower()
    Recogniting(query, VAName)
    
