from SGPMain import takeCommand,speak,VAName
from pynput.keyboard import Key,Controller
import time

keyboard = Controller()

def mediaControl(query):

    # elif 'increase volume' in query:
    #     for i in range(2):
    #         keyboard.press(Key.media_volume_up)
    #         keyboard.release(Key.media_volume_up)
    #         time.sleep(0.1)
    
    # elif 'decrease volume' in query:
    #     for i in range(2):
    #         keyboard.press(Key.media_volume_down)
    #         keyboard.release(Key.media_volume_down)
    #         time.sleep(0.1)
    
    
    if 'mute' in query:
        keyboard.press(Key.media_volume_mute)
    
    elif 'play next' in query:
        keyboard.press(Key.media_next)
    
    elif 'play previous' in query:
        keyboard.press(Key.media_previous)

    elif 'play' in query or 'pause' in query:
        keyboard.press(Key.media_play_pause)