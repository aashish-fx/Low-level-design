from movie import Movie
from seat import Seat, PremiumSeat, RegularSeat

class Hall:
    def __init__(self, hallId: str, no_of_premium_seats: str, no_of_regular_seats: str, current_running_movie: str = None):
        self.hallId = hallId
        self.no_of_premium_seats = no_of_premium_seats
        self.no_of_regular_seats = no_of_regular_seats
        self.premium_seats = {}
        self.regular_seats = {}
        self.current_running_movie = current_running_movie
    
    def get_id(self):
        return self.hallId
    
    def get_no_of_premium_seats(self):
        return self.get_no_of_premium_seats
    
    def get_no_of_regular_seats(self):
        return self.get_no_of_regular_seats
    
    def set_current_running_movie(self, movie: Movie):
        self.current_running_movie = movie
        
    def get_current_running_movie(self):
        return self.current_running_movie
    
    def book_seat(self, seat: Seat):
        if isinstance(seat, PremiumSeat):
            self.premium_seats[seat.id] = seat
        elif isinstance(seat, RegularSeat):
            self.regular_seats[seat.id] = seat
        else:
            raise ValueError("Seat type not available")
    
    def get_seats(self):
        premium = self.get_no_of_premium_seats()
        regular = self.get_no_of_regular_seats()
        premium.updade(regular)
        return premium
    