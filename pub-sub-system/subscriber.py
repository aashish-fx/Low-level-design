import collections

from .message import Message
from .topic import Topic
class Subscriber:
    def __init__(self):
        self.topic_to_message = collections.defaultdict(list)
    
    def subscribe(self, topic):
        self.topics.append(topic)
        
    def receive(self, message: Message, topic: Topic):
        publisher = message.publisher()
        self.topic_to_message[topic].append(message)
    
    
    
    