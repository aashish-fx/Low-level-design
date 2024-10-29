
from .car import CarInterface, CarConcrete
from .customer import Customer
from .reservation import Reservation

import typing as tp

class CarRentalSystem:
    _instance = None
    
    def __call__(cls):
        if not cls._instance:
            cls._instance = super().__call__(cls, CarRentalSystem)
            cls._cars = []
            
        return cls._instance
    
    def add_car(self, car: CarInterface):
        self._cars.append(car)
    
    def browse_cars(self):
        car_info = []
        for car in self._cars:
            car_info.append(car.get_details())

    def search(self, car_type, price_range: tp.Tuple[int, int]) -> tp.List[CarInterface]:
        filtered_cars = [car for car in self._carsif if ((car_type and car.model().lower() == car_type.lower()) or (price_range and price_range[0] <= car.rental_price_per_day() <= [price_range[1]])) and car.is_available()]
        return filtered_cars
            
    def add_reservation(self, car: CarConcrete, customer: Customer, start_date: str, end_date: str):
        try:
            if not car.is_available():
                raise ValueError("Car is not available")
            
            reservation = Reservation(customer, car, from_ts=start_date, to_ts=end_date)
            customer.add_reservation(reservation)
        except Exception as e:
            print(str(e))
            
    def cancel_reservation(self, customer: Customer, reservation_id: str):
        customer.cancel_reservation(reservation_id)
        
    def modify_reservation(self, customer: Customer, reservation_id: str, start: str, end: str):
        customer.modify_reservation(reservation_id, start, end)
        
    def get_available_cars(self) -> tp.List[CarInterface]:
        available_cars = [car for car in self._cars if car.is_available()]
        return available_cars
    
    def get_reservations(self, customer: Customer):
        reservations_obj = customer.get_reservations()
        reservations = []
        for reservation_id in reservations_obj:
            reservations.append(reservations_obj[reservation_id])
        return reservations_obj
            
            
            
        
        
    