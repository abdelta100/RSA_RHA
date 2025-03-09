from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm


def plotDesignSpectrum(design_spectrum, T, property= "Acceleration"):
    figure, axis = plt.subplots(1, 1, figsize=(5, 8))
    grid_on = False
    x_line = True

    axis.plot(T, design_spectrum)
    axis.set_title("Design Spectrum " + property)
    axis.set_xlabel('Time Period (s)')
    axis.set_ylabel(property)
    axis.grid(grid_on)
    # axis.legend(loc='upper right')
    if x_line:
        axis.axhline(y=0, color='black', linewidth=1.5)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing
    # plt.show()
    return figure


import matplotlib.pyplot as plt
import numpy as np


def plotDesignSpectrumStatistics(distribution, X, Y, cmap='viridis', title='Probability Map for Design Spectrum',
                                 xlabel='Time Period (s)', ylabel='Acceleration', log_scale=False, contour=False, lognorm=False, mode="mean"):
    """
    Plots a heatmap or contour plot of the distribution over the meshgrid (X, Y).

    Parameters:
        distribution (2D array): The computed distribution values (PDF or CDF) over the meshgrid.
        X (2D array): The X coordinates of the meshgrid.
        Y (2D array): The Y coordinates of the meshgrid.
        cmap (str): The colormap to use for the plot.
        title (str): Title of the plot.
        xlabel (str): Label for the X-axis.
        ylabel (str): Label for the Y-axis.
    """

    figure = plt.figure(figsize=(10, 6))

    axes = figure.add_subplot(111)

    max_dist=np.max(distribution)
    min_dist=np.min(distribution)
    print(max_dist)

    if log_scale:
        axes.set_xscale('log')
        axes.set_yscale('log')
        axes.set_aspect('auto')
    # Plot the heatmap using pcolormesh or imshow
    if lognorm:
        pcm=axes.pcolormesh(X, Y, distribution, cmap=cmap, shading='nearest', norm=LogNorm(vmin=0.01, vmax=max_dist))
    else:
        pcm=axes.pcolormesh(X, Y, distribution, cmap=cmap, shading='nearest')

    cbar = figure.colorbar(pcm, ax=axes)
    if mode=="mean":
        cbar.set_label('Probability (Mass Function)')
    else:
        cbar.set_label('Cumulative Probability')
    # Add labels and title
    axes.set_title(title)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)

    if contour:
        axes.contour(X, Y, distribution, 10, linewidths=0.5, colors='black')

    # Show the plot
    # plt.show()
    # return plt.gcf()
    return figure

# Example Usage
# Assuming distribution, X, and Y are already defined
# distribution, X, Y = designSpectrumStatistics(DVA_arr, T, mode='mean')

# Example: Plot the distribution
# plotDesignSpectrumStatistics(distribution, X, Y)


