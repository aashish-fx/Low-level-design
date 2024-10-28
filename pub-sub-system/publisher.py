from .topic import Topic
from .message import Message
class Publisher:
    def __init__(self):
        pass
    
    def publish(topic: Topic, message: Message):
        topic.publish(message)
        