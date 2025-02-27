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
    z_max=max(abs(ground_accel_arr))
    wd = wn*np.sqrt(1 - zeta ** 2)
    print(z_max)
    # impulse_resp_func=1/(m*wd)*np.exp(-zeta*wn*t_arr)*np.sin(wd*t_arr)
    impulse_resp_func = (1 / (wd*z_max)) * np.exp(-zeta * wn * t_arr) * np.sin(wd * t_arr)

    # disp = np.convolve(ground_accel_arr, impulse_resp_func, mode='same')
    disp = np.convolve(impulse_resp_func,ground_accel_arr, mode='full')
    disp=disp[0:len(t_arr)]*tstep

    vel = (disp[1:] - disp[:-1]) / tstep
    vel = np.concatenate(([0], vel))

    accel = (vel[1:] - vel[:-1]) / tstep
    accel = np.concatenate(([0], accel))

    return disp, vel, accel
