import time
from math import sin, cos
import keyboard
import pyautogui



def run_no_afk():
    theta = 0
    step = 1
    h = int(2560/2)
    k = int(1440/2)
    r = 50
    running = True
    while running:
        time.sleep(5)

        x = h + r*cos(theta)
        y = k + r*sin(theta)

        print(f"{x}, {y}")

        if theta == 360:
            theta = 0

        pyautogui.moveTo(x, y)

        pyautogui.click(button='right')

        theta+=step

        if keyboard.is_pressed("ctrl"):
            running = not running