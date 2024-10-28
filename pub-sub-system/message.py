class Message:
    def __init__(self, content, published_by):
        self.content = content
        self.published_by = published_by
    
    def get_content(self):
        return self.content
    
    def publisher(self):
        return self.published_by
    
    
    