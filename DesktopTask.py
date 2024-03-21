from SGPMain import takeCommand,speak,VAName
import os
import pyautogui
from PIL import ImageGrab
#==========================================================================================================
def openApp(query):
    
    if 'open vscode' in query or 'open visual code' in query:
        print(f"{VAName} : Opening vscode")
        speak("Opening vscode")
        codepath = "C:\\Users\\JAYDP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
        os.startfile(codepath)

    elif "open settings" in query:
        print(f'{VAName} : Opening settings')
        speak('Opening settings')
        pyautogui.hotkey('win','x')
        pyautogui.sleep(0.5)
        pyautogui.press('n')  
    
    elif "open task manager" in query:
        print(f'{VAName} : Opening Task Manager')
        speak('Opening Task Manager')
        pyautogui.hotkey('win','x')
        pyautogui.sleep(0.5)
        pyautogui.press('t')
    
    elif 'oepn search' in query:
        print(f'{VAName} : Opening Search')
        speak('Opening Search')
        pyautogui.hotkey('win','x')
        pyautogui.sleep(0.5)
        pyautogui.press('s')

    elif 'open system information' in query:
        print(f'{VAName} : Opening System info')
        speak('Opening System info')
        pyautogui.hotkey('win','x')
        pyautogui.sleep(0.5)
        pyautogui.press('y')

    elif 'open clipboard' in query:
        print(f'{VAName} : Opening Clipboard')
        speak('Opening Clipboard')
        pyautogui.hotkey('win','v')

    else:
        app_name = query.split(' ')
        app_name = app_name[app_name.index('open') + 1]
        print(f'{VAName} : Opening {app_name}')
        speak(f"Opening {app_name}")
        try:
            os.system(f'start {app_name}')
        except Exception as e:
            print(f'{VAName} : {app_name} not found')
            speak(f'{app_name} not found')
            print(e)

#==========================================================================================================
def closeApp(query):
    app_name = query.split(' ')
    app_name = app_name[app_name.index('close') + 1]
    print(f'{VAName} : Closing {app_name}')
    speak(f"Closing {app_name}")
    try:
        os.system(f'taskkill /f /im {app_name}.exe')
    except Exception as e:
        print(f'{VAName} : {app_name} not found')
        speak(f'{app_name} not found')
        print(e)

#==========================================================================================================
def dTask(query):
    
    if "take a screen shot" in query:
        print(f"{VAName} Taking screen shot")
        speak("Taking screenshot")
        image  = ImageGrab.grab()
        image.show()

    elif "shutdown my pc" in query:
        print(f'{VAName} : Shuting down')
        speak('shutting down')
        pyautogui.hotkey('win','x')
        pyautogui.press('U',2)  

    elif "restart my pc" in query:
        print(f'{VAName} : Restarting')
        speak('Restarting')
        pyautogui.hotkey('win','x')
        pyautogui.press('u')   
        pyautogui.press('r') 

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

#==========================================================================================================
        
if __name__ == '__main__':
    # This is only example
    query = 'open chrome' #takeCommand().lower()
    openApp(query)
    pyautogui.sleep(2)
    query = 'close chrome'
    closeApp(query)
