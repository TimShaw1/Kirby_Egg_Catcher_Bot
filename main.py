from utility import *
import copy
import keyboard
import time

dim = get_dimensions()

bomb_col = (45,58,126)
egg_col = (255,255,255)
bg = (99, 111, 176)
bg2 = (51, 99, 146)

x = dim[0] + round(dim[2] / 2.74)
y = dim[1] + round(dim[3] / 1.67)
pyautogui.moveTo(x,y)

while not keyboard.is_pressed('`'):
    pixel = pyautogui.pixel(x, y)
    if pixel != bg and pixel != bg2:
        print(pixel)
    pyautogui.keyUp('c')
    if pixel[0] > 200 and pixel[1] > 180 and pixel[2] > 180:
        pyautogui.keyDown('c')
        print("egg")
        time.sleep(0.1)