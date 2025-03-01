from EQ_Data import Sin_EQ, EQ_Data
from Integrators.Duhamel import duhamel
from Integrators.GroundMotionIntegrator import groundMotionIntegrator
from Integrators.Newmark import newmarkBeta, newmarkBeta_GroundMotion
import numpy as np
import matplotlib.pyplot as plt

from Plotters.RSH_Plotters import plotRSH, plotDVASpectrum
from Response_History.SpectralValues import getFullSpectralDVA_T_range

file_path = 'EQ_List/El_Centro-NS-Imperial_Valley-SI.txt'
eq_data_read = np.loadtxt(file_path)

time_arr=eq_data_read[:, 0]
ground_accel=eq_data_read[:, 1]

el_centro=EQ_Data(time_arr, ground_accel, g_units=False)
time_arr=el_centro.time
ground_accel=el_centro.ground_accel


# disp_d, vel_d, accel_d = duhamel(ground_accel, time_arr, wn=4*np.pi, zeta=0.15)
disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn=4*np.pi, zeta=0.15, m=1, g_units=False)

plotRSH(disp,vel,accel,time_arr)
plt.show()

zeta_range=[0.01,0.02, 0.03]
D,V,A,T = getFullSpectralDVA_T_range(el_centro, T=np.arange(0.04, 5, 0.01), zeta=zeta_range)
plotDVASpectrum(D,V,A,T, zeta=zeta_range)

