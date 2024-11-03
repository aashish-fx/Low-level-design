from booking import Booking

class PaymentService:
    def __init__(self):
        self.payments = {}
    
    def process(self, booking: Booking, amount):
        print(f"apying: {amount} for booking id {booking.bookingId}")
        self.payments[booking.bookingId] = booking
        return True
        
    def check_if_payment_processed(self, booking: Booking):
        return self.payments.get(booking.bookingId)