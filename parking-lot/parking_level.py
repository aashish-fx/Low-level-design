
from .vehicles import Bike, Car, Truck, Vehicles, VehicleEnum

class ParkingLevel:
    def __init__(self, level: str, bike_parking: int = 10, car_parking: int = 10, truck_parking: int = 10):
        self.id = self
        self.level = level
        self.bike_parking_spots = bike_parking
        self.car_parking_spots = car_parking
        self.truck_parking_spots = truck_parking
        self.bikes = {}
        self.cars = {}
        self.trucks = {}
        
    def _assign_bike(self, bike: Vehicles) -> bool:
        if len(set(self.bikes.keys())) < self.bike_parking_spots:
            self.bikes[bike.vehicle_number] = bike
            return True
        else:
            return False
    
    def _assign_car(self, car: Vehicles) -> bool:
        if len(set(self.cars.keys())) < self.car_parking_spots:
            self.cars[car.vehicle_number] = car
            return True
        else:
            return False
    
    def _assign_truck(self, truck: Vehicles) -> bool:
        if len(set(self.trucks.keys())) < self.truck_parking_spots:
            self.trucks[truck.vehicle_number] = truck
            return True
        else:
            return False
        
    def _release_bike(self, bike: Vehicles):
        if len(set(self.bikes.keys())):
            if self.bikes.get(bike.vehicle_number, None):
                del self.bikes[bike.vehicle_number]
            else:
                raise ValueError("Bike does not exist in this parking level.")
    
    def _release_car(self, car: Vehicles):
        if len(set(self.cars.keys())):
            if self.cars.get(car.vehicle_number, None):
                del self.cars[car.vehicle_number]
            else:
                raise ValueError("Bike does not exist in this parking level.")
    
    def _release_truck(self, truck: Vehicles):
        if len(set(self.trucks.keys())):
            if self.trucks.get(Truck.vehicle_number, None):
                del self.trucks[truck.vehicle_number]
            else:
                raise ValueError("Bike does not exist in this parking level.")
    
    def get_empty_spots(self, vehicle: VehicleEnum):
        if vehicle == VehicleEnum.BIKE:
            return self.bike_parking_spots - len(set(self.bikes.keys()))
        elif vehicle == VehicleEnum.CAR:
            return self.car_parking_spots - len(set(self.cars.keys()))
        elif vehicle == VehicleEnum.TRUCK:
            return self.truck_parking_spots - len(set(self.trucks.keys()))
        else:
            raise ValueError("Vehicle does not exist")
    
    def assign_vehicles(self, vehicle: Vehicles):
        if isinstance(vehicle, Car):
            self._assign_car(vehicle)
        elif isinstance(vehicle, Bike):
            self._assign_bike(Bike)
        elif isinstance(vehicle, Truck):
            self._assign_truck(vehicle)
        else:
            raise ValueError("Vehicle does not exist")
    
    def release_vehicles(self, vehicle: Vehicles):
        if isinstance(vehicle, Car):
            self._release_car(vehicle)
        elif isinstance(vehicle, Bike):
            self._release_bike(Bike)
        elif isinstance(vehicle, Truck):
            self._release_truck(vehicle)
        else:
            raise ValueError("Vehicle does not exist")

    def total_empty_spot(self):
        empty_spot = 0
        for vehicle in VehicleEnum:
            empty_spot += self.get_empty_spots(vehicle)
        return empty_spot
                
    def bikes_parked(self):
        return self.bike_parking_spots
    
    def car_parked(self):
        return self.car_parking_spots
    
    def trucks_parked(self):
        return self.trucks_parked
        
        
        
        
        