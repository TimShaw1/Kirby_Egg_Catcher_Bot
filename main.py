from utility import *
import copy
import keyboard
import time
from PIL import ImageGrab

dim = get_dimensions()

bomb_col = (45,58,126)
egg_col = (255,255,255)
bg = (99, 111, 176)
bg2 = (51, 99, 146)

x = dim[0] + round(dim[2] / 2.74)
y = dim[1] + round(dim[3] / 1.67)
pyautogui.moveTo(x,y)

# short = 12-13 frames -- 8 from the apex
# long = 18-23 frames -- 13 from the apex

top_x = dim[0] + round(dim[2] / 1.79)
top_y = dim[1] + round(dim[3] / 5.83)

mid_x = dim[0] + round(dim[2] / 1.76)
mid_y = dim[1] + round(dim[3] / 3.57)

low_x = dim[0] + round(dim[2] / 1.87)
low_y = dim[1] + round(dim[3] / 2.84)

egg = False
egg_times = []

def get_pixels():
    pixel_top = ImageGrab.grab().getpixel((top_x, top_y))
    pixel_mid = ImageGrab.grab().getpixel((mid_x, mid_y))
    pixel_low = ImageGrab.grab().getpixel((low_x, low_y))

    pix_list = [pixel_low, pixel_mid, pixel_top]
    for i in range(len(pix_list)):
        if pix_list[i][0] > 200 and pix_list[i][1] > 180 and pix_list[i][2] > 180:
            egg_times.append(time.time() + 6/60 + (3/60)*i)
            egg_times.sort()
            print("egg")
            continue

while not keyboard.is_pressed('`'):
    get_pixels()

    t = time.time()
    offset = 0
    if len(egg_times) > 0:
        if egg_times[0] <= t:
            pyautogui.keyDown('c')
            egg_times.pop(0)
            t2 = time.time()
            while time.time() - t2 < 1/15:
                get_pixels()
            pyautogui.keyUp('c')