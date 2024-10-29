from .person import Person

class GameInfo:
    def __init__(self, is_over: bool = False, is_won: bool = False, is_draw: bool = False, person: Person = ""):
        self.is_over = is_over
        self.is_won = is_won
        self.is_draw = is_draw
        self.person = person
        
    def winner(self):
        return self.person
    
    def set_is_over(self):
        self.is_over = True
        
    def set_is_won(self):
        self.is_won = True
    
    def set_is_draw(self):
        self.is_draw = True
        
    def set_winner(self, person: Person):
        self.person = person
        
    def to_string(self):
        return f"Over: {self.is_over} \n Won: {self.is_won}, \n Draw: {self.is_draw} \n winner: {self.person}"