import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter

from Constants import *


# https://github.com/anismhd/TRIPARTITE/blob/master/tripartite.py

def tripartite_axis(axis, name):
    plt.rcParams['font.family'] = 'serif'
    axis.set_xscale('log')
    axis.set_yscale('log')
    axis.set_aspect('equal')
    xlim = axis.get_xlim()
    axis.set_xlim(xlim)
    ylim = axis.get_ylim()
    axis.set_ylim(ylim)

    axis.xaxis.set_major_formatter(FuncFormatter(lambda val, pos: format_number(val)))
    axis.yaxis.set_major_formatter(FuncFormatter(lambda val, pos: format_number(val)))

    # Optional: To make sure all ticks are shown as numbers
    # axis.ticklabel_format(style='plain', axis='both')


    tick_font_size = axis.get_xticklabels()[0].get_fontsize()
    # TODO use a label keyword
    axis.grid(True, which='both', color='k', linestyle='-', alpha=.3, lw=.3)
    axis.set_xlabel('Period (sec.)')
    axis.set_ylabel('Pseudo Velocity (m/s)')
    axis.set_title(name)
    a_c = 2 * np.pi / g_list[working_units]
    d_c = 1 / (2 * np.pi)

    # acc_axis
    axis.plot(xlim, 10 ** (1 / (2 * np.pi)) / np.array(xlim), c='k', lw=1)
    # # d_axis
    axis.plot(xlim, 10 ** (2 * np.pi / g_list[working_units]) * np.array(xlim) / 2 * np.pi, c='k', lw=1)

    # Finding the middle point of the graph
    xcenter = 10 ** (0.5 * sum(np.log10(xlim)))
    ycenter = 10 ** (0.5 * sum(np.log10(ylim)))

    # Finding minimum and maximum value of displacement and accelaration
    log10DISP_min = np.floor(np.log10(ylim[0] * xlim[0] / (2 * np.pi)))
    log10DISP_max = min(np.ceil(np.log10(ylim[1] * xlim[1] / (2 * np.pi))), 1)
    log10DISP_mid = (log10DISP_max + log10DISP_min) * 0.4
    log10ACCL_min = np.floor(np.log10(ylim[0] * 2 * np.pi / xlim[1]))
    log10ACCL_max = min(np.ceil(np.log10(ylim[1] * 2 * np.pi / xlim[0])), 2)
    log10ACCL_mid = (log10ACCL_max + log10ACCL_min) * 0.4

    C1 = 0.5 * (sum(np.log10(ylim)) - sum(np.log10(xlim)))
    C2 = 0.5 * (sum(np.log10(ylim)) + sum(np.log10(xlim)))
    bbox = {'fc': '0.8', 'pad': 0}

    for accl in range(int(log10ACCL_min), int(log10ACCL_max) + 1):
        # formatted_number = r"$10^{" + f"{accl}" + r"}$"
        formatted_number = format_number(10 ** accl)
        axis.plot(xlim, 10 ** accl * np.array(xlim) / 2 * np.pi, c='k', lw=.7, alpha=.3)

        l_a = accl + 1
        l_d = -2 * np.pi / g_list[working_units]
        loc_v = np.sqrt(10 ** (l_d) * 10 ** (l_a))

        loc_t = 2 * np.pi * 10 ** (l_d) / loc_v

        if (loc_v >= ylim[0]) and (loc_v <= ylim[1]) and (loc_t >= xlim[0]) and (loc_t <= xlim[1]):
            axis.text(loc_t, loc_v, formatted_number,
                    ha='center', va='center', rotation=45, color='k', fontsize=tick_font_size,
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'), family='Times New Roman')

        for i in range(1, 10):
            axis.plot(xlim, 10 ** accl * i * np.array(xlim) / 2 * np.pi, c='k', lw=.5, alpha=.3)

    for disp in range(int(log10DISP_min), int(log10DISP_max) + 1):
        # formatted_number = r"$10^{" + f"{disp}" + r"}$"  # LaTeX style for power of 10
        formatted_number=format_number(10**disp)
        axis.plot(xlim, 10 ** disp * 2 * np.pi / np.array(xlim), c='k', lw=.5, alpha=.3)

        offset_a = 0.1
        l_a = (1 / (2 * np.pi)) * g_list[working_units] + offset_a
        l_d = disp
        loc_v = np.sqrt(10 ** (l_d) * 10 ** (l_a))

        loc_t = 2 * np.pi * 10 ** (l_d) / loc_v
        if (loc_v >= ylim[0]) and (loc_v <= ylim[1]) and (loc_t >= xlim[0]) and (loc_t <= xlim[1]):
            axis.text(loc_t, loc_v, formatted_number,
                     horizontalalignment='center', rotation=-45,
                    verticalalignment='center', color='k', fontsize=tick_font_size,
                    bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'), family='Times New Roman')


        for i in range(1, 10):
            axis.plot(xlim, 10 ** (disp) * i * 2 * np.pi / np.array(xlim), c='k', lw=.5, alpha=.3)

    # axis.plot([10 ** loc_x, 5], [10 ** loc_y, 5], color='k', linewidth=2)
    return axis


def tripartitePlot(D, V, A, T, name="Tri-Log Plot"):
    plt.rcParams['font.family'] = 'serif'
    fig = plt.figure()
    fig.set_size_inches(6.5, 5)
    ax = plt.gca()
    # ax.plot(T, V, c='k', alpha=0)
    ax.plot(T, V, c='k')

    ax = tripartite_axis(ax, name=name)
    # plt.show()
    #
    # if save:
    #     plt.savefig(filename)
    # plt.show()
    return fig

def tripartitePlotSeries(D, V, A, T, name="Tri-Log Plot", legend_list=None):
    plt.rcParams['font.family'] = 'serif'
    fig = plt.figure()
    fig.set_size_inches(6,5)
    ax = plt.gca()
    # ax.plot(T, V, c='k')
    for i in range(V.shape[2]):
        ax.plot(T,V[:,0,i],label=legend_list[i], lw=1)
    # plt.show()
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax = tripartite_axis(ax, name=name)
    #
    # if save:
    #     plt.savefig(filename)
    # plt.show()
    return fig


def format_number(num):
    # If the number is very close to an integer (within a small tolerance), treat it as an integer
    if num.is_integer():
        return f"{int(num)}"  # No decimals for whole numbers
    else:
        # Otherwise, show the number with significant decimals
        return f"{num:.10g}"  # Adjust precision for significant digits (up to 10 significant digits)

# Example values
accl = 0.00123  # Example acceleration value
formatted_number = format_number(accl)

#
# x = np.logspace(-2.1, 1.6, 100)  # Generates 100 points from 10^-1 to 10^2
# y = x  # A function of x to plot
#
# fig=tripartitePlot(y,y,y,x, " ")
# fig.savefig("Tripartite Blank2.png", dpi=600)
# # fig = tripartitePLot(periods, PGV)
# # # plt.savefig('bis_spectra.pdf')
# # plt.show()
