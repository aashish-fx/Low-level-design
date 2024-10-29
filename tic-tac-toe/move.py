from .cell import Cell
from .person import Person
class Move:
    def __init__(self, person: Person, cell: Cell):
        self.person = person
        self.cell = cell
        
    def get_person(self):
        return self.person
    
    def get_cell(self):
        return self.cell
    
    def to_string(self):
        return f"{self.person.get_name()} made move on ({self.cell.get_coordinates()})"