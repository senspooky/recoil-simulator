import numpy as np
import queue

#object represents an object in the world to be rendered
class Object():
    def __init__(self):
        self.pos = np.array([0,0]) # position in x and y
        self.angle = 0 # angle in radians. Will rotate counter-clockwise for positive angles
        self.scale = np.array([1,1]) # scale in x and y
        self.transformationQueue = queue.SimpleQueue() # queue of transformations to be applied to the object