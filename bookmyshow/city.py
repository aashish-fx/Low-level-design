import typing as tp

from cinema import Cinema


class City:
    def __init__(self, id: str, name: str, postal_code: int):
        self.id = id
        self.name = name
        self.postal_code = postal_code
        self.cinemas = {}
        
    def add_cinema(self, cinema: Cinema):
        self.cinemas[cinema.cinemaId] = cinema
    
    def get_id(self) -> str:
        return self.id
        
    def get_cinemas(self) -> tp.Dict[str, Cinema]:
        return self.cinemas
    
    def get_cinema(self, cinema_id: str):
        cinema = self.cinemas.get(cinema_id)
        if not cinema:
            return ValueError("Cinema does not exist")
        return cinema
    
    def get_postal_code(self) -> int:
        return self.postal_code
    
    
            

