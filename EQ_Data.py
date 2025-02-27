import numpy as np
from Constants import g
class EQ_Data():

    def __init__(self, time, ground_accel, g_units=True):

        self.name="Unknown"
        self.g = g
        self.is_orig_unit_g = g_units

        self.getGroundAccelInUnits(ground_accel)
        self.time=time
        # assume constant timestep for now
        self.dt=time[1]-time[0]


    def getGroundAccelInUnits(self, ground_accel):
        if self.is_orig_unit_g:
            self.ground_accel=ground_accel * self. g
            self.ground_accel_g=ground_accel
        else:
            self.ground_accel=ground_accel
            self.ground_accel_g=ground_accel/self.g


class Sin_EQ(EQ_Data):

    def __init__(self, amplitude=1, frequency=3, t_end=10, t_step=0.1):
        t=np.arange(0, t_end,t_step )
        ground_accel=amplitude*np.sin(frequency*t)
        super().__init__(t, ground_accel, g_units=False)
        # self.ground_accel