import numpy as np
import pandas as pd

from EQ_Aggregator_Scripts.Aggregate_Statistics import meanSpectrum, meanSpectrumStatistics
from EQ_Aggregator_Scripts.Design_Spectrum_Plotter import plotDesignSpectrum, plotDesignSpectrumStatistics
from EQ_Aggregator_Scripts.RS_Plotters_Aggregate import plotDVASpectrum_Aggregate
from EQ_Aggregator_Scripts.Spectral_Values_Aggregate import getFullSpectralDVA_Aggregate, getFullSpectralDPVPA_Aggregate
from EQ_Aggregator_Scripts.Tripartite__Plot import tripartitePlot, tripartitePlotSeries
from EQ_Loader import EQ_Loader
from Integrators.Newmark import newmarkBeta_GroundMotion
from LoadExcel import loadExcelDVAPVPA
from Plotters.RSA_Plotters import plotDPVPASpectrum
from Plotters.RSH_Plotters import plotRSH, plotDVASpectrum
from Response_History.FullSpectralAll import getFullSpectralAll
from Response_History.SpectralValues import getFullSpectralDVA_T_range
from Response_Spectrum.PsuedoSpectralValues import getFullSpectralDPVPA_T_range
from Constants import *
import matplotlib.pyplot as plt

eq_list = EQ_Loader()
# eq_list=EQ_Loader(files=['BearCity-EW-ParkHill-g.txt', 'Denali-90-AnchorageK202-g.txt', 'ChiChi_Taiwan04-NS-CHY024-g.txt'])
# for eq in eq_list:
#     disp, vel, accel = newmarkBeta_GroundMotion(eq.ground_accel, eq.time, wn=4 * np.pi, zeta=0.15, m=1, g_units=False)
#     plotRSH(disp, vel, accel, eq.time)
#     # plt.show()

save_dir = 'CEE572_A2_Deliverables/'
file_typ = ".png"
#
# excel_writer = pd.ExcelWriter(save_dir + "earthquake_spectral_data.xlsx", engine='openpyxl')
T_range = np.arange(0.01, 10, 0.01)
# for i, eq in enumerate(eq_list):
#     print(eq.name)
#     # # Plot spectral response plots individually
#     # zeta = [0.05]
#     # D, V, A, T = getFullSpectralDVA_T_range(eq, T=T_range, zeta=zeta)
#     # fig=plotDVASpectrum(D, V, A, T, zeta, name=eq.name)
#     # fig.savefig(save_dir+eq.meta_name+"Spectral_Response"+file_typ)
#     # plt.close(fig)
#     #
#     # # Plot pseudo response plots individually
#     # zeta = [0.05]
#     # D, PV, PA, T = getFullSpectralDPVPA_T_range(eq, T=T_range, zeta=zeta)
#     # fig = plotDPVPASpectrum(D, PV, PA, T, zeta, name=eq.name)
#     # fig.savefig(save_dir + eq.meta_name+"PseudoSpectral_Response"+file_typ)
#     # plt.close(fig)
#
#     zeta = [0.05]
#     D, V, A, PV, PA, T = getFullSpectralAll(eq, T=T_range, zeta=zeta)
#
#     A = A / g_list[working_units]
#     PA = PA / g_list[working_units]
#
#     fig = plotDVASpectrum(D, V, A, T, zeta, name=eq.name)
#     fig.savefig(save_dir + eq.meta_name + "Actual_Response" + file_typ)
#     plt.close(fig)
#
#     fig = plotDPVPASpectrum(D, PV, PA, T, zeta, name=eq.name)
#     fig.savefig(save_dir + eq.meta_name + "Pseudo_Response" + file_typ)
#     plt.close(fig)
#
#     fig = plotDVASpectrum(D, V, A, T, zeta, name=eq.name, isloglog=True)
#     fig.savefig(save_dir + eq.meta_name + "Actual_Response LogLog" + file_typ)
#     plt.close(fig)
#
#     fig = plotDPVPASpectrum(D, PV, PA, T, zeta, name=eq.name, isloglog=True)
#     fig.savefig(save_dir + eq.meta_name + "Pseudo_Response LogLog" + file_typ)
#     plt.close(fig)
#
#     df = pd.DataFrame({
#         'Period (T)': T,
#         'Displacement (D)': D[:, 0],
#         'Velocity (V)': V[:, 0],
#         'Acceleration (A)': A[:, 0],
#         'Pseudo Velocity (PV)': PV[:, 0],
#         'Pseudo Acceleration (PA)': PA[:, 0]
#     })
#
#     sheet_name = eq.name[:31]
#     df.to_excel(excel_writer, sheet_name=sheet_name, index=False)
# # Save the Excel file
# excel_writer._save()

