import numpy as np
import scipy.integrate as integrate

class AppliedForce():
    def __init__(self, force=np.array([0,0]), start=None, end=None, 
                 interval=None, f_as_func_of_t=None):
        if not start:
            raise Exception("impulse must have a start time")
        if not end and not interval:
            raise Exception("impulse must have an end time or interval")
        
        self.__force = force # total force applied over time interval
        self.__start = start # start time of impulse
        self.__end = end or start + interval # end time of impulse
        if f_as_func_of_t is None:
            f_as_func_of_t = lambda t: self.__force * t # constant force
        
    def getAppliedForce(self, start=None, end=None, 
                        interval=None) -> (np.ndarray[float], bool):
        """
        Get the force applied to an arbitrary object over a given interval of 
        time.
        
        Parameters
        ----------
        start: float
            The start time of the interval, measured in seconds. Typically, this
            is the time in the simulation that the impulse begins to act on
            an object.
            
            Note: if start is not specified, then an exception is raised.
        end: float
            The end time of the interval, measured in seconds. Typically, this
            is the time in the simulation that the impulse stops acting on
            an object.
            
            Note: if end is not specified, then the interval is assumed to be
            from start to start + interval. If both end and interval are not
            specified, then an exception is raised.
        interval: float
            The length of the interval, measured in seconds. Typically, this
            is the time in the simulation that the impulse acts on an object.
            
            Note: if interval is not specified, then the interval is assumed to
            be from start to end. If both end and interval are not specified,
            then an exception is raised.
        
        Returns
        -------
        f: np.ndarray[float]
            The force applied by the impulse over the given interval of time,
            measured in Newtons. It is represented as a 2D vector, where the
            x-component is the force applied in the x-direction, and the
            y-component is the force applied in the y-direction.
        done: bool
            Returns true if the impulse interval has been exhausted, ie. every 
            following call to getAppliedForce will return a zero vector. Use
            this to determine when to remove the force from the simulation.
        """
        if not start:
            raise Exception("applied force must have a start time")
        if not end and not interval:
            raise Exception("applied force have an end time or interval")
        end = end or start + interval
        
        # find overlapping time interval, if one exists
        applied_start = max(self.__start, start)
        applied_end = min(self.__end, end)
        if applied_start >= applied_end:
            return np.array([0,0]) # no overlap
        
        # integrate the force function over the time interval
        return integrate.quad(self.__f_as_func_of_t, applied_start, 
                                       applied_end)