import threading
import typing as tp

from seat import Seat
from show import Show
from queue import Queue
from user import User
from booking import Booking
from payment_service import PaymentService

class SeatReservationManager:
    def __init__(self):
        self.queue = {}
        self.locks = {}
        self.payment_service = PaymentService()
        
    def add_seat(self, seat: Seat):
        seat_id = seat.get_id()
        if seat_id not in self.queue:
            self.queue[seat_id] = Queue()
            self.locks[seat_id] = threading.Lock()
            
    def try_holding_lock(self, booking: Booking) -> tp.Union[Booking, None]:
        lock_already_acquired = False
        user = booking.user
        for seat in booking.seats:
            seat_id = seat.get_id()
            if not self.locks[seat_id].locked() and not seat.get_booked_by():
                self.locks[seat_id].acquire()
                seat.set_booked_by(user)
                
                # threading.Timer(30, self.check_payment_completion_and_release_lock, [show, seat, user])
                # print(f"Seat {seat_id} is held by {user.name}.")
                # return True
            else:
                lock_already_acquired = True
                break
        if lock_already_acquired:
            for seat in booking.seats:
                self.queue[seat.get_id()].put(booking)
                self.release_lock(seat, user)
            raise ValueError("some seats are already acquired..") 
        self.payment_service.process(booking)
        threading.Timer(30, self.check_payment_completion_and_release_lock, [booking])
        return booking


    def check_payment_completion_and_release_lock(self, booking: Booking):
        
        payment_processed = self.payment_service.check_if_payment_processed(booking)
        if payment_processed:
            for seat in booking.seats:
                self.queue[seat.get_id()] = Queue()
            # fire an event
        else:
            self.release_lock_for_a_booking(booking)
    
    def release_lock_for_a_booking(self, booking: Booking):
        user = booking.user
        for seat in booking.seats:
            self.release_lock(seat, user)
        
    def release_lock(self, seat: Seat, user: User):
        seat_id = seat.get_id()
        if seat.get_booked_by() == user:
            seat.set_booked_by(None)
            self.locks[seat_id].release()
            return True
        return False
                
            
        