class Movie:
    def __init__(self, movieId: str, name: str, description: str, duration: str, genre: str, language: str, release_date: str = ""):
        self.movieId = movieId
        self.name = name
        self.genre = genre
        self.duration = duration
        self.language = language
        self.release_date = release_date
        self.description = description
        
    def get_genre(self):
        return self.genre
    
    def get_name(self):
        return self.name
    
    def get_language(self):
        return self.language
    
    def get_release_date(self):
        return self.release_date
        
    def get_description(self):
        return self.description
    
    def get_duration(self):
        return self.duration
        
        
    
        
    
        
