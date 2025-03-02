from platform import machine
from types import NoneType

import numpy as np
from numpy import pi

from Constants import *
from EQ_Data import EQ_Data

from Integrators.Newmark import newmarkBeta, newmarkBeta_GroundMotion


def getSpectralDPVPA(eq_data, T, zeta=0.15, g_units=False) -> [float, float, float]:
    wn = 2 * pi / T
    time_arr = eq_data[:, 0]
    ground_accel = eq_data[:, 1] * g

    disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta,  g_units=g_units)

    D = max(abs(disp))
    PV = wn*D
    PA = (wn**2)*D

    return D, PV, PA, T


# def getFullSpectralDVA(eq_data, step=0.05, T=None, zeta=0.15, ) -> [np.ndarray, np.ndarray, np.ndarray]:
#     # Fill this
#
#     # return D, V, A, T

def getFullSpectralDPVPA_T_range(eq_data: EQ_Data,T=None, step=0.02, zeta=0.15, g_units=False) -> [np.ndarray, np.ndarray, np.ndarray]:
    time_arr = eq_data.time
    ground_accel = eq_data.ground_accel

    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    if isinstance(zeta, NoneType):
        zeta = np.arange(0.01, 0.3, step=step)
    elif isinstance(zeta, float):
        zeta=[zeta]

    D = np.zeros((len(T), len(zeta)))
    PV = np.zeros((len(T), len(zeta)))
    PA = np.zeros((len(T), len(zeta)))

    for t in range(0, len(T)):
        for z in range(0, len(zeta)):
            wn = 2 * pi / T[t]
            disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta[z], g_units=g_units)

            D[t, z] = max(abs(disp))
            PV[t, z] = wn*D[t, z]
            PA[t, z] = (wn**2)*D[t, z]

    return D, PV, PA, T

def getFullSpectralDPVPA_zeta_range(eq_data, T, step=0.001, zeta=None,  g_units=False ) -> [np.ndarray, np.ndarray, np.ndarray]:
    time_arr = eq_data[:, 0]
    ground_accel = eq_data[:, 1] * g

    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    if isinstance(zeta, NoneType):
        zeta = np.arange(0.01, 0.3, step=step)

    D = np.zeros((len(T),len(zeta)))
    PV = np.zeros((len(T),len(zeta)))
    PA = np.zeros((len(T),len(zeta)))

    for t in range(0, len(T)):
        for z in range(0, len(zeta)):
            wn = 2 * pi / T
            disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta[z],  g_units=g_units)

            D[t,z] = max(abs(disp))
            PV[t, z] = wn * D[t, z]
            PA[t, z] = (wn ** 2) * D[t, z]

    return D, PV, PA, T