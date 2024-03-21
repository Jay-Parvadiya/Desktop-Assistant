from SGPMain import takeCommand,speak,VAName
from pynput.keyboard import Key,Controller
from time import sleep

keyboard = Controller()

def mediaControl(query):

    if 'incress volume' in query:
        for i in range(2):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            sleep(0.1)
    
    elif 'decress volume' in query:
        for i in range(2):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            sleep(0.1)
    
    elif 'play' in query or 'paush' in query:
        keyboard.press(Key.media_play_pause)
    
    elif 'mute' in query:
        keyboard.press(Key.media_volume_mute)
    
    elif 'play next' in query:
        keyboard.press(Key.media_next)
    
    elif 'play previous' in query:
        keyboard.press(Key.media_previous)
