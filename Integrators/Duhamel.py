import numpy as np
from numpy.ma.core import concatenate


def duhamel(ground_accel_arr, t_arr: np.ndarray, wn: float = 6, zeta: float = 0.1, m: float = 1) -> [np.ndarray,
                                                                                                     np.ndarray,
                                                                                                     np.ndarray]:
    disp = np.zeros(len(t_arr))
    vel = np.zeros(len(t_arr))
    accel = np.zeros(len(t_arr))

    # If timesteps are equal
    tstep = t_arr[1] - t_arr[0]

    wd = wn*np.sqrt(1 - zeta ** 2)
    # impulse_resp_func=1/(m*wd)*np.exp(-zeta*wn*t_arr)*np.sin(wd*t_arr)
    impulse_resp_func = 1 / (wd) * np.exp(-zeta * wn * t_arr) * np.sin(wd * t_arr)

    # disp = np.convolve(ground_accel_arr, impulse_resp_func, mode='same')
    disp = np.convolve(impulse_resp_func,ground_accel_arr, mode='same')
    vel = disp[0:-1] - disp[1:] / tstep
    vel = concatenate(([0], vel))

    accel = (vel[0:-1] - vel[1:]) / tstep
    accel = concatenate(([0], accel))

    return disp, vel, accel
