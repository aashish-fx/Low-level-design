import typing as tp

from bookmyshow.show import Show
from movie import Movie

class Cinema:
    def __init__(self, cinemaId: str, name: str):
        self.cinemaId = cinemaId
        self.name = name
        self.running_movies = {}
        self.running_shows = {}
        
    def get_name(self):
        return self.name
    
    def get_running_movies(self):
        return list(self.running_movies.values())
    
    def add_running_movies(self, movie: Movie):
        self.running_movies[movie.movieId] = movie
        
    def add_running_show(self, show: Show):
        self.running_shows[show.showId] = show
    
    def get_all_running_shows(self) -> tp.Dict[str, Show]:
        return self.running_shows
    
    def get_running_show(self, show_id: str) -> Show:
        show = self.running_shows.get(show_id)
        if not show:
            raise ValueError("show does not exist")
        return show