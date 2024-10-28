from .message import Message
from .subscriber import Subscriber
class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
    
    def get_name(self):
        return self.name
    
    def publish(self, message: Message):
        for subscriber in self.subscribers:
            subscriber.receive(message, self)
                
    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)
                    
    