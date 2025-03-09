from collections.abc import Iterable
from types import NoneType

import numpy as np
import matplotlib.pyplot as plt

def plotDVASpectrum(D,V,A,T,zeta=None, name="", isloglog=False, grid_on=False):
    figure, axis = plt.subplots(3, 1, figsize=(10, 8))
    grid_on = grid_on
    x_line = True

    if isinstance(zeta, (list, np.ndarray)):
        for z in range(len(zeta)):
            axis[0].plot(T,A[:, z], label="z= "+str(zeta[z]))

        if isloglog:
            axis[0].set_xscale('log')
            axis[0].set_yscale('log')

        axis[0].set_title("Spectral Acceleration")
        axis[0].set_xlabel('Time Period (s)')
        axis[0].set_ylabel('Acceleration')
        axis[0].grid(grid_on)
        axis[0].legend(loc='upper right')
        if x_line:
            axis[0].axhline(y=0, color='black', linewidth=1.5)

        for z in range(len(zeta)):
            axis[1].plot(T, V[:, z] , label="z= "+str(zeta[z]))

        if isloglog:
            axis[1].set_xscale('log')
            axis[1].set_yscale('log')

        axis[1].set_title("Spectral Velocity")
        axis[1].set_xlabel('Time Period(s)')
        axis[1].set_ylabel('Velocity')
        axis[1].grid(grid_on)
        axis[1].legend(loc='upper right')
        if x_line:
            axis[1].axhline(y=0, color='black', linewidth=1.5)

        for z in range(len(zeta)):
            axis[2].plot(T, D[:, z], label="z= "+str(zeta[z]))

        if isloglog:
            axis[2].set_xscale('log')
            axis[2].set_yscale('log')

        axis[2].set_title("Spectral Displacement")
        axis[2].set_xlabel('Time Period(s)')
        axis[2].set_ylabel('Displacement')
        axis[2].grid(grid_on)
        axis[2].legend(loc='upper right')
        if x_line:
            axis[2].axhline(y=0, color='black', linewidth=1.5)

    else:
        figure, axis = plt.subplots(3, 1)

        axis[0].plot(T, A)
        axis[0].set_title("Spectral Acceleration")

        axis[1].plot(T, V)
        axis[1].set_title("Spectral Velocity")

        axis[2].plot(T, D)
        axis[2].set_title("Spectral Displacement")

    figure.suptitle("Response History Spectrum: "+name)
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing
    # plt.show()

    return figure

def plotRSH(disp, vel, accel, time, g_accel=None, name=""):
    grid_on = False
    x_line = True

    n = 4
    if g_accel is None:
        n = 3
        figure, axis = plt.subplots(n, 1, figsize=(10, 8))
    else:
        n = 4
        figure, axis = plt.subplots(n, 1, figsize=(10, 8))
        axis[0].plot(time, g_accel)
        axis[0].set_title("Ground Accel")
        axis[0].set_xlabel('Time (s)')
        axis[0].set_ylabel('Acceleration')
        axis[0].grid(grid_on)
        if x_line:
            axis[0].axhline(y=0, color='black', linewidth=1.5)

    axis[n - 3].plot(time, accel)
    axis[n - 3].set_title("Acceleration")
    axis[n - 3].set_xlabel('Time (s)')
    axis[n - 3].set_ylabel('Acceleration')
    axis[n - 3].grid(grid_on)
    if x_line:
        axis[n - 3].axhline(y=0, color='black', linewidth=1.5)

    axis[n - 2].plot(time, vel)
    axis[n - 2].set_title("Velocity")
    axis[n - 2].set_xlabel('Time (s)')
    axis[n - 2].set_ylabel('Velocity')
    axis[n - 2].grid(grid_on)
    if x_line:
        axis[n - 2].axhline(y=0, color='black', linewidth=1.5)

    axis[n - 1].plot(time, disp)
    axis[n - 1].set_title("Displacement")
    axis[n - 1].set_xlabel('Time (s)')
    axis[n - 1].set_ylabel('Displacement')
    axis[n - 1].grid(grid_on)
    if x_line:
        axis[n - 1].axhline(y=0, color='black', linewidth=1.5)

    figure.suptitle("Response History: " + name)
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing
    # plt.show()
    return figure