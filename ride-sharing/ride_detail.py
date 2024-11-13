from enum import Enum
from user import User
from driver_detail import DriverDetail
from direction import Direction
from util import calc_distance

class RideType(Enum):
    REGULAR="Regular"
    PREMIUM="Premium"

class RideStatus(Enum):
    REQUESTED = "Requested"
    ACCEPTED = "Accepted"
    STARTED = "Started"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    NOTSTARTED = "Not_Started"

class RideDetail:
    def __init__(self, id: str, user: User, pickup_location: Direction, destination: Direction, ride_type: RideType, status: RideStatus = RideStatus.REQUESTED):
        self.id = id
        self.user = user
        self.pickup_location = pickup_location
        self.destination = destination
        self.ride_type = ride_type
        self.driver = None
        self.cost = self.calc_fare()
        self.status = status
        
    def get_id(self):
        return self.id
    
    def get_passenger(self) -> User:
        return self.user
        
    def get_ride_type(self):
        return self.ride_type
    
    def get_destination(self):
        return self.destination
    
    def get_pickup_location(self):
        return self.pickup_location
    
    def set_driver(self, driver: DriverDetail):
        self.driver = driver
        
    def get_driver(self):
        return self.driver.get_driver() if self.driver else None
    
    def calc_fare(self):
        speed = 30
        ride_pickup_direction = self.get_pickup_location()
        ride_destination_direction = self.get_destination()
        ride_type = self.get_ride_type()
        distance = calc_distance(ride_pickup_direction, ride_destination_direction)
        time = distance / speed
        cost_premium = 1.2 if ride_type == RideType.PREMIUM else 1
        cost = cost_premium * 10 * time
        return cost
    
    def get_cost(self):
        return self.cost
    
    def get_status(self):
        return self.status
    
    def update_status(self, status: RideStatus):
        self.status = status
    
        