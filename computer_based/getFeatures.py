import pyautogui as pag
import pandas as pd
import time, timeit
import ctypes

features = {
    't': [],
    'x': [],
    'y': [],
    'dx': [],
    'dy': [],
    'v_x': [],
    'v_y': []
}


def run(time_interval: float, stopTime: float):
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)

    pos = pag.position()
    x_i, y_i = pos[0], screensize[1] - pos[1]  # get initial coordinates

    t, t_p = 0, time_interval
    while (t // 1) < stopTime:
        t_i = t

        start_tp = timeit.default_timer()  # start processing time, t_p(0)
        time.sleep(time_interval)  # pause for (time_interval) seconds
        t += t_p  # t_f = t_i + t_p

        pos = pag.position()  # get the current position of the mouse
        x_f, y_f = pos[0], screensize[1] - pos[1]
        dx, dy, dt = (x_f - x_i), (y_f - y_i), (t - t_i)  # get differentials
        x_i, y_i = x_f, y_f  # update the initial coordinates with current

        v_x, v_y = dx / dt, dy / dt  # calculate horizontal and vertical velocity

        features['t'].append(t)
        features['x'].append(x_f)
        features['y'].append(y_f)
        features['dx'].append(dx)
        features['dy'].append(dy)
        features['v_x'].append(v_x)
        features['v_y'].append(v_y)
        t_p = timeit.default_timer() - start_tp  # end processing time

    return features
