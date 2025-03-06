from types import NoneType

import numpy as np

from EQ_Data import EQ_Data
from Integrators.Newmark import newmarkBeta_GroundMotion


def getFullSpectralAll(eq_data: EQ_Data,T=None, step=0.02, zeta=0.15, g_units=False) -> [np.ndarray, np.ndarray, np.ndarray]:
    time_arr = eq_data.time
    ground_accel = eq_data.ground_accel

    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    if isinstance(zeta, NoneType):
        zeta = np.arange(0.01, 0.3, step=step)
    elif isinstance(zeta, float):
        zeta=[zeta]

    D = np.zeros((len(T), len(zeta)))
    V = np.zeros((len(T), len(zeta)))
    A = np.zeros((len(T), len(zeta)))
    PV = np.zeros((len(T), len(zeta)))
    PA = np.zeros((len(T), len(zeta)))

    for t in range(0, len(T)):
        for z in range(0, len(zeta)):
            wn = 2 * np.pi / T[t]
            disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn, zeta=zeta[z], g_units=g_units)

            D[t, z] = max(abs(disp))
            V[t, z] = max(abs(vel))
            A[t, z] = max(abs(accel))
            PV[t, z] = wn * D[t, z]
            PA[t, z] = wn**2 * D[t, z]

    return D, V, A, PV, PA, T