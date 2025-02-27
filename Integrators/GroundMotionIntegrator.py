from Constants import g
import numpy as np



def groundMotionIntegrator(eq_data, g_units=False):

    time=eq_data[0]
    if g_units:
        ground_accel_arr=eq_data[1]*g
    else:
        ground_accel_arr=eq_data[1]

    u0 = 0
    v0 = 0

    dt = np.diff(time)

    del_vel = (ground_accel_arr[1:] + ground_accel_arr[:-1]) * dt / 2
    vel = np.concatenate(([v0], np.cumsum(del_vel)))  # Integrate to get velocity

    # Calculate displacement using the trapezoidal rule
    del_disp = (vel[1:] + vel[:-1]) * dt / 2
    disp = np.concatenate(([u0], np.cumsum(del_disp)))  # Integrate to get displacement

    return disp, vel, ground_accel_arr, time