# Load Data from excel
D, V, A, PV, PA, T = loadExcelDVAPVPA(save_dir + "earthquake_spectral_data.xlsx")
# Following two steps not required i think
# PLot collective spectral response plot
zeta = [0.05]
# D,V,A,T=getFullSpectralDVA_Aggregate(eq_list, T=T_range, zeta=zeta)
# fig=plotDVASpectrum_Aggregate(D,V,A,T, eq_list, zeta_list=zeta, zeta=0.05, mode="History")
# fig.savefig(save_dir+ "Collective Spectral Response"+file_typ)
# plt.close(fig)

# PLot collective pseudo response plot
# zeta=[0.05]
# D,PV,PA,T=getFullSpectralDPVPA_Aggregate(eq_list, T=T_range, zeta=zeta)
# fig=plotDVASpectrum_Aggregate(D,PV,PA,T, eq_list, zeta_list=zeta, zeta=0.05, mode="Pseudo")
# fig.savefig(save_dir+ "Collective Pseudo Spectral Response"+file_typ)
# plt.close(fig)
zeta = [0.05]

# T=T_range

fig = plotDVASpectrum_Aggregate(D, V, A, T, eq_list, zeta_list=zeta, zeta=0.05, mode="History")
fig.savefig(save_dir + "Collective Spectral Response" + file_typ)
plt.close(fig)

fig = plotDVASpectrum_Aggregate(D, PV, PA, T, eq_list, zeta_list=zeta, zeta=0.05, mode="Pseudo")
fig.savefig(save_dir + "Collective Pseudo Spectral Response" + file_typ)
plt.close(fig)

fig = plotDVASpectrum_Aggregate(D, V, A, T, eq_list, zeta_list=zeta, zeta=0.05, mode="History", isloglog=True,
                                grid_on=True)
fig.savefig(save_dir + "Collective Actual Response LogLog" + file_typ)
plt.close(fig)

fig = plotDVASpectrum_Aggregate(D, PV, PA, T, eq_list, zeta_list=zeta, zeta=0.05, mode="Pseudo", isloglog=True,
                                grid_on=True)
fig.savefig(save_dir + "Collective Pseudo Spectral Response LogLog" + file_typ)
plt.close(fig)

# plot mean spectral response (Clarify if pseudo or spectral acc, since disp is common to both)
# accel_design_spectrum, T=designSpectrum(A, T)
# plotDesignSpectrum(accel_design_spectrum,T)

# Plot probability heatmap, not required but looks nice, CHeck what spectrum is being plotted
# heatmap savefig is problematic
distribution, X, Y = meanSpectrumStatistics(PV, T, mode='mean')
fig = plotDesignSpectrumStatistics(distribution, X, Y, mode="mean", log_scale=True)
fig.savefig(save_dir + "Collective Spectral Probability Map" + file_typ)
plt.close(fig)

# Figure what needs to be in g units
A = A * g_list[working_units]
PA = PA * g_list[working_units]
for i, eq in enumerate(eq_list):
    # Plot tripartite plot for each
    fig = tripartitePlot(D[:, 0, i], PV[:, 0, i], PA[:, 0, i], T, name=eq.meta_name)
    # print("TBD")
    fig.savefig(save_dir + eq.meta_name + "Tripartite_Plot" + file_typ, dpi=600)
    plt.close(fig)
    # tripartitePlot(D[:, 0, 1], V[:, 0, 1], A[:, 0, 1], T)
    pass

