from EQ_Data import Sin_EQ, EQ_Data
from Integrators.Duhamel import duhamel
from Integrators.GroundMotionIntegrator import groundMotionIntegrator
from Integrators.Newmark import newmarkBeta, newmarkBeta_GroundMotion
import numpy as np
import matplotlib.pyplot as plt

from Plotters.RSH_Plotters import plotRSH, plotDVASpectrum
from Response_History.SpectralValues import getFullSpectralDVA_zeta_range, getFullSpectralDVA_T_range

file_path = 'EQ_List/El_Centro-NS-Imperial_Valley-SI.txt'
eq_data_read = np.loadtxt(file_path)

time_arr=eq_data_read[:, 0]
ground_accel=eq_data_read[:, 1]

el_centro=EQ_Data(time_arr, ground_accel, g_units=False)
time_arr=el_centro.time
ground_accel=el_centro.ground_accel

# eq_data=Sin_EQ(amplitude=10, frequency=2*np.pi/1.2, t_end=1.2, t_step=0.1)
# time_arr=eq_data.time
# ground_accel=eq_data.ground_accel
# time_arr=np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
# ground_accel=np.array([0, 5, 8.6602, 10.0, 8.6603, 5, 0,0,0,0,0])


# time_arr=np.linspace(0,10,2000)
# ground_accel=np.sin(time_arr)
# zeta=0.15
# wn=3
zeta=0
wn=np.sqrt(40/0.1)
wd = wn*np.sqrt(1 - zeta ** 2)
z_max=max(abs(ground_accel))
# disp_d, vel_d, accel_d = duhamel(ground_accel, time_arr, wn=4*np.pi, zeta=0.15)
disp, vel, accel = newmarkBeta_GroundMotion(ground_accel, time_arr, wn=4*np.pi, zeta=0.15, m=1, g_units=False)
# disp, vel, accel = newmarkBeta(ground_accel, time_arr, wn=6.283, zeta=0.05, m=0.2533)
impulse_resp_func = (wn**2 / (wd*z_max)) * np.exp(-zeta * wn * time_arr) * np.sin(wd * time_arr)

# disp, vel, accel, time = groundMotionIntegrator([time_arr, ground_accel])

# plt.plot(time_arr, impulse_resp_func)
#
# disp, vel, accel = newmarkBeta(ground_accel, time_arr, wn=6.283, zeta=0.05, m=0.2533)

#  add displacement and vel adder
# zeta_range=[0.01,0.02, 0.03]
# D,V,A,T = getFullSpectralDVA_T_range(el_centro, T=np.arange(0.04, 5, 0.01), zeta=zeta_range)
# plotDVASpectrum(D,V,A,T, zeta=zeta_range)

plotRSH(disp,vel,accel,time_arr)
# plotRSH(disp_d,vel_d,accel_d,time_arr)
# plt.plot(time_arr, ground_accel)
# plt.plot(time_arr2, ground_accel2)
# plt.plot(time_arr3, ground_accel3)
# plt.plot(time_arr4, ground_accel4)
plt.show()