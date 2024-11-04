from abc import ABC, abstractmethod

class Output(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def add(self, data):
        # do something with data
        ...
        

class DataBase(Output):
    pass
    
class File(Output):
    pass
    
class Console(Output):
    pass
