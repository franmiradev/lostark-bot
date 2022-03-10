import keyboard
import pyautogui
import random
import time
from tkinter import messagebox

buy_button_x = 2088
buy_button_y = 1232
item_x = 954
item_y = 442
add_x = 1376
add_y = 692
price_x = 1356 
price_y = 744
buy_final_x = 1281
buy_final_y = 1082
confirm_x = 1280
confirm_y = 780
move_left_x = 11
move_left_y = 579
move_right_x = 2540
move_right_y = 887
minutes = 5
seconds = 2*minutes

def clic(x,y,times):
    pyautogui.moveTo(x, y,duration=0.1, tween=pyautogui.easeInOutQuad)
    for i in range(0, times):
        pyautogui.click()
    time.sleep(0)
    
def no_afk(mouseMove):
    if bool(random.getrandbits(1)):
        pyautogui.moveTo(move_right_x, move_right_y,duration=0.1, tween=pyautogui.easeInOutQuad)
    else:
        pyautogui.moveTo(move_left_x, move_left_y,duration=0.1, tween=pyautogui.easeInOutQuad)
    print(mouseMove)
    pyautogui.click(button=mouseMove)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.press('t')
    keyboard.release('t')
    start = time.time()

def buy_item(entryPrice, amount, mouseMove):
    loop = True
    start = time.time() 
    while loop:
        clic(item_x, item_y,2)
        clic(buy_button_x, buy_button_y,1)
        clic(add_x, add_y,2)
        keyboard.write(str(amount))
        clic(price_x, price_y,2)
        keyboard.write(str(entryPrice))
        clic(buy_final_x, buy_final_y,2)
        clic(confirm_x, confirm_y,2)
        timeAlive = time.time() - start
        if timeAlive >= seconds:
            no_afk(str(mouseMove))
        if keyboard.is_pressed("ctrl"):
            loop = False 
           
  
