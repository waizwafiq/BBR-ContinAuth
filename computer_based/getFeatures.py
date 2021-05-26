import pyautogui as pag
import pandas as pd
import time
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)

while(True):
    pos = pag.position() #get the current position of the mouse
    x_coord, y_coord = pos[0], screensize[1]-pos[1]
    print(x_coord, y_coord)
    time.sleep(0.01)
