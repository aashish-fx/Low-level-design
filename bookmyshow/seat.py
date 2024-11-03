import typing as tp
from abc import ABC, abstractmethod
from user import User

class Seat(ABC):
    def __init__(self, id):
        self.id = id
        self.availability_status = None
        self.price = None
        self.booked_by = None
        
        
    def get_id(self):
        return self.id
    
    def set_booked_by(self, user: tp.Union[User, None]):
        self.booked_by = user
        
    def get_booked_by(self):
        return self.booked_by
        
    @abstractmethod
    def get_availability_status(self):
        pass
    
    @abstractmethod
    def set_availability_status(self, status):
        pass
    
    @abstractmethod
    def get_price(self):
        pass
    
    @abstractmethod
    def set_price(self, price):
        pass
    
class PremiumSeat(Seat):
    def get_availability_status(self):
        return self.availability_status
    
    def set_availability_status(self, status):
        self.availability_status = status
        
    def get_price(self):
        return self.price
    
    
class RegularSeat(Seat): 
    def get_availability_status(self):
        return self.availability_status
    
    def set_availability_status(self, status):
        self.availability_status = status
        
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price
        
    