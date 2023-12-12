# Calculating the movement of a firearm and shooter by recoil effects

## Momentum

In a closed system, the total momentum of said system sums to zero. In the case of a system made up of only the firearm, and projectile, the system can be expressed as follows:

$$m_fv_f+m_pv_p=0$$

where: 

- $m_f$ is the mass of the firearm
- $v_f$ is the velocity of the firearm after immediately firing
- $m_p$ is the mass of the projectile
- $v_p$ is the velocity of the projectile after immediately firing

A force integrated over a time period during which it acts will yield the momentum that is supplied by that force. In the case of the of the recoil force that is applied to the firearm, this means that:

$$\int_0^{t_r}F_r(t)dt=m_fv_f=-m_pv_p$$

where:
- $F_r(t)$ is the recoil force as a function of time
- $t_r$ is the time period during which the recoil force is applied

To reduce free recoil, a counter-recoil force must be applied to the firearm. This force must supply enough momentum to bring the firearm to a halt. Similar to the above formula, this can be expressed as:

$$\int_0^{t_{cr}}F_{cr}(t)dt=-m_fv_f=m_pv_p$$

where:
- $F_{cr}(t)$ is the counter-recoil force as a function of time
- $t_{cr}$ is the time period during which the counter-recoil force is applied

Assuming that the forces are somewhat evenly spread out over their respective durations, this means the condition for free recoil is $t_r < t_{cr}$, while $F_r(t)+F_{cr}(t)=0$ would result in zero recoil.

## Angular Momentum

For a firearm firing under free-recoil conditions, it is likely that the recoil force will not only force the firearm backwards, but also cause it to rotate about its center of mass, or an anchor point (such as a shooter's shoulder). This can be observed on firearms where the barrel is above the center of mass or pivot point. If there is an angle for the rifle to rotate about, then the force will apply a torque to the firearm, causing it to rotate, given by:

$$\tau=I\frac{d^2\theta}{dt^2}=hF(t)$$

where:
- $h$ is the perpendicular distance of the centre of mass of the firearm below the barrel axis
- $F(t)$ is the force on the firearm due to expanding gasses, equal and opposite to the force on the projectile
- $I$ is the moment of inertia of the firearm about it's centre of mass or the pivot point
- $\theta$ is the angle of rotation of the barrel axis up from it's orientation at ignition.

From this the angular momentum can be found by integrating the torque over time:

$$I\frac{d\theta}{dt}=h\int_0^tF(t)dt=hm_gV_g(T)=hm_bV_b(t)$$

where the equality of the momenta of the firearm and momenta has been used. The angular rotation of the firearm as the bullet exists the barrel is found by integrating again:

$$I\theta_f=h\int_0^{t_f}m_bV_bdt=2hm_bL$$

where:
- $\theta_f$ is the angle of rotation above the aim angle at which the projectile leaves the barrel
- $t_f$ is the time of travel of the projectile in the barrel
- $L$ is the distance the projectile travels from it's rest position to the tip of the barrel

Then, the angle at which the projectile leaves the barrel above the aim angle is given by:

$$\theta_f=\frac{2hm_bL}{I}$$

## Accounting for ejecta

The above calculations assume that the projectile is the only mass that leaves the barrel. However, in reality, the expanding gasses that propel the projectile also leave the barrel. While a projectile travels down the barrel, the expanding gasses have no effect on the firearm, as the projectile forms a plug, and so the gasses are part of a closed system. However once the projectile leaves the barrel, the gasses are free to expand, and so the firearm is no longer a closed system. The gasses will continue to expand until they reach atmospheric pressure, and in doing so, will contribute to the recoil of the firearm. A more accurate calculation of momentum of the system looks like this:

$$p_e=m_pV_0+m_g\alpha V_0$$

where:

- $p_e$ is the momentum of the projectile and ejecta after the projectile has left the barrel
- $m_g$ is the mass of the gasses that propel the projectile. By conservation og mass, the mass of the ejected gasses is equal to the mass of the propellant 
- $V_0$ is the muzzle velocity of the projectile
- $\alpha$ is the ratio of the muzzle velocity of the projectile to the muzzle velocity of the gasses. This is usually taken to be between 1.25 and 1.75. This is mostly dependant on the propellant used, but also and the ratio of the barrel's length to it's radius.

This can then be substituted into the equation for calculating the momentum of the projectile for a more accurate calculation:

$$m_fv_f+m_pV_0+m_g\alpha V_0=0$$