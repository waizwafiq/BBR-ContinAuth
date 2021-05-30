import pyautogui as pag
import time, timeit
import ctypes, math

features = {
    't': [],  # time
    'ttc': [],  # time to collect
    'paused_time': [],  # paused time (cumulative of ttc)
    'paused_time_ratio': [],  # paused time ratio
    'x': [],  # x-coordinate
    'y': [],  # y-coordinate
    's_euclid_c': [],  # cumulative euclidean distance
    'theta': [],  # tangential angle from x-axis
    'c': [],  # curvature
    'c_roc': [],  # rate of change of curvature
    'v_x': [],  # horizontal velocity
    'v_y': [],  # vertical velocity
    'v': [],  # resultant velocity
    'a': [],  # resultant acceleration
    'j': [],  # resultant jerk
    'w': [],  # angular velocity
    'straightness': [],
    'jitter': [],
    'pauses': []
}


def run(time_interval=0.01, stopTime=5):
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)

    '''INITIALIZE VARIABLES'''
    pos = pag.position()
    x_i, y_i = pos[0], screensize[1] - pos[1]  # get initial coordinates
    x_o, y_o = x_i, y_i

    t, t_p, t_o = 0 - time_interval, time_interval, 0  # (0 - time_interval) to get the initial data features (t=0)
    s_euclid = 0  # cumulative s_euclid
    theta_i = 0  # initial angle of the path, tangent with the x-axis
    v_i = 0  # initial velocity
    a_i = 0  # initial acceleration
    c_i = 0  # initial curvature
    pauses = 0  # initial pauses
    paused_time = 0  # initial paused time
    paused_time_ratio = 0
    while (t // 1) < stopTime:
        '''TIME'''
        t_i = t
        start_tp = timeit.default_timer()  # start processing time, t_p(0)
        time.sleep(time_interval * 1)  # pause for (time_interval) seconds
        t += t_p  # t_f = t_i + t_p
        dt = t - t_i

        pos = pag.position()  # get the current position of the mouse
        x_f, y_f = pos[0], screensize[1] - pos[1]
        if x_f != x_i or y_f != y_i or t == 0:
            # obtain features when the mouse is moving only

            '''SPATIAL FEATURES'''
            # Coordinates
            dx, dy = (x_f - x_i), (y_f - y_i)  # get differentials
            x_i, y_i = x_f, y_f  # update the latest coordinates with current
            # Path length
            ds_euclid = (dx ** 2 + dy ** 2) ** 0.5  # get the change of path length
            s_euclid += ds_euclid  # get the cumulative euclidean distance
            # Angle of the path tangent with x-axis
            if dx != 0:
                theta = math.atan(dy / dx)
            elif t == 0:
                theta = 0
            else:
                theta = math.pi / 2
            d_theta = theta - theta_i  # get the change in angle
            theta_i = theta  # update the latest theta
            # Curvature
            if ds_euclid != 0:
                c = d_theta / ds_euclid
                d_c = c - c_i  # get the change in curvature
                c_i = c  # update the latest c
                c_roc = d_c / ds_euclid  # get the rate of change (roc) of curvature
            else:
                c, d_c = 0, -1 * c_i
                c_i = 0
                c_roc = d_c / dt

            '''TEMPORAL FEATURES'''
            # Velocity
            v_x, v_y = dx / dt, dy / dt  # calculate horizontal and vertical velocity
            v_t = (v_x ** 2 + v_y ** 2) ** 0.5  # get the resultant velocity
            dv_t = v_t - v_i  # get the change in velocity (dv = v_i - v_(i-1))
            v_i = v_t  # update the latest velocity with current
            # Acceleration
            a_t = dv_t / dt
            da_t = a_t - a_i  # get the change in acceleration (da = a_i - a_(i-1))
            a_i = a_t  # update the latest acceleration with current
            # Jerk
            j_t = da_t / dt
            # Angular velocity
            w = d_theta / dt

            '''DERIVED FEATURES'''
            # Straightness
            if s_euclid != 0:
                straightness = (((x_o - x_f) ** 2 + (y_o - y_f) ** 2) ** 0.5) / s_euclid
            else:
                straightness = 1
            # Jitter
            if s_euclid != ds_euclid:
                jitter = s_euclid / (s_euclid - ds_euclid)  # jitter = s_i/s_(i-1)
            else:
                jitter = 0
            # Number of pauses
            ttc = t - t_o
            t_o = t
            if ttc > dt:
                pauses += 1
                paused_time += ttc
            elif t != 0:
                paused_time_ratio = paused_time / t

            '''ADDING INTO FEATURES DICTIONARY'''
            features['t'].append(t)
            features['ttc'].append(ttc)
            features['paused_time'].append(paused_time)
            features['paused_time_ratio'].append(paused_time_ratio)
            features['x'].append(x_f)
            features['y'].append(y_f)
            features['s_euclid_c'].append(s_euclid)
            features['theta'].append(theta)
            features['c'].append(c)
            features['c_roc'].append(c_roc)
            features['v_x'].append(v_x)
            features['v_y'].append(v_y)
            features['v'].append(v_t)
            features['a'].append(a_t)
            features['j'].append(j_t)
            features['w'].append(w)
            features['straightness'].append(straightness)
            features['jitter'].append(jitter)
            features['pauses'].append(pauses)
            # features['n_critical'].append(n_critical)

        t_p = timeit.default_timer() - start_tp  # end processing time

    return features
