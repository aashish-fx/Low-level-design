from datetime import datetime
from log_levels import Level

class LoggingMessage:
    def __init__(self, level: Level, message: str):
        self.level = level 
        self.message = message
        self.timestamp = datetime.timestamp

    def get_level(self):
        return self.level

    def get_message(self):
        return self.message
    
    def created_at(self):
        return self.timestamp
    