
from car import CarInterface, CarConcrete
from customer import Customer
from reservation import Reservation
from process_payment import PaymentProcessor

import typing as tp

class CarRentalSystem:
    _instance = None
    
    def __call__(cls):
        if not cls._instance:
            cls._instance = super().__call__(cls, CarRentalSystem)
            cls._cars = {}
            cls._reservations = {}
            
        return cls._instance
    
    def add_car(self, car: CarInterface):
        self._cars[car.licence_plate_number] = car
        
    def remove_car(self, license_place_no):
        if license_place_no not in self._cars:
            raise ValueError("car does not exist")
        self._cars.pop(license_place_no)
    
    def browse_cars(self):
        car_info = []
        for car_license_no in self._cars:
            car = self._cars[car_license_no]
            car_info.append(car.get_details())

    def search(self, car_type, price_range: tp.Tuple[int, int]) -> tp.List[CarInterface]:
        filtered_cars = [car for car in self._cars.values() if ((car_type and car.model().lower() == car_type.lower()) or (price_range and price_range[0] <= car.rental_price_per_day() <= [price_range[1]])) and car.is_available()]
        return filtered_cars
            
    def add_reservation(self, car: CarConcrete, customer: Customer, start_date: str, end_date: str):
        try:
            if not car.is_available():
                return None
            
            reservation = Reservation(customer, car, from_ts=start_date, to_ts=end_date)
            car.mark_unavailable()
            self._reservations[reservation.id] = reservation
            customer.add_reservation(reservation)
            return reservation
        except Exception as e:
            print(str(e))
            
    def cancel_reservation(self, customer: Customer, reservation_id: str):
        customer.cancel_reservation(reservation_id)
        reservation = self._reservations[reservation_id]
        reservation.get_car().mark_available()
        self._reservations.pop(reservation_id)
        
    def modify_reservation(self, customer: Customer, reservation_id: str, start: str, end: str):
        customer.modify_reservation(reservation_id, start, end)
    
    def get_non_available_cars_license(self, start, end):
        non_avail_cars_license = {}
        for reservation_id in self._reservations:
            reservation = self._reservations.get(reservation_id)
            r_start, r_end = reservation.get_dates()
            if  start <= r_start <= end or  start <= r_end <= end:
                non_avail_cars_license.add(reservation.get_car().licence_plate_number())
        return non_avail_cars_license
        
    def get_available_cars(self, start: str, end: str) -> tp.List[CarInterface]:
        non_avail_cars_license = self.get_non_available_cars(start=start, end=end)
        available_cars = []
        
        for license in self._cars:
            if license not in non_avail_cars_license:
                available_cars.append(self._cars[license])                
                
        return available_cars
    
    def get_reservations(self, customer: Customer):
        reservations_obj = customer.get_reservations()
        reservations = []
        for reservation_id in reservations_obj:
            reservations.append(reservations_obj[reservation_id])
        return reservations_obj
            
    def make_payment(self, payment_processor: PaymentProcessor, reservation_id: str):
        cost = self._reservations.get(reservation_id).get_cost()
        paid = payment_processor.pay(reservation_id, cost)
        return paid
                
    
        
        
    