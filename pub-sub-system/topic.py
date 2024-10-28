class Topic:
    def __init__(self, name):
        self.name = name
        self.messages = []
        self.subscribers = []
    
    def get_name(self):
        return self.name
    
    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber.receive(message, self)
            
        # self.messages.append(message)
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
                    
    