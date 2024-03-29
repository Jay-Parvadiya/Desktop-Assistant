from SGPMain import speak,VAName,takeCommand
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
    
    elif 'open voice typing' in query:
        print(f'{VAName} : Opening Voice typing')
        speak('Opening voice typing')
        pyautogui.hotkey('win','h')

    elif 'open clipboard' in query:
        print(f'{VAName} : Opening Clipboard')
        speak('Opening Clipboard')
        pyautogui.hotkey('win','v')

    else:
        app_name = query.split(' ')
        try:
             
            app_name = app_name[app_name.index('open') + 1]
        except Exception as e:
             print(f"{VAName} : No application name provided")
             speak(f" something wrong ") 
             
        print(f'{VAName} : Opening {app_name}')
        speak(f"Opening {app_name}")
        #try:
            #os.system(f'start {app_name}')
        #except Exception as e:
        pyautogui.press('win')
            
        if len(app_name)>0 :
                pyautogui.typewrite(app_name)
                pyautogui.sleep(0.5)
                pyautogui.press('enter')
        else:
                print(f"{VAName} : No application name provided")
                speak(f" something wrong ")
#==========================================================================================================
def closeApp(query):
    
    if 'close current app' in query:
        print(f'{VAName} : closing ')
        speak('closing')
        pyautogui.hotkey('alt','f4')
    else:
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
def whatsappTask(query):
    if "open whatsapp and send message to" in query:  # This is use for massage anyone on whatsapp only # This only work when whatsapp is off and video call or voice call is off
        array = query.split()
        input_name = array[array.index('open') + 1] # This is use for take name of person for massage
        print(f"{VAName} : Opening {input_name}")
        speak(f"Opening {input_name}")
 
        pyautogui.keyDown('win')
        pyautogui.press('q')
        pyautogui.keyUp('win')
 
        if len(input_name)>0 :
                pyautogui.sleep(2)
                pyautogui.typewrite(input_name)
                pyautogui.press('enter')
        else:
            print(f"{VAName} : No application name provided")
        pyautogui.sleep(3)
 
        input_name = array[array.index('to') + 1]
        pyautogui.typewrite(f'{input_name}')
        pyautogui.press('enter')
        pyautogui.sleep(3)
       
        print(f'{VAName} : what you whant to send')
        speak('what you whant to send')
        query = takeCommand().lower()
       
        if query == 'none':
                print(f'{VAName} : Massage not given')
        else:
                pyautogui.typewrite(query)
                print(f'{VAName} : sending {query}')
                speak(f'sending {query}')
                pyautogui.press('enter') 

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
