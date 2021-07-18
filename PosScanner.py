import pyautogui as pq
import time as t
import keyboard as kb
import random

#Color: (186, 219,  85)
#Pos: X: 934 Y:  848

def jump():
    pq.press('up')


t.sleep(1)
while kb.is_pressed('q') == False:
    t.sleep(random.uniform(0.1, 1.0))
    if pq.pixel(934, 848)[1] != 219:
        jump()
        t.sleep(0.1)
