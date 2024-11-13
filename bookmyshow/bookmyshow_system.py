import typing as tp

from city import City
from cinema import Cinema
from hall import Hall
from show import Show
from seat import Seat

class BookMyShowSystem:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(BookMyShowSystem).__new__(cls)
            cls._cities = {}
            cls._halls = {}
        return cls._instance
    
    def add_city(self, city: City):
        self._cities[city.id] = city
    
    def add_cinema(self, city: City, cinema: Cinema):
        if city.get_id() in self._cities:
            city.add_cinema(cinema)
        else:
            raise ValueError("city does not exist")
    
    def get_cities(self) -> tp.List[City]: 
        return list(self._cities.values())
    
    def add_hall(self, hall: Hall):
        self._halls[hall.get_id()] = hall
    
    def add_show(self, cinema: Cinema, show: Show):
        cinema.add_running_show(show)
    
    def get_seats(self, hall: Hall) -> tp.List[Seat]:
        seats = hall.get_seats()
        return seats

    def book_seats(self, seats: tp.List[Seat]):
        ...
    
    