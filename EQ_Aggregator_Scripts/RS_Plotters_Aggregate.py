import warnings
from operator import index

import numpy as np
from matplotlib import pyplot as plt

from EQ_Data import EQ_Data


def plotDVASpectrum_Aggregate(D, V, A, T, eq_list: list[EQ_Data], zeta_list=None, zeta=None, legend_on=True, mode="Pseudo", isloglog=False, grid_on=False):
    figure, axis = plt.subplots(3, 1, figsize=(12, 13))
    grid_on = grid_on
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

    if mode=="Pseudo":
        veltitle="Pseudo Velocity"
        acceltitle="Pseudo Acceleration"
    else:
        veltitle = "Velocity"
        acceltitle = "Acceleration"


    if isinstance(eq_list, (list, np.ndarray)):
        for i, eq in enumerate(eq_list):
            axis[0].plot(T,A[: , z , i], label=eq.meta_name)

        if isloglog:
            axis[0].set_xscale('log')
            axis[0].set_yscale('log')

        axis[0].set_title(acceltitle)
        axis[0].set_xlabel('Time Period (s)')
        axis[0].set_ylabel(acceltitle+ ' g')
        # axis[0].set_aspect('equal')
        axis[0].grid(grid_on)

        if legend_on:
            box = axis[0].get_position()
            axis[0].set_position([box.x0, box.y0, box.width * 0.8, box.height])

            # Put a legend to the right of the current axis
            axis[0].legend(loc='center left', bbox_to_anchor=(1, 0.5))
            # axis[0].legend(loc='upper right')
        if x_line:
            axis[0].axhline(y=0, color='black', linewidth=1.5)

    if isinstance(eq_list, (list, np.ndarray)):
        for i, eq in enumerate(eq_list):
            axis[1].plot(T, V[: , z , i], label=eq.meta_name)

        if isloglog:
            axis[1].set_xscale('log')
            axis[1].set_yscale('log')

        axis[1].set_title(veltitle)
        axis[1].set_xlabel('Time Period(s)')
        axis[1].set_ylabel(veltitle + ' (m/s)')
        # axis[1].set_aspect('equal')
        axis[1].grid(grid_on)
        if legend_on:
            box = axis[1].get_position()
            axis[1].set_position([box.x0, box.y0, box.width * 0.8, box.height])

            # Put a legend to the right of the current axis
            axis[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
            # axis[1].legend(loc='upper right')
        if x_line:
            axis[1].axhline(y=0, color='black', linewidth=1.5)

    if isinstance(eq_list, (list, np.ndarray)):
        for i, eq in enumerate(eq_list):
            axis[2].plot(T, D[: , z , i], label=eq.meta_name)

        if isloglog:
            axis[2].set_xscale('log')
            axis[2].set_yscale('log')

        axis[2].set_title("Displacement")
        axis[2].set_xlabel('Time Period(s)')
        axis[2].set_ylabel('Displacement (m)')
        # axis[2].set_aspect('equal')
        axis[2].grid(grid_on)
        if legend_on:
            box = axis[2].get_position()
            axis[2].set_position([box.x0, box.y0, box.width * 0.8, box.height])

            # Put a legend to the right of the current axis
            axis[2].legend(loc='center left', bbox_to_anchor=(1, 0.5))
            # axis[2].legend(loc='upper right')
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

    if mode=="Pseudo":
        figure.suptitle("Pseudo-Response Spectrum", fontsize=16, fontweight='bold')

    else:
        figure.suptitle("Actual Response Spectrum", fontsize=16, fontweight='bold')


    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5, right=0.65)  # Adjust vertical spacing
    # plt.show()
    return figure


    def DVA_trilog_plot():
        return 0