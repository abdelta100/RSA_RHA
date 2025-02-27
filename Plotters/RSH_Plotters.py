from collections.abc import Iterable
from types import NoneType

import numpy as np
import matplotlib.pyplot as plt

def plotDVASpectrum(D,V,A,T,zeta=None):
    figure, axis = plt.subplots(3, 1)

    if isinstance(zeta, Iterable):
        for z in range(len(zeta)):
            axis[0].plot(T,A[:, z], label="z= "+str(z))
        axis[0].set_title("Spectral Acceleration")

        for z in range(len(zeta)):
            axis[1].plot(T, V[:, z] , label="z= "+str(z))
        axis[1].set_title("Spectral Velocity")

        for z in range(len(zeta)):
            axis[2].plot(T, D[:, z], label="z= "+str(z))
        axis[2].set_title("Spectral Displacement")

    else:
        figure, axis = plt.subplots(3, 1)

        axis[0].plot(T, A)
        axis[0].set_title("Spectral Acceleration")

        axis[1].plot(T, V)
        axis[1].set_title("Spectral Velocity")

        axis[2].plot(T, D)
        axis[2].set_title("Spectral Displacement")

    plt.show()

def plotRSH(disp, vel, accel, time, g_accel=None):

    n=4
    if isinstance(g_accel, NoneType):
        n=3
        figure, axis = plt.subplots(n, 1)

    else:
        n=4
        figure, axis = plt.subplots(n, 1)
        axis[0].plot(time, g_accel)
        axis[0].set_title("Ground Accel")

    axis[n-3].plot(time, accel)
    axis[n-3].set_title("Acceleration")

    axis[n-2].plot(time, vel)
    axis[n-2].set_title("Velocity")

    axis[n-1].plot(time, disp)
    axis[n-1].set_title("Displacement")

    plt.show()