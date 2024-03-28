from SGPMain import speak,VAName
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
def shutdownPC(query):
    if 'shutdown this pc in' in query:
        time = query.split(' ')
        time = time[time.index('in')+1]
        print(f'{VAName} : Shutdown this pc in {time} second')
        speak(f'shutdown this pc in {time} second')
        os.system(f'shutdown /s /t {time} /c "Shutdown This PC in {time} Second"')

    elif 'force shutdown ths pc' in query:
        time = query.split(' ')
        time = time[time.index('in')+1]
        print(f'{VAName} : Force Shutdown this pc in {time} second')
        speak(f'force shutdown this pc in {time} second')
        os.system(f'shutdown /s /f /t {time} /c "Shutdown This PC in {time} Second"')


#==========================================================================================================
        
if __name__ == '__main__':
    # This is only example
    query = 'open chrome' #takeCommand().lower()
    openApp(query)
    pyautogui.sleep(2)
    query = 'close chrome'
    closeApp(query)
