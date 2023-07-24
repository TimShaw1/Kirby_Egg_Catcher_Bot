from utility import *
import copy
import keyboard
import time
from ctypes import windll
dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))

dim = get_dimensions()

LEVEL = "3"

bomb_col = (45,58,126)
egg_col = (255,255,255)
bg = (99, 111, 176)
bg2 = (51, 99, 146)

x = dim[0] + round(dim[2] / 2.34)
x2 = dim[0] + round(dim[2] / 2.74)

y_1 = dim[1] + round(dim[3] / 1.65)
y_2 = dim[1] + round(dim[3] / 1.7)
y_3 = dim[1] + round(dim[3] / 1.8)
pyautogui.moveTo(x,y_3)

level_ys = {"1": y_1, "2": y_2, "3": y_3}
level_times = {"1": 8/60, "2": 6/60, "3": 5/60}

y = level_ys[LEVEL]
wait_time = level_times[LEVEL]

while not keyboard.is_pressed('`'):
    t = time.time()
    pixel = getpixel(x, y)
    pixel2 = getpixel(x2, y)
    #if keyboard.is_pressed('c'):
    keyboard.release('c')
    if pixel[0] > 200 and pixel[1] > 180 and pixel[2] > 180:
        keyboard.press('c')
        print("egg")
        time.sleep(5/60)
    if pixel2[0] > 200 and pixel2[1] > 180 and pixel2[2] > 180:
        keyboard.press('c')
        print("egg")
        time.sleep(wait_time)
    #print(time.time() - t)