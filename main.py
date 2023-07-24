from utility import *
import copy
import keyboard
import time
from ctypes import windll
dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))

dim = get_dimensions()

bomb_col = (45,58,126)
egg_col = (255,255,255)
bg = (99, 111, 176)
bg2 = (51, 99, 146)

x = dim[0] + round(dim[2] / 2.34)
x2 = dim[0] + round(dim[2] / 2.74)
y = dim[1] + round(dim[3] / 1.87)
pyautogui.moveTo(x,y)

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
        time.sleep(5/60)
    #print(time.time() - t)