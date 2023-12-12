import base_classes as bc
import numpy as np
import scipy as sp

class M4A1(bc.Firearm):
    def __init__(self):
        super().__init__()
        
        # physical properties
        self.weight = 3.52 # kg
        self.center_of_mass = np.array([0, 0, 0]) # position vector in meters
        self.barrel_axis = np.array([0, 0, 0.02])
        self.pivot_point = np.array([0, 0.33, -0.025]) # position vector in meters
        
        # ballistic properties
        self.muzzle_velocity = np.array([0, -880, 0]) # muzzle velocity at the end of the barrel in m/s
        self.gas_constant = 1.7 # the jet moves quicker than the projectile in all cases: anywhere from 1.25-1.75 times. Can be calced but it's too much atm.
        
        #projectile properties
        self.projectile_mass = 0.004
        self.charge_mass = 0.001710691
        
        # barrel
        self.barrel_length = 0.415
        
class Man(bc.Operator):
    def __init__(self):
        super().__init__()
        
        self.weight = 80 # kg
        self.centre_of_mass = np.array([0, 0, 0]) # position vector in meters
        self.contact_point = np.array([0.3, 0.6, 0]) # approx location of contact point with rifle stock. Should be offset from centre of mass.