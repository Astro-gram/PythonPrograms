from pyautogui import *
import pyautogui
import time
import keyboard
import mouse
import win32api, win32con

#


def RightClick(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def LeftClick(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

time.sleep(2)

while keyboard.is_pressed('q') == False:
    while keyboard.is_pressed("tab") == True:
        RightClick(pyautogui.position().x, pyautogui.position().y)

    while keyboard.is_pressed("control") == True:
        LeftClick(pyautogui.position().x, pyautogui.position().y)


    
