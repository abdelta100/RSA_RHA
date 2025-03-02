import numpy as np

from EQ_Aggregator_Scripts.Aggregate_Statistics import designSpectrum, designSpectrumStatistics
from EQ_Aggregator_Scripts.Design_Spectrum_Plotter import plotDesignSpectrum, plotDesignSpectrumStatistics
from EQ_Aggregator_Scripts.RS_Plotters_Aggregate import plotDVASpectrum_Aggregate
from EQ_Aggregator_Scripts.Spectral_Values_Aggregate import getFullSpectralDVA_Aggregate, getFullSpectralDPVPA_Aggregate
from EQ_Aggregator_Scripts.Tripartite__Plot import tripartitePlot
from EQ_Loader import EQ_Loader
from Integrators.Newmark import newmarkBeta_GroundMotion
from Plotters.RSA_Plotters import plotDPVPASpectrum
from Plotters.RSH_Plotters import plotRSH, plotDVASpectrum
from Response_History.SpectralValues import getFullSpectralDVA_T_range
from Response_Spectrum.PsuedoSpectralValues import getFullSpectralDPVPA_T_range

eq_list=EQ_Loader(files=['Alkion-EW-OTE_Building-SI.txt', 'El_Centro-NS-Imperial_Valley-SI.txt', 'Unknown-NS-random-g.txt'])

# for eq in eq_list:
#     disp, vel, accel = newmarkBeta_GroundMotion(eq.ground_accel, eq.time, wn=4 * np.pi, zeta=0.15, m=1, g_units=False)
#     plotRSH(disp, vel, accel, eq.time)
#     # plt.show()

save_dir='CEE572_A2_Deliverables/'
file_typ=".png"

for eq in eq_list:
    # Plot spectral response plots individually
    zeta = [0.05]
    D, V, A, T = getFullSpectralDVA_T_range(eq, T=np.arange(0.04, 3, 0.01), zeta=zeta)
    fig=plotDVASpectrum(D, V, A, T, zeta)
    fig.savefig(save_dir+eq.meta_name+"Spectral_Response"+file_typ)

    # Plot pseudo response plots individually
    zeta = [0.05]
    D, PV, PA, T = getFullSpectralDPVPA_T_range(eq, T=np.arange(0.04, 3, 0.01), zeta=zeta)
    fig = plotDPVPASpectrum(D, PV, PA, T, zeta)
    fig.savefig(save_dir + eq.meta_name+"PseudoSpectral_Response"+file_typ)


# Following two steps not required i think
# PLot collective spectral response plot
zeta=[0.05]
D,V,A,T=getFullSpectralDVA_Aggregate(eq_list, T=np.arange(0.04,3,0.01), zeta=zeta)
fig=plotDVASpectrum_Aggregate(D,V,A,T, eq_list, zeta_list=zeta, zeta=0.05)
fig.savefig(save_dir+ "Collective Spectral Response"+file_typ)

# PLot collective pseudo response plot
zeta=[0.05]
D,PV,PA,T=getFullSpectralDPVPA_Aggregate(eq_list, T=np.arange(0.04,3,0.01), zeta=zeta)
fig=plotDVASpectrum_Aggregate(D,PV,PA,T, eq_list, zeta_list=zeta, zeta=0.05)
fig.savefig(save_dir+ "Collective Pseudo Spectral Response"+file_typ)

# plot mean spectral response (Clarify if pseudo or spectral acc, since disp is common to both)
# accel_design_spectrum, T=designSpectrum(A, T)
# plotDesignSpectrum(accel_design_spectrum,T)

# Plot probability heatmap, not required but looks nice, CHeck what spectrum is being plotted
# heatmap savefig is problematic
distribution, X, Y =  designSpectrumStatistics(A, T , mode='mean')
fig=plotDesignSpectrumStatistics(distribution, X, Y)
fig.savefig(save_dir+ "Collective Spectral Probability Map"+file_typ)


# Figure what needs to be in g units

for eq in eq_list:
    # Plot tripartite plot for each
    print("TBD")
    # tripartitePlot(D[:, 0, 1], V[:, 0, 1], A[:, 0, 1], T)


# plot design spectrum at mean


# plot design spectrum at mean+1sigma (Clarify)



# Create a design spectrum (sorry for the confusion this is a created spectrum, will need to check)

# Save data to excel sheet

