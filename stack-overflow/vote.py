import typing as tp

from user import User


class Vote:
    def __init__(self, user: User, vote_type: str = tp.Literal["UP", "DOWN"]):
        self.user = user
        self.vote_type = vote_type

    def get_vote_type(self) -> str:
        return self.vote_type

    def voted_by(self) -> str:
        return self.user
