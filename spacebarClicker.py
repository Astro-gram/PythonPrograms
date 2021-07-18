import pyautogui
import keyboard as kb
import time

time.sleep(2)
while kb.is_pressed("q") == False:
    pyautogui.press("space")
