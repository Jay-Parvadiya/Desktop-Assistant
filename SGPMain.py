import pyttsx3 as ptt             # This module is use for convert text-to-speech 
import datetime                   # This module is use for import date and time   
import speech_recognition as sr   # This module is use for convert spoken word into text 
import wikipedia                  # This module is use for searching and retrieving information from Wikipedia.
import webbrowser                 # This module is use for automating web browsing tasks in Python
import os                         # This module is use for for interacting with the operating system
from PIL import Image, ImageGrab  # This module is use for taking screen shot
import pyautogui         # This module is use for automate keybord and mouse with python programm
import time
import multiprocessing
from DAGUI import guiStart
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
        r.energy_threshold = 100
        audio = r.listen(source,timeout=20,phrase_time_limit=20)    # for convert voice to text
        
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

    media_control = ['incress volume', 'decress volume', 'play', 'paush', 'mute', 'play next', 'play previous']
    if 'google' in query:
        from webTask import searchGoogle
        searchGoogle(query)

    elif 'youtube' in query:
        from  webTask import searchYoutube
        searchYoutube(query)
    
    elif 'wikipedia' in query:
        from webTask import searchWikipedia
        searchWikipedia(query)
    
    elif 'open' in query:
        from DesktopTask import openApp
        openApp(query)
    
    elif 'close' in query:
        from DesktopTask import closeApp
        closeApp(query)
    
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{VAName} : the time is {strTime}")
        speak(f"the time is {strTime}")
    
    elif query in media_control:
        from keyboardTask import mediaControl
        mediaControl(query)

    elif "take a screen shot" in query:
        print(f"{VAName} Taking screen shot")
        speak("Taking screenshot")
        image  = ImageGrab.grab()
        image.show()

    elif "shutdown this pc" in query:
        from DesktopTask import shutdownPC
        shutdownPC(query)

    elif "restart this pc" in query:
        print(f'{VAName} : Restarting')
        speak('Restarting')
        os.system('shutdown /r') 

    elif 'select all' in query:
        print(f'{VAName} : selecting all')
        speak('Selecting all')
        pyautogui.hotkey('ctrl','a')
        
    elif 'copy all' in query:
        print(f'{VAName} : Coping all')
        speak('Coping all')
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.sleep(0.5)
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')

    elif 'remove all file' in query:
        print(f'{VAName} : Removing all file')
        speak('Removing all file')
        pyautogui.hotkey('ctrl','a')
        pyautogui.press('delete')

    elif 'remove all' in query:
        print(f'{VAName} : Removing all')
        speak('Removing all')
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.press('backspace')
        pyautogui.keyUp('ctrl')

    else:
        from NormalConversation import Conversetion
        Conversetion(query)
        
def inputQuery(self):
    while True:
        query = takeCommand().lower()
        Recogniting(query, VAName)
    
#===================================================================================================================================
# ------------------------------ Main part ---------------------------
VAName = "ALEX".lower()
if __name__ == '__main__':
    
    p1 = multiprocessing.Process(target=guiStart,args=(10,))
    p2 = multiprocessing.Process(target=inputQuery,args=(10,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    wishMe(VAName)
   