from .subscriber import Subscriber
from .pub_sub import PubSub
from .publisher import Publisher
from .message import Message

class PubSubDemo:
    @staticmethod
    def run():
        pubsub = PubSub()
        subscriber1 = Subscriber("subscriber1")
        subscriber2 = Subscriber("subscriber2")
        
        pubsub.create_topic("topic1")
        pubsub.create_topic("topic2")
        
        pubsub.subscribe("topic1", subscriber1)
        pubsub.subscribe("topic2", subscriber2)
        
        publisher1 = Publisher("publisher1")
        publisher2 = Publisher("publisher2")
        
        publisher1.publish(pubsub.get_topic("topic1"), Message("Hi how are you", publisher1))
        publisher2.publish(pubsub.get_topic("topic2"), Message("i am fine", publisher2))
        
        
        
if __name__ == "__main__":
    PubSubDemo.run()