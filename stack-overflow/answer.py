import typing as tp
import uuid

from comment import Comment
from commentable import Commentable
from question import Question
from user import User
from votable import Votable
from vote import Vote


class Answer(Commentable, Votable):
    def __init__(self, user: User, question: Question, answer: str = None):
        self.id = uuid.uuid4()
        self.user = user
        self.ans = answer
        self.comments = []
        self.votes = []
        self.question = question

    def get_question(self) -> str:
        return self.question

    @property
    def answer(self) -> str:
        return self.ans

    @answer.setter
    def set_answer(self, answer: str):
        self.ans = answer

    def answered_by(self) -> User:
        return self.user

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments(self) -> tp.List[Comment]:
        return self.comments

    def get_vote_count(self) -> int:
        return len(self.votes)

    def add_vote(self, userid: str, vote_type: tp.Literal["UP", "DOWN"]):
        self.votes.append(Vote(userid, vote_type))
        
    def get_votes(self) -> tp.List[Vote]:
        return self.votes
