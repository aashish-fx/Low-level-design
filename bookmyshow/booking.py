import typing as tp

from user import User
from show import Show
from seat import Seat


class Booking:
    def __init__(self, bookingId: str, user: User, show: Show, seats: tp.List[Seat]):
        self.bookingId = bookingId
        self.user = user
        self.show = show
        self.seats = tp.List[seats]
        
    def get_booking_details(self):
        return {
            "booking_id": self.bookingId,
            "user": self.user,
            "show": self.show,
            "seats": self.seats
        }