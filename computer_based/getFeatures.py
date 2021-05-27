import pyautogui as pag
import pandas as pd
import time, timeit
import ctypes, math

features = {
    't': [],
    'x': [],
    'y': [],
    'dx': [],
    'dy': [],
    's_euclid': [],
    's_euclid_c': [],
    'v_x': [],
    'v_y': [],
    'v': []
}


def run(time_interval: float, stopTime: float):
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)

    pos = pag.position()
    x_i, y_i = pos[0], screensize[1] - pos[1]  # get initial coordinates

    t, t_p = 0, time_interval
    sum_se = 0  # cumulative s_euclid and s_manhattan
    while (t // 1) < stopTime:
        '''TIME'''
        t_i = t
        start_tp = timeit.default_timer()  # start processing time, t_p(0)
        time.sleep(time_interval)  # pause for (time_interval) seconds
        t += t_p  # t_f = t_i + t_p
        dt = t - t_i

        '''POSITIONS/SPATIAL FEATURES'''
        pos = pag.position()  # get the current position of the mouse
        x_f, y_f = pos[0], screensize[1] - pos[1]
        dx, dy = (x_f - x_i), (y_f - y_i)  # get differentials
        x_i, y_i = x_f, y_f  # update the initial coordinates with current
        s_e = (dx ** 2 + dy ** 2) ** 0.5
        sum_se += s_e

        '''TEMPORAL FEATURES'''
        v_x, v_y = dx / dt, dy / dt  # calculate horizontal and vertical velocity
        v_t = (v_x ** 2 + v_y ** 2) ** 0.5

        '''ADDING INTO FEATURES DICTIONARY'''
        features['t'].append(t)
        features['x'].append(x_f)
        features['y'].append(y_f)
        features['dx'].append(dx)
        features['dy'].append(dy)
        features['s_euclid'].append(s_e)
        features['s_euclid_c'].append(sum_se)
        features['v_x'].append(v_x)
        features['v_y'].append(v_y)
        features['v'].append(v_t)
        t_p = timeit.default_timer() - start_tp  # end processing time

    return features
