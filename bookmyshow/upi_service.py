from payment_service import PaymentService

class UPIService(PaymentService):
    
    def process(self, booking_id, amount):
        return super().process(booking_id, amount)