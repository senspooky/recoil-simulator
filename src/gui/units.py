from enum import Enum
from typing import Callable

class Type(Enum):
    INVALID = 0
    TIME = 1
    LENGTH = 2
    MASS = 3
    ELECTRIC_CURRENT = 4
    TEMPERATURE = 5
    AMOUNT_OF_SUBSTANCE = 6
    LUMINOUS_INTENSITY = 7
    
class Unit():
    def __init__(self, type:Type, 
                 to_si:Callable[[float], float] | float | None = None, 
                 from_si:Callable[[float], float] | float | None = None):
        """
        Creates a new unit of measurement.
        
        Parameters
        ----------
        type: Type
            The type of unit of measurement. This is used to determine whether
            or not the unit of measurement can be converted to or from another 
            unit ofmeasurement.
        toSI: Callable[[float], float] | float | None
            Represents the conversion from the unit of measurement to SI units.
            If this is a function, then it is called with it's own value to get
            the equivalent in SI units. If this is a float, then it is 
            multiplied by the value of the unit of measurement to get the 
            equivalent in SI units. If this is None, then the it is treated as
            a float, which is determined from the inverse of fromSI if it is a 
            float value, otherwise this results in an error.
        fromSI: Callable[[float], float] | float | None
            Represents the conversion from SI units to the unit of measurement.
            If this is a function, then it is called with the value of it's 
            equivalent SI unit to get the equivalent in the unit of measurement. 
            If this is a float, then it is multiplied by the value of the SI
            unit to get the equivalent in the unit of measurement. If this is
            None, then the it is treated as a float, which is determined from
            the inverse of toSI if it is a float value, otherwise this results
            in an error.
        """ 
        temp_to_si = (to_si if isinstance(to_si, Callable) else 
                       self.__constant_conversion(to_si) if 
                       isinstance(to_si, float) else 
                       self.__constant_conversion(from_si) if 
                       isinstance(from_si, float) else None)
        if not temp_to_si:
            raise ValueError("from_si must be a float if to_si is omitted")
        self.__to_si = temp_to_si
        
        temp_from_si = (from_si if isinstance(from_si, Callable) else 
                self.__constant_conversion(from_si) if isinstance(from_si, float) 
                else self.__constant_conversion(to_si) if isinstance(to_si, float) 
                else None)
        if not temp_from_si:
            raise ValueError("to_si must be a float if from_si is omitted")
        self.__from_si = temp_from_si
        self.__type = type
        
    def __constant_conversion(self, value:float) -> Callable[[float], float]:
        return lambda x: x * value
    
    def convert_unit_value_to_si(self, value:float) -> float:
        return self.__to_si(value)
    
    def convert_si_to_unit_value(self, value:float) -> float:
        return self.__from_si(value)
    
    def get_type(self) -> Type:
        return self.__type