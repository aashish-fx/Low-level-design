from .reservation import Reservation
from uuid import uuid4

class Customer:
    def __init__(self, name: str, contact_details: int, driving_license: str):
        self.id = str(uuid4())
        self.name = name
        self.reservations = {}
        self.contact_details = contact_details
        self.driving_license = driving_license
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def add_reservation(self, reservation: Reservation):
        self.reservations[reservation.id] = reservation
        
    def cancel_reservation(self, reservation_id: str):
        if reservation_id in self.reservations:
            reservation = self.reservations[reservation_id] 
            reservation.mark_as_invalid()
            del self.reservations[reservation_id]
        else:
            raise ValueError("reservation does not exist")
        
    def modify_reservation(self, reservation_id: str, start: str, end: str):
        reservation = self.reservations.get(reservation_id)
        if not reservation:
            raise ValueError("reservation does not exist")
        reservation.modify_dates(start, end)
    
    def get_driving_license(self) -> str:
        return self.driving_license
    
    def get_contact_details(self) -> int:
        return self.contact_details
    
    def get_reservations(self):
        return self.reservations
    
    
    
    
    