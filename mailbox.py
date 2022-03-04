import time
import keyboard
import pyautogui

mess_x = 280
mess_y = 139
acc_x = 727
acc_y = 677
del_x = 865
del_y = 673

r = 50

def clic(x,y,times):
    #print(f"{x}, {y}")
    pyautogui.moveTo(x, y,duration=0.2, tween=pyautogui.easeInOutQuad)
    if times>1:
        pyautogui.doubleClick()
    else:
        pyautogui.click()
    time.sleep(0)



def clearMail():
    loop = True
    while loop:
        clic(mess_x, mess_y,1)
        clic(acc_x, acc_y,1)
        clic(del_x, del_y,1)
        if keyboard.is_pressed("ctrl"):
            loop = False