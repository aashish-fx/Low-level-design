import typing as tp

from credit_card import CreditCard
from direction import Direction
from driver_detail import DriverDetail, DriverStatus
from ride_detail import RideDetail, RideStatus, RideType
from booking import Booking
from util import calc_distance
from user import User
from payment_service import PaymentService


MAX_DISTANCE_TO_NOTIFY_DIRVERS = 3

class CarSharingSystem:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(CarSharingSystem).__new__(cls)
            cls._derivers = {}
            cls._rides = {}
            
        return cls._instance
    
    def add_driver(self, driver: DriverDetail):
        self._derivers[driver.get_id()] = driver
    
    def get_driver(self, id):
        return self._derivers.get(id, None)
    
    def add_ride(self, ride: RideDetail):
        self._rides[ride.get_id()] = ride
    
    def _calc_distance_between_driver_and_pickup_point(self, ride: RideDetail, driver: DriverDetail):
        driver_direction = driver.get_direction()
        ride_pickup_location = ride.get_pickup_location()
        distance = calc_distance(driver_direction, ride_pickup_location)
        return distance
    
    def allocate_ride(self, passanger: User, source: Direction, destination: Direction, ride_type: RideType):
        ride = RideDetail(user=passanger, pickup_location=source, destination=destination, ride_type=ride_type)
        self.add_ride(ride)
        valid_drivers = []
        for driver in self._derivers.keys():
            if driver.get_status() == DriverStatus.AVAILABLE:
                distance = self._calc_distance_between_driver_and_pickup_point(ride, driver)
                if distance <= MAX_DISTANCE_TO_NOTIFY_DIRVERS:
                    valid_drivers.append(driver)
        self._notify_drivers(valid_drivers, ride)

    def _notify_drivers(self, drivers: tp.List[DriverDetail], ride: RideDetail):
        for driver in drivers:
            print(f"Notifiying driver:{driver.driver.get_name()}, you have a new ride request: Name: {ride.get_passenger().get_name()}")
                
                
    def accept_ride(self, driver: DriverDetail, ride: RideDetail):
        driver.update_status(DriverStatus.BUSY)
        ride.set_driver(driver)
        ride.update_status(RideStatus.ACCEPTED)
        self.notify(ride, "Ride Accepted")
        
    def start_ride(self, ride: RideDetail):
        if ride.get_status() == RideStatus.ACCEPTED:
            ride.update_status(RideStatus.STARTED)
            self.notify(ride, "Ride has started")
    
    def complete_ride(self, ride: RideDetail):
        if ride.get_status() == RideStatus.STARTED:
            paid = self.pay(ride)
            if paid:
                ride.update_status(RideStatus.COMPLETED)
                ride.driver.update_status(DriverStatus.AVAILABLE)
                self.notify(ride, "RIDE COMPLETED")
            else:
                self.notify(ride, "Retry")
            
           
    def pay(self, ride: RideDetail, payment_service: PaymentService = CreditCard):
        payment_completed = payment_service.pay(ride) 
        if payment_completed:
            self.notify(ride, "Payment completed")
            ride.update_status(RideStatus.COMPLETED)
        else:
            self.notify(ride, "Payment Cancelled")
            
       
    def notify(self, ride: RideDetail, message: str):
        ...
    
            
    