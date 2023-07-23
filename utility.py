import win32gui
import pyautogui
import ctypes

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