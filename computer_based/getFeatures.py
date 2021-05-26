import pyautogui as pag
import pandas as pd
import time
import ctypes


def run(time_interval: float, stopTime: float):
    features = {
        't': [],
        'x': [],
        'y': []
    }

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)
    t = 0
    while t // 1 < stopTime:
        pos = pag.position()  # get the current position of the mouse
        x_coord, y_coord = pos[0], screensize[1] - pos[1]
        t += time_interval
        # print(t, x_coord, y_coord)

        features['t'].append(t)
        features['x'].append(x_coord)
        features['y'].append(y_coord)

        time.sleep(time_interval)

    return features
