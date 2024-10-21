from abc import ABC, abstractmethod

class Votable(ABC):
    @abstractmethod
    def add_vote(self, user, vote_type):
        pass
    
    @abstractmethod
    def get_votes(Self):
        pass