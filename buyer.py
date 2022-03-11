import keyboard
import pyautogui
import random
import time
from tkinter import messagebox

buy_button = { "x":2088, "y":1232}
item = { "x":954, "y":442 }
add = { "x":1376, "y":692}
price = { "x":1356, "y":744 } 
buy_final = { "x":1281, "y":1082 }
confirm = { "x":1280, "y":780 }
move_left = { "x":11, "y":579 }
move_right = { "x":2540, "y":887 }
minutes = 5
seconds = 60*minutes

def clic(position, times):
    pyautogui.moveTo(position["x"], position["y"],duration=0.1, tween=pyautogui.easeInOutQuad)
    for i in range(0, times):
        pyautogui.click()
    time.sleep(0)
    
def no_afk(mouseMove):
    if bool(random.getrandbits(1)):
        pyautogui.moveTo(move_right["x"], move_right["y"],duration=0.1, tween=pyautogui.easeInOutQuad)
    else:
        pyautogui.moveTo(move_left["x"], move_left["y"],duration=0.1, tween=pyautogui.easeInOutQuad)
    pyautogui.click(button=mouseMove)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.press('t')
    keyboard.release('t')

def buy_item(entryPrice, amount, mouseMove):
    loop = True
    start = time.time() 
    while loop:
        clic(item,2)
        clic(buy_button,1)
        clic(add,2)
        keyboard.write(str(amount))
        clic(price,2)
        keyboard.write(str(entryPrice))
        clic(buy_final,2)
        clic(confirm,2)
        timeAlive = time.time() - start
        if timeAlive >= seconds:
            no_afk(str(mouseMove))
            start = time.time()
        if keyboard.is_pressed("ctrl"):
            loop = False 
           
  
