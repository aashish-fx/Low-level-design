
class Person:
    def __init__(self, name, symbol):
        self.name = name
        self.won = False
        self.assigned_symbol = symbol
        
    def get_name(self):
        return self.name
    
    def has_won(self):
        return self.won
    
    def set_won(self):
        self.won = True
    
    def get_symbol(self):
        return self.assigned_symbol
    