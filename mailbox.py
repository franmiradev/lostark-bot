import time
from buyer import *
import keyboard
import pyautogui

def clearMail():
    loop = True
    while loop:
        mailbox = { "x":280, "y":139 }
        accept = { "x":727, "y":677 }
        delete = { "x":865, "y": 673 }
        clic(mailbox,1)
        time.sleep(0.1)
        clic(accept,1)
        time.sleep(0.1)
        clic(delete,1)
        if keyboard.is_pressed("ctrl"):
            loop = False