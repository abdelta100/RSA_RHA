import warnings
from operator import index

import numpy as np
from matplotlib import pyplot as plt

from EQ_Data import EQ_Data


def plotDVASpectrum_Aggregate(D, V, A, T, eq_list: list[EQ_Data], zeta_list=None, zeta=None):
    figure, axis = plt.subplots(3, 1, figsize=(10, 8))
    grid_on = False
    x_line = True

    if isinstance(eq_list, EQ_Data):
        eq_list=[eq_list]

    if zeta is None:
        zeta=zeta_list[0]

    try:
        z=zeta_list.index(zeta)
    except ValueError:
        warnings.warn(f"Warning: {zeta} not found in zeta_list. Setting z to 0. Try passing a float instead of a list to parameter zeta")
        z = 0

    if isinstance(eq_list, (list, np.ndarray)):
        for i, eq in enumerate(eq_list):
            axis[0].plot(T,A[: , z , i], label=eq.meta_name)
        axis[0].set_title("Spectral Acceleration")
        axis[0].set_xlabel('Time Period (s)')
        axis[0].set_ylabel('Acceleration')
        axis[0].grid(grid_on)
        axis[0].legend(loc='upper right')
        if x_line:
            axis[0].axhline(y=0, color='black', linewidth=1.5)

    if isinstance(eq_list, (list, np.ndarray)):
        for i, eq in enumerate(eq_list):
            axis[1].plot(T, V[: , z , i], label=eq.meta_name)
        axis[1].set_title("Spectral Velocity")
        axis[1].set_xlabel('Time Period(s)')
        axis[1].set_ylabel('Velocity')
        axis[1].grid(grid_on)
        axis[1].legend(loc='upper right')
        if x_line:
            axis[0].axhline(y=0, color='black', linewidth=1.5)

    if isinstance(eq_list, (list, np.ndarray)):
        for i, eq in enumerate(eq_list):
            axis[2].plot(T, D[: , z , i], label=eq.meta_name)
        axis[2].set_title("Spectral Displacement")
        axis[2].set_xlabel('Time Period(s)')
        axis[2].set_ylabel('Displacement')
        axis[2].grid(grid_on)
        axis[2].legend(loc='upper right')
        if x_line:
            axis[0].axhline(y=0, color='black', linewidth=1.5)

    else:
        figure, axis = plt.subplots(3, 1)

        axis[0].plot(T, A)
        axis[0].set_title("Spectral Acceleration")

        axis[1].plot(T, V)
        axis[1].set_title("Spectral Velocity")

        axis[2].plot(T, D)
        axis[2].set_title("Spectral Displacement")

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing
    plt.show()


    def DVA_trilog_plot():
        return 0