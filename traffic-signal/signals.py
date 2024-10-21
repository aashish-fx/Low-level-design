from abc import ABC, abstractmethod

class Signals(ABC):
    def __int__(self):
        self.duration = 120
        
    @abstractmethod
    def get(self):
        pass
    
    @abstractmethod
    def action(self):
        pass
    
    @property
    def duration(self) -> int:
        return self.time
    
    @duration.setter
    def set_duration(self, duration):
        self.time = duration
        
    
class Red(Signals):
    def __init__(self):
        self.duration = super().duration
        
    def get(self):
        return "RED"
    
    def action(self):
        return "STOP"
    

class Green(Signals):
    def __init__(self):
        self.duration = super().duration
        
    def get(self):
        return "GREEN"
    
    def action(self):
        return "GO"
    
    
class Yellow(Signals):
    def __init__(self):
        self.duration = super().duration
        
    def get(self):
        return "BLUE"
    
    def action(self):
        return "READY TO GO"
    
    def duration(self):
        return 3

    