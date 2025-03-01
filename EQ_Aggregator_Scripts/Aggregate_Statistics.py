from statistics import stdev

import numpy as np
import scipy.stats as stats

def designSpectrum(DVA_arr, T, sigma=0):

    mean=np.mean(DVA_arr, axis=(1, 2))
    std=np.std(DVA_arr,axis=(1, 2))

    design_spectrum=mean+sigma*std

    return design_spectrum, T

def designSpectrumStatistics(DVA_arr, T , mode='mean'):
    # Not using heavy tailed distribution
    max_lim=np.max(DVA_arr)*1.5
    p_lim=np.linspace(0, max_lim, 200)
    X,Y=np.meshgrid(T, p_lim)
    # bin size used for pdf to pmf
    bin_size = p_lim[1] - p_lim[0]
    mean = np.mean(DVA_arr, axis=2)
    std = np.std(DVA_arr, axis=2)

    mean_broadcasted = mean[:, None]  # Shape (998, 1) -> Broadcasts along Y (200, 98)
    std_broadcasted = std[:, None]
    print(mean)
    print(std)
    print(X)
    print(Y)
    if mode == 'mean':

        # stats.norm.pdf(DVA_arr)
        # distribution = stats.norm.pdf(DVA_arr, loc=mean, scale=std)
        distribution = stats.norm.pdf(Y, loc=mean_broadcasted.T, scale=std_broadcasted.T)
        distribution = (bin_size) * distribution

    if mode == 'stdev':

        # stats.norm.pdf(DVA_arr)
        distribution = 1-(stats.norm.cdf(Y, loc=mean_broadcasted.T, scale=std_broadcasted.T))
    #     TODO dont bin this

    distribution = np.squeeze(distribution)
    print(distribution)
    return distribution, X, Y