from ctypes import alignment
from app import *
import time
import keyboard
import pyautogui
 

# Bot methods
def clic(x,y,times):
    print(f"{x}, {y}")
    pyautogui.moveTo(x, y,duration=0.1, tween=pyautogui.easeInOutQuad)
    if times>1:
        pyautogui.doubleClick()
    else:
        pyautogui.click()
    time.sleep(0)
    
def buy_item(price):
    clic(item_x, item_y,2)
    clic(buy_button_x, buy_button_y,1)
    clic(add_x, add_y,1)
    clic(price_x, price_y,2)
    keyboard.write(price)
    clic(buy_final_x, buy_final_y,2)
    clic(confirm_x, confirm_y,2)     
        
buy_button_x = 2088
buy_button_y = 1232
item_x = 954
item_y = 442
add_x = 1458
add_y = 678
price_x = 1356 
price_y = 744
buy_final_x = 1281
buy_final_y = 1082
confirm_x = 1280
confirm_y = 780

price = 10

main_app()

loop = False
while loop:
    buy_item(price)
    if keyboard.is_pressed("h"):
        loop = False

    

