from .parking_level import ParkingLevel
from .vehicles import Vehicles

class ParkingLot:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls, ParkingLot)
            cls._parking_levels = {}
        return cls._instance
    
    def add_parking_level(self, parking_level: ParkingLevel):
        self._parking_levels[parking_level.level] = parking_level
    
    def assign_vehicle(self, vehicle: Vehicles):
        vehicle_assigned = False
        for level in self._parking_levels:
            parking_level = self._parking_levels[level]
            if parking_level.get_empty_spots(vehicle) > 0:
                parking_level.assign_vehicles(vehicle)
                vehicle_assigned = True
                break
        if not vehicle_assigned:
            raise ValueError("Parking lot is full")
    
    def get_empty_spot(self, level: int):
        parking_level = self._parking_levels.get(level, None)
        return parking_level.total_empty_spot() if parking_level else None
    
    def get_empty_spot_across_parking_levels(self):
        total_empty_spot = 0
        for level in self._parking_levels:
            empty_spot = self.get_empty_spot(level)
            if empty_spot:
                total_empty_spot += empty_spot
        return empty_spot

    def release_vehicle(self, level: int, vehicle: Vehicles):
        vehicle_level = self._parking_levels[level]
        vehicle_level.release_vehicles(vehicle)

        
            

        
        
    

                
        
    