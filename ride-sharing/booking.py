from enum import Enum
from ride_detail import RideDetail
from driver import Driver



class Booking:
    def __init__(self, amount: float, ride_detail: RideDetail, driver: Driver):
        self.amount = amount
        self.ride_detail = ride_detail
        self.driver = driver
        
    def get_amount(self):
        return self.amount
    
    def get_driver(self):
        return self.amount
    
    def get_ride_detail(self):
        return self.ride_detail
    
    