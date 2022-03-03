from ctypes import alignment
import time
import keyboard
import pyautogui
from tkinter import *
from tkinter.ttk import *

def clic(x,y,times):
    print(f"{x}, {y}")
    pyautogui.moveTo(x, y,duration=0.1, tween=pyautogui.easeInOutQuad)
    if times>1:
        pyautogui.doubleClick()
    else:
        pyautogui.click()
    time.sleep(0)

def createWindows():
    tab_control = ttk.Notebook(window)
    generateBuyerWindow(tab_control)
    generateMailWindow(tab_control)
    tab_control.pack(expand=1, fill='both')

def generateBuyerWindow(tab_control):
    buyerTab = ttk.Frame(tab_control)
    tab_control.add(buyerTab, text='Buy items')
    lbl1 = Label(buyerTab, text= 'Open the auction at the game')
    lbl1.grid(column=0, row=0)
    
def generateMailWindow(tab_control):
    buyerTab = ttk.Frame(tab_control)
    tab_control.add(buyerTab, text='Clear mail box')
    lbl1 = Label(buyerTab, text= 'Open the mail box at the game', anchor='center')
    lbl1.grid(column=0, row=0)    
    
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

window = Tk()

window.title("LostArk Bot")
window.geometry('350x400')
combo = Combobox(window)
createWindows()
window.mainloop()

loop = False
while loop:
    clic(item_x, item_y,2)
    clic(buy_button_x, buy_button_y,1)
    clic(add_x, add_y,1)
    clic(price_x, price_y,2)
    keyboard.write('10')
    clic(buy_final_x, buy_final_y,2)
    clic(confirm_x, confirm_y,2)
    if keyboard.is_pressed("h"):
        loop = False

    

