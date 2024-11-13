from payment_service import PaymentService

class CreditCard(PaymentService):
    def pay(self, booking_detail):
        return super().pay(booking_detail)