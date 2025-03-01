import numpy as np
import matplotlib.pyplot as plt


# https://github.com/anismhd/TRIPARTITE/blob/master/tripartite.py

def tripartite_axis(axis):
    axis.set_xscale('log')
    axis.set_yscale('log')
    axis.set_aspect('equal')
    xlim = axis.get_xlim()
    axis.set_xlim(xlim)
    ylim = axis.get_ylim()
    axis.set_ylim(ylim)
    tick_font_size = axis.get_xticklabels()[0].get_fontsize()

    axis.grid(True, which='both', color='k', linestyle='-', alpha=.3, lw=.3)
    axis.set_xlabel('Period (sec.)')
    axis.set_ylabel('Spectral Velocity')

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
        axis.plot(xlim, 10 ** accl * np.array(xlim) / (2 * np.pi), c='k', lw=.5, alpha=.3)
        loc_x = -0.5 * (accl - np.log10(2 * np.pi) - C2)
        loc_y = -loc_x + C2
        axis.text(10 ** loc_x, 10 ** loc_y, "{:.1g}".format(10 ** accl),
                  ha='center', va='center', rotation=45, color='k', fontsize=tick_font_size,
                  bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

        for i in range(1, 10):
            axis.plot(xlim, 10 ** accl * i * np.array(xlim) / (2 * np.pi), c='k', lw=.5, alpha=.3)

    for disp in range(int(log10DISP_min), int(log10DISP_max) + 1):
        formatted_number = r"$10^{" + f"{disp}" + r"}$"  # LaTeX style for power of 10
        axis.plot(xlim, 10 ** disp * 2 * np.pi / np.array(xlim), c='k', lw=.5, alpha=.3)
        loc_x = 0.5 * (disp + np.log10(2 * np.pi) - C1)
        loc_y = loc_x + C1
        axis.text(10 ** loc_x, 10 ** loc_y, formatted_number,
                  horizontalalignment='center', rotation=-45,
                  verticalalignment='center', color='k', fontsize=tick_font_size,
                  bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

        for i in range(1, 10):
            axis.plot(xlim, 10 ** (disp) * i * 2 * np.pi / np.array(xlim), c='k', lw=.5, alpha=.3)

    axis.plot(xlim, 10 ** (log10DISP_mid) * 2 * np.pi / np.array(xlim), c='k', lw=1)
    axis.plot(xlim, 10 ** (log10ACCL_mid) * np.array(xlim) / (2 * np.pi), c='k', lw=1)
    # axis.plot([10 ** loc_x, 5], [10 ** loc_y, 5], color='k', linewidth=2)
    return axis


def tripartitePlot(D, V, A, T):
    fig = plt.figure()
    ax = plt.gca()
    ax.plot(T, V, c='k')
    ax = tripartite_axis(ax)
    plt.show()


# fig = tripartitePLot(periods, PGV)
# # plt.savefig('bis_spectra.pdf')
# plt.show()
