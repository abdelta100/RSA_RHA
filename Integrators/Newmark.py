import numpy as np
import ctypes

from Constants import *

def newmarkBeta(applied_force: np.ndarray, t_arr: np.ndarray, wn: float, zeta: float, m=1, beta: float = 1 / 6,
                gamma_: float = 0.5) \
        -> [np.ndarray, np.ndarray, np.ndarray]:
    newmark = ctypes.CDLL("./Integrators/newmark.dll")


    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<_____________C Implementation____________>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    n = len(applied_force)
    force_arr = (ctypes.c_double * n)(*applied_force)
    time_arr = (ctypes.c_double * n)(*t_arr)
    disp = (ctypes.c_double * n)()
    vel = (ctypes.c_double * n)()
    accel = (ctypes.c_double * n)()

    newmark.newmark_beta.argtypes = [
        ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int,
        ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
        ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
    ]

    newmark.newmark_beta(force_arr, time_arr, n, wn, zeta, m, beta, gamma_, disp, vel, accel)

    return np.array(disp), np.array(vel), np.array(accel)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<_____________C Implementation____________>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    # k = m * wn ** 2
    # c = 2 * m * zeta * wn
    #
    # disp = np.zeros(len(t_arr))
    # vel = np.zeros(len(t_arr))
    # accel = np.zeros(len(t_arr))  # Acceleration
    #
    # disp[0] = 0
    # vel[0] = 0
    # accel[0] = 0
    # accel[0] = (applied_force[0] - c * vel[0] - k * disp[0]) / m
    # h = t_arr[1] - t_arr[0]
    #
    # a1 = (1 / (beta * h ** 2)) * m + (gamma_ / (beta * h)) * (c)
    # a2 = (1 / (beta * h)) * m + ((gamma_ / beta) - 1) * (c)
    # a3 = ((1 / (2 * beta)) - 1) * m + (h) * (gamma_ / (2 * beta) - 1) * (c)
    #
    # ks = k + a1
    #
    # for i in range(len(applied_force) - 1):
    #     ps = applied_force[i + 1] + a1 * disp[i] + a2 * vel[i] + a3 * accel[i]
    #     disp[i + 1] = ps / ks
    #     vel[i + 1] = (gamma_ / (beta * h)) * (disp[i + 1] - disp[i]) + (1 - gamma_ / beta) * vel[i] + h * (
    #                 1 - gamma_ / (2 * beta)) * accel[i]
    #     accel[i + 1] = (1 / (beta * h ** 2)) * (disp[i + 1] - disp[i]) - (1 / (beta * h)) * vel[i] - (
    #                 (1 / (2 * beta)) - 1) * accel[i]
    #
    # return disp, vel, accel


def newmarkBeta_GroundMotion(ground_accel_arr: np.ndarray, t_arr: np.ndarray, wn: float, zeta: float, m=1,
                             beta: float = 1 / 4,
                             gamma_: float = 1 / 2, g_units=False) \
        -> [np.ndarray, np.ndarray, np.ndarray]:
    # TODO handle g here
    # TODO remove dependence on explicit ground accel array
    # Not required anymore, but haven't verified.
    if g_units:
        accel_ground = ground_accel_arr * g
    else:
        accel_ground = ground_accel_arr

    eq_force = -accel_ground * m
    disp, vel, accel = newmarkBeta(eq_force, t_arr, wn=wn, zeta=zeta, m=m, beta=beta, gamma_=gamma_)

    return disp, vel, accel
