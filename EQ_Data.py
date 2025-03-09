import numpy as np
from matplotlib.scale import scale_factory

from Constants import *


class EQ_Data():

    def __init__(self, time, ground_accel, units='g', name="Unknown", orientation="unknown", location="Unknown", normalize=False):

        self.name = name
        self.orientation=orientation
        self.location=location

        self.meta_name = name+ " - " + orientation + " - " + location

        g_scale=1
        norm_scale=1

        if units=="SI":
            norm_scale=g_list[units]*g_scale
        elif units=="Imp":
            norm_scale = g_list[units]*g_scale
        elif units=='g':
            norm_scale=1*g_scale


        if normalize:
            scale_factor=norm_scale/max(abs(ground_accel))
            ground_accel=ground_accel*scale_factor

        # assume constant timestep for now
        self.dt = time[1] - time[0]
        time, ground_accel=self.checktimestep(self.dt, time,ground_accel)
        self.g = g
        self.orig_units = units

        self.time = time
        self.getGroundAccelInUnits(ground_accel)

    def getGroundAccelInUnits(self, ground_accel):
        if self.orig_units == "SI":
            self.ground_accel_SI = ground_accel
            self.ground_accel_g = ground_accel/g_SI
            self.ground_accel_Imp=ground_accel*g_Imp
        elif self.orig_units=="Imp":
            self.ground_accel_Imp = ground_accel
            self.ground_accel_g = ground_accel/g_Imp
            self.ground_accel_SI=ground_accel*g_SI
        elif self.orig_units == "g":
            # TODO add working units condition here
            self.ground_accel_SI = ground_accel*g_SI
            self.ground_accel_Imp = ground_accel * g_Imp
            self.ground_accel_g = ground_accel

    def checktimestep(self, dt, time, ground_accel):
        min_dt = 0.005  # Hard limit for the minimum timestep

        if dt <= min_dt:
            return time, ground_accel  # No interpolation needed

        num_intervals = int(np.ceil(dt / min_dt))
        # print(dt)
        # print(num_intervals)  # Ensure a whole number of divisions
        new_dt = dt / num_intervals  # Adjusted timestep

        new_time = []
        new_accel = []

        for i in range(len(time) - 1):
            t_start, t_end = time[i], time[i + 1]
            a_start, a_end = ground_accel[i], ground_accel[i + 1]

            interpolated_times = np.linspace(t_start, t_end, num_intervals + 1)
            interpolated_accel = np.linspace(a_start, a_end, num_intervals + 1)

            new_time.extend(interpolated_times[:-1])  # Exclude last to prevent duplication
            new_accel.extend(interpolated_accel[:-1])  # Exclude last to prevent duplication

        new_time.append(time[-1])  # Add final time step
        new_accel.append(ground_accel[-1])  # Add final acceleration value

        return np.array(new_time), np.array(new_accel)

    @property
    def ground_accel(self, units: str= working_units):
        if units== "SI":
            return self.ground_accel_SI
        elif units== "Imp":
            return self.ground_accel_Imp
        else:
            print("Invalid Units")
            return 0

class Sin_EQ(EQ_Data):

    def __init__(self, amplitude=1, frequency=3, t_end=10, t_step=0.1):
        t = np.arange(0, t_end, t_step)
        ground_accel = amplitude * np.sin(frequency * t)
        super().__init__(t, ground_accel, units="Imp", name="Sin Wave")
        # self.ground_accel
