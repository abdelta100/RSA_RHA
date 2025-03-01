import numpy as np
from Constants import *


class EQ_Data():

    def __init__(self, time, ground_accel, units='g', name="Unknown", orientation="unknown", location="Unknown"):

        self.name = name
        self.orientation=orientation
        self.location=location

        self.meta_name = name+ " - " + orientation + " - " + location
        self.g = g
        self.orig_units = units

        self.getGroundAccelInUnits(ground_accel)
        self.time = time
        # assume constant timestep for now
        self.dt = time[1] - time[0]

    def getGroundAccelInUnits(self, ground_accel):
        if self.orig_units == "SI":
            self.ground_accel = ground_accel
            self.ground_accel_g = ground_accel/g_SI
        elif self.orig_units=="Imp":
            self.ground_accel = ground_accel
            self.ground_accel_g = ground_accel/g_Imp
        elif self.orig_units == "g":
            # TODO add working units condition here
            self.ground_accel = ground_accel*g_SI
            self.ground_accel_g = ground_accel

    @property
    def ground_accel_working(self, working_units: str="SI"):
        if working_units=="SI":
            return self.ground_accel_g * g_SI
        elif working_units=="Imp":
            return self.ground_accel_g * g_Imp
        else:
            print("Invalid Units")
            return 0

class Sin_EQ(EQ_Data):

    def __init__(self, amplitude=1, frequency=3, t_end=10, t_step=0.1):
        t = np.arange(0, t_end, t_step)
        ground_accel = amplitude * np.sin(frequency * t)
        super().__init__(t, ground_accel, units="Imp", name="Sin Wave")
        # self.ground_accel
