from log_levels import Level, INFO
from output_destinations import Output, DataBase

class LogConfig:
    def __init__(self, level: Level = INFO, destination: Output = DataBase):
        self.level = level
        self.destination = destination
      
    @property  
    def log_level(self):
        return self.level
    
    @log_level.setter
    def log_level(self, level: Level):
        self.level = level
    
    @property
    def output_destination(self):
        return self.destination
    
    @output_destination.setter
    def output_destination(self, destination):
        self.destination = destination
    