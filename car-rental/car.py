from abc import ABC, abstractmethod
from uuid import uuid4

class CarInterface(ABC):
    def __init__(self, maker, model, year, licence_plate_number, rental_price_per_day):
        self.id = str(uuid4())
        self._maker = maker
        self._model = model
        self._year = year
        self._licence_plate_number = licence_plate_number
        self._rental_price_per_day = rental_price_per_day
        self.available = True
        # self.booked_by = None
        
    @abstractmethod
    def maker(self):
        ...
        
    @abstractmethod
    def model(self):
        ...
        
    @abstractmethod
    def year(self):
        ...
        
    @abstractmethod
    def licence_plate_number(self):
        ...
        
    @abstractmethod
    def rental_price_per_day(self):
        ...
    
        
class CarConcrete(CarInterface):
    def __init__(self, maker, model, year, licence_plate_number, rental_price_per_day):
        super().__init__(maker, model, year, licence_plate_number, rental_price_per_day)
        
    def maker(self):
        return self._maker
    
    def model(self):
        return self._model
    
    def year(self):
        return self._year
    
    def licence_plate_number(self):
        return self._licence_plate_number
    
    def rental_price_per_day(self):
        return self._rental_price_per_day
    
    def is_available(self):
        return self.available
    
    def mark_unavailable(self):
        self.available = False
    
    def mark_available(self):
        self.available = True
    
    def set_booked_by(self, booked_by):
        self.available = False
        self.booked_by = booked_by
        
    # def get_booked_by(self):
    #     return self.booked_by
    
    def get_details(self):
        return {
                "model": self.model(), 
                "maker": self.maker(), 
                "license_plate_number": self.licence_plate_number(),
                "year": self.year(), 
                "rental_price_per_day": self.rental_price_per_day(),
                "is_available": self.is_available()
                }
    
    