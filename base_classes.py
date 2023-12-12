import numpy as np

class Firearm:
    def __init__(self):
        pass
        # hnng colonel, i have an empty constructor
        
    # calcFirearmMomentum returns the momentum of the firearm at the moment of firing        
    def calcFirearmMomentum(self):
        return (-self.calcProjectileMomentum()) - self.calcGasMomentum()
    
    def calcProjectileMomentum(self):
        return self.projectile_mass * self.muzzle_velocity
    
    def calcGasMomentum(self):
        return self.charge_mass * self.muzzle_velocity * self.gas_constant
    
    def calcTimeInBarrel(self):
        return 2 * self.barrel_length / (np.linalg.norm(self.muzzle_velocity))
    
    def calcTorque(self):
        return self.calcRecoilForce() * abs(self.barrel_axis[2] - self.pivot_point[2])
    
    def calcRecoilForce(self):
        return self.calcProjectileRecoilForce() + self.calcGasRecoilForce()

    # f = change in momentum / change in time
    # this is while the projectile is in the barrel
    def calcProjectileRecoilForce(self):
        return self.calcProjectileMomentum() / self.calcTimeInBarrel()
    
    # calculating the gas recoil force is more complicated and requires knowing the time it takes for the gas to exit the barrel
    def calcGasRecoilForce(self):
        return 0
        
class Operator:
    def __init__(self):
        pass
        # hnng colonel, i have an empty constructor