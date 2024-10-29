import typing as tp

from uuid import uuid4
from customer import Customer
from car import CarConcrete
from utils import no_of_days_between_two_dates

class Reservation:
    def __init__(self, customer: Customer, car: CarConcrete, to_ts: str, from_ts: str):
        self.id = str(uuid4())
        self.reservation_by = customer
        self.to_ts = to_ts
        self.from_ts = from_ts
        self.car = car
        self.is_valid = True
        
    def get_reservation_by(self) -> Customer:
        return self.reservation_by
    
    def get_car(self) -> CarConcrete:
        return self.car
    
    def get_dates(self) -> tp.Tuple[str, str]:
        return (self.from_ts, self.to_ts)
        
    def get_reservation_detail(self) -> str:
        return f"Car: {self.car} is booked by {self.reservation_by} from date: {self.from_ts} to {self.to_ts}"
    
    def modify_dates(self, start, end):
        self.from_ts = start
        self.to_ts = end
        
    def mark_as_invalid(self):
        self.car.mark_available()
        self.is_valid = False
         
    def get_cost(self):
        total_cost = self.car.rental_price_per_day() * (no_of_days_between_two_dates(self.from_ts, self.to_ts))
        return total_cost
    