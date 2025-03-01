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
    axis.legend(loc='upper right')
    if x_line:
        axis.axhline(y=0, color='black', linewidth=1.5)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Adjust vertical spacing
    plt.show()


import matplotlib.pyplot as plt
import numpy as np


def plotDesignSpectrumStatistics(distribution, X, Y, cmap='viridis', title='Design Spectrum Statistics',
                                 xlabel='X-axis', ylabel='Y-axis', log_scale=False, contour=False, lognorm=False):
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
    # Create a figure and axis
    plt.figure(figsize=(10, 6))
    max_dist=np.max(distribution)
    min_dist=np.min(distribution)
    print(max_dist)

    if log_scale:
        plt.xscale('log')
        plt.yscale('log')
        plt.gca().set_aspect('auto')
    # Plot the heatmap using pcolormesh or imshow
    if lognorm:
        plt.pcolormesh(X, Y, distribution, cmap=cmap, shading='nearest', norm=LogNorm(vmin=0.01, vmax=max_dist))
    else:
        plt.pcolormesh(X, Y, distribution, cmap=cmap, shading='nearest')
    # Add a color bar to show the scale of values
    cbar = plt.colorbar()
    cbar.set_label('Distribution Value')

    # Add labels and title
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Optionally, add contour lines for additional visual detail
    if contour:
        plt.contour(X, Y, distribution, 10, linewidths=0.5, colors='black')

    # Show the plot
    plt.show()

# Example Usage
# Assuming distribution, X, and Y are already defined
# distribution, X, Y = designSpectrumStatistics(DVA_arr, T, mode='mean')

# Example: Plot the distribution
# plotDesignSpectrumStatistics(distribution, X, Y)