fig = tripartitePlotSeries(D, PV, PA, T, name="Tripartite Plots", legend_list=[eq.name for eq in eq_list])
fig.savefig(save_dir + "CollectiveTripartite_Plot" + file_typ, dpi=600)
plt.close(fig)

A = A / g_list[working_units]
PA = PA / g_list[working_units]

# plot design spectrum at mean
# designSpec, T =  designSpectrum(PA, T )
# fig=plotDesignSpectrum(designSpec, T, property="Pseudo-Acceleration")
# fig.savefig(save_dir+"Mean DesignSpectrum"+file_typ)
# plt.close(fig)
# # plot design spectrum at mean+1sigma (Clarify)
#
# designSpec, T =  designSpectrum(PA, T , sigma=1)
# fig=plotDesignSpectrum(designSpec, T, property="Pseudo-Acceleration")
# fig.savefig(save_dir+"Mean+1sig DesignSpectrum"+file_typ)
# plt.close(fig)


# plot design spectrum at mean
mdesignSpec, T = meanSpectrum(PV, T)
fig = tripartitePlot(D, mdesignSpec, PA, T, name='Mean Spectrum')
fig.savefig(save_dir + "Mean Spectrum" + file_typ, dpi=600)
plt.close(fig)
# plot design spectrum at mean+1sigma (Clarify)

mpsdesignSpec, T = meanSpectrum(PV, T, sigma=1)
fig = tripartitePlot(D, mpsdesignSpec, PA, T, name='Mean + 1 sigma Spectrum')
fig.savefig(save_dir + "Mean+1sig Spectrum" + file_typ, dpi=600)
plt.close(fig)

# Create a design spectrum (sorry for the confusion this is a created spectrum, will need to check)

# Save data to excel sheet
col_name = ['Time Period(s)'] + [eq.name for eq in eq_list]  # Add "Time Period(s)" as the first column

# Assuming PA, PV, D, V, A are your quantities (e.g., 3D arrays)
quantities = {'Displacement (m)': D,
              'Velocity (mps)': V,
              'Acceleration (g)': A,
              'Pseudo_Velocity (mps)': PV,
              'Pseudo_Acceleration (g)': PA}

# Create an Excel writer object using 'openpyxl'
with pd.ExcelWriter(save_dir + "Spectral_Quantities.xlsx", engine='openpyxl') as writer:
    for quantity_name, data in quantities.items():
        # Create the DataFrame with T as the first column and the quantity data as the rest
        df = pd.DataFrame(data[:, 0, :], columns=col_name[1:])  # Exclude 'Time Period(s)' from column names
        df.insert(0, 'Time Period(s)', T)  # Insert the Time Periods as the first column

        # Write the DataFrame to the corresponding sheet
        df.to_excel(writer, sheet_name=quantity_name, index=False)
#
# Deliverables:
# •	Response Spectrum for x10 earthquakes: 5% damping. Spectral(actual response) + Pseudo. Plot this or not?
# •	Tri-log plot of response spectrum (pseudo seems to be the only valid one for this)
# •	Statistical Distribution: Can be done on excel if you want to explicitly show it.
# •	Final  Plots:
# o	Tri-log of individual response (pseudo) spectra
# o	Tri-log of mean (pseudo) spectra
# o	Tri-log of Mean+1 sigma (pseudo) spectra
# •	Deliverables:
# o	Excel table with  eq name and ground motion (format indicates  accel spectra but is this pseudo or actual)
# o	Tri-log of individual response (pseudo) spectra
# o	Tri-log of mean (pseudo) spectra
# o	Tri-log of Mean+1 sigma (pseudo) spectra
# o	Tri-log of approximate design spectrum based on mean +1 sigma
#
# Something in the recent emails makes me think the statistical analysis needs to be done on all 120 motions instead of 10 from each group. This is not stated in the homework document.
#
# Can this be clarified.
