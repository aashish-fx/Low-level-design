from abc import ABC, abstractmethod
from enum import Enum

class VehicleEnum(Enum):
    BIKE = "Bike"
    CAR = "Car"
    TRUCK = "Truck"

class Vehicles(ABC):
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number
        
    @abstractmethod
    def get_type():
        pass
    
    @abstractmethod
    def vehicle_number(self):
        return self.vehicle_number
    
    @abstractmethod
    def no_of_tyres():
        pass
    
class Car(Vehicles):
    def get_type():
        return VehicleEnum.CAR
    
    def no_of_tyres():
        return 4
    
class Bike(Vehicles):
    def get_type():
        return VehicleEnum.BIKE
    
    def no_of_tyres():
        return 2
    

class Truck(Vehicles):
    def get_type():
        return VehicleEnum.TRUCK
    
    def no_of_tyres():
        return 4
   
 
    
    