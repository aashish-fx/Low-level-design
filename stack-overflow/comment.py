from user import User

class Comment:
    def __init__(self, user: User, comment: str = None):
        self.user = user
        self.comment = comment

    def commented_by(self) -> User:
        return self.user

    @property
    def comment(self):
        self.comment

    @comment.setter
    def comment(self, comment: str):
        self.comment = comment
