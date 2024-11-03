import datetime

from bookmyshow.movie import Movie


class Show:
    def __init__(self, showId: str, movie: Movie, start_datetime: datetime.datetime, end_datetime: datetime.datetime, hallId: str):
        self.showId = showId
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.current_movie = movie
        self.hallId = hallId
    
    def get_current_movie(self):
        return self.current_movie
    
    def get_hall_id(self):
        return self.hallId
    
    def get_start_time(self):
        return self.start_datetime
    
    def get_end_time(self):
        return self.end_datetime
    