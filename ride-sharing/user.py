class User:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.type = "Passenger"
        
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_type(self):
        return self.type
    