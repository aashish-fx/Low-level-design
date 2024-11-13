class Direction:
    def __init__(self, lat: int, long: int, detail: str = ""):
        self.lat = lat
        self.long = long
        self.detail = detail
        
    def get_lat(self):
        return self.lat
    
    def get_long(self):
        return self.long

