from platform import machine
from types import NoneType

import numpy as np
from numpy import pi

from Constants import *
from EQ_Data import EQ_Data

from Integrators.Newmark import newmarkBeta, newmarkBeta_GroundMotion


def getSpectralDVA(eq_data, T, zeta=0.15, g_units=False) -> [float, float, float]:
    wn = 2 * pi / T
    time_arr = eq_data[:, 0]
    ground_accel = eq_data[:, 1] * g

    disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta,  g_units=g_units)

    D = max(abs(disp))
    V = max(abs(vel))
    A = max(abs(accel))

    return D, V, A, T


# def getFullSpectralDVA(eq_data, step=0.05, T=None, zeta=0.15, ) -> [np.ndarray, np.ndarray, np.ndarray]:
#     # Fill this
#
#     # return D, V, A, T

def getFullSpectralDVA_T_range(eq_data: EQ_Data,T=None, step=0.02, zeta=0.15, g_units=False) -> [np.ndarray, np.ndarray, np.ndarray]:
    time_arr = eq_data.time
    ground_accel = eq_data.ground_accel

    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    D = np.zeros(len(T))
    V = np.zeros(len(T))
    A = np.zeros(len(T))

    for t in range(0, len(T)):
        print(T[t])
        wn = 2 * pi / T[t]
        disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta, g_units=g_units)

        D[t] = max(np.abs(disp))
        V[t] = max(np.abs(vel))
        A[t] = max(np.abs(accel))

    return D, V, A, T

def getFullSpectralDVA_zeta_range(eq_data, T, step=0.001, zeta=None,  g_units=False ) -> [np.ndarray, np.ndarray, np.ndarray]:
    time_arr = eq_data[:, 0]
    ground_accel = eq_data[:, 1] * g

    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    if isinstance(zeta, NoneType):
        zeta = np.arange(0.01, 0.3, step=step)

    D = np.zeros(len(zeta))
    V = np.zeros(len(zeta))
    A = np.zeros(len(zeta))

    for t in range(0, len(zeta)):
        wn = 2 * pi / T
        disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta[t],  g_units=g_units)

        D[t] = max(abs(disp))
        V[t] = max(abs(vel))
        A[t] = max(abs(accel))

    return D, V, A, T