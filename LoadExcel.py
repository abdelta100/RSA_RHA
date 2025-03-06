import numpy as np
import pandas as pd


def loadExcelDVAPVPA(file_path):
    # excel_path = "earthquake_spectral_data.xlsx"
    xls = pd.ExcelFile(file_path)

    # Initialize dictionaries to store reshaped arrays
    earthquake_data = {}

    D_all = np.empty((0, 1))  # Empty array to store displacement data (t, n)
    V_all = np.empty((0, 1))  # Empty array to store velocity data (t, n)
    A_all = np.empty((0, 1))  # Empty array to store acceleration data (t, n)
    PV_all = np.empty((0, 1))  # Empty array to store pseudo displacement data (t, n)
    PA_all = np.empty((0, 1))


    # Iterate through each sheet (each earthquake data)
    for i, sheet_name in enumerate(xls.sheet_names):
        print(f"Loading data for earthquake: {sheet_name}")

        # Load the data for the current earthquake
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # Extract columns as arrays (assuming column names match exactly with what was saved)
        T = df['Period (T)'].values
        D = df['Displacement (D)'].values
        V = df['Velocity (V)'].values
        A = df['Acceleration (A)'].values
        PV = df['Pseudo Displacement (PV)'].values
        PA = df['Pseudo Acceleration (PA)'].values
 # Shape (t, 1)

        if i == 0:
            t = len(T)  # Number of time steps (rows)

            # Initialize arrays with shape (t, 0) where `0` will be filled with the data of each earthquake
            D_all = np.empty((t, 0))
            V_all = np.empty((t, 0))
            A_all = np.empty((t, 0))
            PV_all = np.empty((t, 0))
            PA_all = np.empty((t, 0))

            # Stack all earthquakes' data into 2D arrays (shape: t x n)
        # For this, we will stack along axis 1 (horizontally)
        D_all = np.concatenate((D_all, D[:, np.newaxis]), axis=1)  # Shape (t, n)
        V_all = np.concatenate((V_all, V[:, np.newaxis]), axis=1)  # Shape (t, n)
        A_all = np.concatenate((A_all, A[:, np.newaxis]), axis=1)  # Shape (t, n)
        PV_all = np.concatenate((PV_all, PV[:, np.newaxis]), axis=1)  # Shape (t, n)
        PA_all = np.concatenate((PA_all, PA[:, np.newaxis]), axis=1)  # Now shape (t, n) for PA

        # Now reshape them to (t, 1,  # Shape (t, 1, n)

    D_all_reshaped = D_all[:, np.newaxis, :]  # Shape (t, 1, n)
    V_all_reshaped = V_all[:, np.newaxis, :]  # Shape (t, 1, n)
    A_all_reshaped = A_all[:, np.newaxis, :]  # Shape (t, 1, n)
    PV_all_reshaped = PV_all[:, np.newaxis, :]  # Shape (t, 1, n)
    PA_all_reshaped = PA_all[:, np.newaxis, :]

    # for i, sheet_name in enumerate(xls.sheet_names):
    #     earthquake_data[sheet_name] = {
    #         'T': T,  # Period (T) array for each earthquake
    #         'D': D_all_reshaped[:, :, i],  # Displacement for this earthquake
    #         'V': V_all_reshaped[:, :, i],  # Velocity for this earthquake
    #         'A': A_all_reshaped[:, :, i],  # Acceleration for this earthquake
    #         'PV': PV_all_reshaped[:, :, i],  # Pseudo Displacement for this earthquake
    #         'PA': PA_all_reshaped[:, :, i],  # Pseudo Acceleration for this earthquake
    #     }

    return D_all_reshaped, V_all_reshaped, A_all_reshaped, PV_all_reshaped, PA_all_reshaped, T