import numpy as np
import numpy.typing as npt
from typing import Callable
import scipy.integrate as integrate

class Force():
    def __init__(self, force:npt.NDArray[np.float64], 
                 start:np.float64,  end:np.float64 | None = None, 
                 interval:np.float64 | None = None, 
                 func:Callable[[np.float64], 
                               npt.NDArray[np.float64]] | None = None):
        
        if not end and not interval:
            raise Exception("impulse must have an end time or interval")
        
        self.__force = force # total force applied over time interval
        self.__start = start # start time of impulse
        self.__end:np.float64 = (end if end else np.add(interval, start) if interval else 
                      start) # end time of impulse
        self.__func = func or self.__defaultFunc # constant force
    
    def __defaultFunc(self, x:np.float64) -> npt.NDArray[np.float64]:
        return np.multiply(self.__force, x)
    
    def getAppliedForce(self, start_time:np.float64, end:np.float64 | None = None,
                        interval:np.float64 | None = None
                        ) -> npt.NDArray[np.float64] | None:
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
        if not end and not interval:
            raise Exception("applied force have an end time or interval")
        
        end_time = end if end else np.add(interval, start_time) if interval else start_time
        
        # find overlapping time interval, if one exists
        applied_start = max(self.__start, start_time)
        applied_end = min(self.__end, end_time)
        if np.greater_equal(applied_start, applied_end):
            return np.array([0,0]) # no overlap
        
        # integrate the force function over the time interval
        return integrate.quad(self.__func, applied_start, 
                                       applied_end)