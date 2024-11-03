from booking import Booking

class User:
    def __init__(self, id: str, name: str, email: str, phone: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.bookings = {}
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def add_booking(self, booking: Booking):
        self.bookings[booking.bookingId] = booking
        
    def get_bookings(self):
        return list(self.bookings.values())
    
    def get_phone(self):
        return self.phone
    