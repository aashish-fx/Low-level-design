import typing as tp
import uuid

from question import Question
from answer import Answer
from comment import Comment
from commentable import Commentable
from tag import Tag
from votable import Votable
from vote import Vote


class User:
    def __init__(self, name, email):
        self.id = uuid.uuid4()
        self.username = name
        self.email = email
        self.questions = []
        self.reputation_score = 0
        
    def add_reputation(self, reputation):
        self.reputation_score += reputation
    
    def get_reputation(self) -> float:
        return self.reputation_score

    def get_user_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def ask_question(self, question: Question):
        self.questions.append(question)
        self.add_reputation(1.1 * len(question.question))
        
    def get_asked_questions(self) -> tp.List[Question]:
        return self.questions

    def answer_question(self, question: Question, content: str) -> Answer:
        answer = Answer(self, question, content)
        question.add_answers(answer)
        self.add_reputation(1.5 * len(answer.answer))
        return answer

    def comment_on(self, commentable: Commentable, comment: str):
        commentable.add_comment(Comment(self, comment))
        self.add_reputation(1.1 * len(comment))

    def vote(self, votable: Votable, vote_type: tp.Literal["UP", "DOWN"]):
        votable.add_vote(self, vote_type)
