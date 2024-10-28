from concurrent.futures import ThreadPoolExecutor
from .topic import Topic
from .subscriber import Subscriber
from .message import Message
class PubSub:
    def __init__(self):
        self.topics = {}
        self.executor_pool = ThreadPoolExecutor(max_workers=10)
        
    def create_topic(self, topic_name):
        self.topics[topic_name] = Topic(topic_name)
        
    def get_topic(self, topic_name):
        return self.topics.get(topic_name)
    
    def subscribe(self, topic_name: str, subscriber: Subscriber):
        topic = self.get_topic(topic_name)
        if topic:
            topic.subscribe(subscriber)
    
    def unsubscriber(self, topic_name: str, subscriber: Subscriber):
        topic = self.get_topic(topic_name)
        if topic:
            topic.unsubscribe(subscriber)
        
    def publish(self, topic_name: str, message: Message):
        topic = self.get_topic(topic_name)
        if topic:
            self.executor_pool.submit(topic.publish, message)
    
    def sutdown(self):
        self.executor_pool.shutdown()
    
    