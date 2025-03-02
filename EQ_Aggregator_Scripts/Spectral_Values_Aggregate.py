from types import NoneType

import numpy as np

from EQ_Data import EQ_Data
from Response_History.SpectralValues import getFullSpectralDVA_T_range
from Response_Spectrum.PsuedoSpectralValues import getFullSpectralDPVPA_T_range


def getFullSpectralDVA_Aggregate(eq_list=list[EQ_Data], T=None, step=0.02, zeta=0.15):
    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    D = np.zeros((len(T), len(zeta), len(eq_list)))
    V = np.zeros((len(T), len(zeta), len(eq_list)))
    A = np.zeros((len(T), len(zeta), len(eq_list)))

    for i, eq in enumerate(eq_list):
        d, v, a, _ = getFullSpectralDVA_T_range(eq, T, step, zeta)
        D[:, :, i] = d
        V[:, :, i] = v
        A[:, :, i] = a
        print("Finished "+ eq.meta_name)

    return D, V, A, T

def getFullSpectralDPVPA_Aggregate(eq_list=list[EQ_Data], T=None, step=0.02, zeta=0.15):
    if isinstance(T, NoneType):
        T = np.arange(0.05, 20, step=step)

    D = np.zeros((len(T), len(zeta), len(eq_list)))
    PV = np.zeros((len(T), len(zeta), len(eq_list)))
    PA = np.zeros((len(T), len(zeta), len(eq_list)))

    for i, eq in enumerate(eq_list):
        d, v, a, _ = getFullSpectralDPVPA_T_range(eq, T, step, zeta)
        D[:, :, i] = d
        PV[:, :, i] = v
        PA[:, :, i] = a
        print("Finished "+ eq.meta_name)

    return D, PV, PA, T