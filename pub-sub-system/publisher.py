from .topic import Topic
from .message import Message
class Publisher:
    def __init__(self, id):
        self.id = id
        
    def publish(topic: Topic, message: Message):
        topic.publish(message)
        