from car_rental_system import CarRentalSystem
from car import CarConcrete
from customer import Customer
from process_payment  import CreditCardProcessor

class CarRentalDemo:
    
    @staticmethod
    def run():
        car_rental_syatem  = CarRentalSystem()
        car_rental_syatem.add_car(CarConcrete("Toyota", "Camry", 2022, "ABC123", 50))
        car_rental_syatem.add_car(CarConcrete("Honda", "Civic", 2021, "XYZ789", 45.0))
        
        customer1 = Customer("John Doe", "john@example.com", "DL1234")
        customer2 = Customer("Jane Smith", "jane@example.com", "DL5678")
        start = "2024-02-01"
        end = "2024-02-04"
        available_cars = car_rental_syatem.get_available_cars(start, end)
        if available_cars:
            selected_car = available_cars[0]
            reservation = car_rental_syatem.add_reservation(selected_car, customer1, start, end)
            if reservation:
                paid = car_rental_syatem.make_payment(CreditCardProcessor, reservation.id)
                if not paid:
                    car_rental_syatem.cancel_reservation(customer1, reservation.id)
                    print("Payment failed...")
                    return 
                print("Payment Successfull..")
                
            
        
        
        
if __name__ == "__main__":
    CarRentalDemo.run()