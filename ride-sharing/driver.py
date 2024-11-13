
class Driver:
    def __init__(self, id: str, name: str, phone: int, ratings: str, license_plate: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.license_plate = license_plate
        self.ratings = ratings
        
    def get_ratings(self):
        return self.ratings
    
    def get_name(self):
        return self.name
    
    def get_license_plate(self):
        return self.license_plate
    