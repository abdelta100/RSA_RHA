import numpy as np


# from typing import Tuple


def newmarkBeta(ground_accel_arr: np.ndarray, t_arr: np.ndarray, wn: float, zeta: float, m=1, beta: float = 1 / 4,
                lambda_: float = 0.5) \
        -> [np.ndarray, np.ndarray, np.ndarray]:
    disp = np.zeros(len(t_arr))
    vel = np.zeros(len(t_arr))
    accel = np.zeros(len(t_arr))

    k = m / wn ** 2
    c = 2 * zeta * wn

    disp[0] = 0
    vel[0] = 0
    # accel[0] = (1/m)*ground_accel_arr[0]-c*vel[0]-k*disp[0]
    accel[0] = (1) * (ground_accel_arr[0] - c * vel[0] - k * disp[0])

    wd = wn * np.sqrt(1 - zeta ** 2);

    # If timestep is constant
    h = t_arr[1]-t_arr[0];

    ms = m + lambda_ *h*c + beta * h ** 2 * k;

    for i in range(0, len(t_arr) - 1):
        dps = -k * disp[i] - (c + h * k) * vel[i] - (h * (1 -lambda_) * c + ((h ** 2) / 2)
                                             * (1 - 2 * beta) * k) * accel[i] + ground_accel_arr[i + 1]
        accel[i + 1] = dps / ms
        vel[i + 1] = vel[i] + ((1 -lambda_) * accel[i] +lambda_ * accel[i+1])*h
        disp[i + 1] = disp[i] + vel[i] * h + ((1 - 2 * beta) * accel[i] + 2 * beta * accel[i + 1]) * (h ** 2) / 2

    return disp, vel, accel
