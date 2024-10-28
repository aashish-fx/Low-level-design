import collections

from .message import Message
from .topic import Topic
class Subscriber:
    def __init__(self, id):
        self.id = id
        self.topic_to_message = collections.defaultdict(list)
    
        
    def receive(self, message: Message, topic: Topic):
        publisher = message.publisher()
        self.topic_to_message[topic].append(message)
    
    
    
    