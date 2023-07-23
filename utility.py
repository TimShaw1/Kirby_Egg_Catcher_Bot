import win32gui
import pyautogui
import ctypes
import copy

ctypes.windll.user32.SetProcessDPIAware()

def get_window_name():
    windows = pyautogui.getAllWindows()
    for w in windows:
        if "yuzu" in w.title:
            return w.title

def get_screenshot(dimensions=None, window_title=get_window_name()):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd and not dimensions:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im
        elif dimensions:
            im = pyautogui.screenshot(region=dimensions)
            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im
    
def get_game_screenshot(dim):
    game_dim = copy.deepcopy(dim)
    game_dim[0] += round(dim[2] / 17.66)
    game_dim[1] = round(dim[3] / 20.05)
    game_dim[2] = round(dim[2] / 1.13)
    game_dim[3] = round(dim[3] / 1.05)

    return get_screenshot(game_dim)
    
def get_dimensions():
    window_title=get_window_name()
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)
        x, y, x1, y1 = win32gui.GetClientRect(hwnd)
        x, y = win32gui.ClientToScreen(hwnd, (x, y))
        x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
        return[x,y,x1,y1]
    else:
        print('Window not found!')

def get_screen_coords():
    while True:
        print(pyautogui.position(), end='\r')

def get_screen_ratio(dim):
    while True:
        print(round(abs(dim[2] / (pyautogui.position().x - dim[0])), 2), round(abs(dim[3] / (pyautogui.position().y - dim[1])), 2), end='\r')