from enum import Enum
from driver import Driver
from direction import Direction

class DriverStatus(Enum):
    AVAILABLE = 1
    BUSY = 2
    

class DriverDetail:
    def __init__(self, id: str, driver: Driver, direction: Direction, speed: float = 0):
        self.id = id
        self.driver = driver
        self.direction = direction
        self.current_speed = speed
        self.status = DriverStatus.AVAILABLE
        
    def get_id(self):
        return self.id
        
    def get_driver(self):
        return self.driver
    
    def get_direction(self) -> Direction:
        return self.driver
    
    def update_direction(self, direction: Direction):
        self.direction = direction
        
    def get_current_speed(self):
        return self.current_speed
    
    def update_status(self, status: DriverStatus):
        self.status = status
        
    def get_status(self):
        return self.status
    
    def update_current_speed(self, speed):
        self.current_speed = speed