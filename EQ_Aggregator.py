import numpy as np

from EQ_Aggregator_Scripts.Aggregate_Statistics import meanSpectrum, meanSpectrumStatistics
from EQ_Aggregator_Scripts.Design_Spectrum_Plotter import plotDesignSpectrum, plotDesignSpectrumStatistics
from EQ_Aggregator_Scripts.RS_Plotters_Aggregate import plotDVASpectrum_Aggregate
from EQ_Aggregator_Scripts.Spectral_Values_Aggregate import getFullSpectralDVA_Aggregate
from EQ_Aggregator_Scripts.Tripartite__Plot import tripartitePlot
from EQ_Loader import EQ_Loader
from Integrators.Newmark import newmarkBeta_GroundMotion
from Plotters.RSH_Plotters import plotRSH

eq_list=EQ_Loader(files=['SierraMadre-00-Altadena-g.txt', 'LAquila-EW-Antrodoco-g.txt'])

# for eq in eq_list:
#     disp, vel, accel = newmarkBeta_GroundMotion(eq.ground_accel, eq.time, wn=4 * np.pi, zeta=0.15, m=1, g_units=False)
#     plotRSH(disp, vel, accel, eq.time)
#     # plt.show()

zeta=[0.05]
D,V,A,T=getFullSpectralDVA_Aggregate(eq_list, T=np.arange(0.04,3,0.01), zeta=zeta)
plotDVASpectrum_Aggregate(D,V,A,T, eq_list, zeta_list=zeta, zeta=0.05)

# accel_design_spectrum, T=designSpectrum(A, T)
# plotDesignSpectrum(accel_design_spectrum,T)
# print()
distribution, X, Y =  meanSpectrumStatistics(A, T, mode='mean')
fig=plotDesignSpectrumStatistics(distribution, X, Y)
fig.show()
# h=tripartitePlot(D[:,0,1],V[:,0,1],A[:,0,1],T)
# h.show()
# print(V)