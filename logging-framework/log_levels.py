from abc import ABC, abstractmethod
from enum import Enum
from output_destinations import Output

class LEVELENUM(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Level(ABC):
    def __init__(self):
        ...
    
    @abstractmethod
    def log_level(self):
        pass
    
    @abstractmethod
    def weight(self):
        pass
        
    
class DEBUG(Level):
    def __init__(self, message):
        super().__init__(message)
    
    def log_level(self):
        return LEVELENUM.DEBUG
    
    def weight(self):
        return 3
    
    
class INFO(Level):
    def __init__(self, message):
        super().__init__(message)
        
    def log_level(self):
        return LEVELENUM.INFO
    
    def weight(self):
        return 2
    
class WARNING(Level):
    def __init__(self, message):
        super().__init__(message)
    
    def log_level(self):
        return LEVELENUM.WARNING
    
    def weight(self):
        return 4
    
class ERROR(Level):
    def __init__(self, message):
        super().__init__(message)
        
    def log_level(self):
        return LEVELENUM.ERROR
    
    def weight(self):
        return 6
    
class FATAL(Level):
    def __init__(self, message):
        super().__init__(message)
        
    def log_level(self):
        return LEVELENUM.FATAL
    
    def weight(self):
        return 10
    