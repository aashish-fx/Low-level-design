from answer import Answer
from commentable import Commentable
from tag import Tag
from comment import Comment
from user import User
from votable import Votable
from vote import Vote

import uuid
import typing as tp
import pendulum as pz


class Question(Commentable, Votable):
    def __init__(self, user: User, question: str, tags: tp.List[Tag] = None):
        self.tags = tags
        self.author = user
        self.question = question
        self.id = uuid.uuid4() # unique id
        self.comments = []
        self.answers = []
        self.votes = []
        self.created_at = pz.now()

    def get_question_id(self) -> str:
        return self._id

    def get_tags(self):
        return self.tags

    def get_question(self):
        return self.question

    def add_tags(self, tags: tp.Union[tp.List[Tag], Tag]):
        if isinstance(tags, list):
            self.tags.extend(tags)
        else:
            self.tags.append(tags)

    def posted_by(self):
        return self.author

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def get_comments(self) -> tp.List[Comment]:
        return self.comments

    def add_answers(self, answer: Answer):
        self.answers.append(answer)

    def get_answers(self) -> tp.List[Answer]:
        return self.answers

    def get_vote_count(self) -> int:
        return len(self.votes)

    def add_vote(self, user: User, vote_type: tp.Literal["UP", "DOWN"]):
        self.votes.append(Vote(user, vote_type))

    def get_votes(self) -> tp.List[Vote]:
        return self.votes
