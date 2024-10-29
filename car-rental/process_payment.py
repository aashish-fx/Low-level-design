from abc import ABC, abstractmethod

# strategy pattern

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, reservation_id: str, amount: float) -> bool:
        pass
    
class CreditCardProcessor(ABC):
    def pay(self, reservation_id: str, amount: float) -> bool:
        return True
    
class PayPalProcessor(ABC):
    def pay(self, reservation_id: str, amount: float) -> bool:
        return True
    
        
        
    