from src.objects.renderable import Renderable
import numpy as np
import queue

# A newtonian object is a renderable that is affected by physics
#
# This is achieved by way of applying simple forces to the object over specified
# time intervalsduring a "step". The object's position and rotation are 
# updated accordingly based on the forces applied to it.
class Newtonian(Renderable):
    def __init__(self):
        super.__init__(self)
        
        self.pivot_point = np.array([0,0]) # the point about which the object rotates. If not anchored to a pivot, this is the centre of mass
        self.centre_of_mass = np.array([0,0]) # the point about which the object's mass is distributed
        # self.friction = 0 # might implement this later
        self.weight = 1 # the weight of the object (kg)
    
        # forces are registered here and are applied over a specified time interval
        # at each step, forces are applied to the object and the object's
        # position and rotation are updated accordingly
        
        self.__forces = queue.PriorityQueue()
        
    def addForce(self, force, interval=1):
        self.__forces.put((interval, force))
    