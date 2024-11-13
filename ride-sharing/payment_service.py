from ride_detail import RideDetail

class PaymentService:
    def __init__(self):
        pass
    
    def pay(self, ride: RideDetail):
        amount = ride.get_amount()
        print(f"amount: {amount}")
        return True
    