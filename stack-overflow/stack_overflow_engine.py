import collections
from answer import Answer
from commentable import Commentable
from question import Question
from user import User
from votable import Votable

import typing as tp

class Engine:
    def __init__(self):
        self.users = []
        self.questions: tp.Dict[int, Question] = {}
        self.answers: tp.Dict[int, Answer] = {}
        self.tags = collections.defaultdict(list)
        
    def create_user(self, name, email) -> User:
        user = User(name=name, email=email)
        self.users.append(user)
        return user
    
    def post_question(self, user: User, question: str, tags: tp.List[str]):
        question = Question(user, question, tags)
        user.ask_question(question)
        self.questions[question.id] = question
        for tag in tags:
            self.tags[tag].append(question.id)
    
    def post_question_answer(self, user: User, question: Question, answer: str) -> Question:
        question = user.answer_question(question, Answer(question, answer))
        return question
        
    def add_comment(self, user: User, commentable: Commentable, comment: str):
        user.comment_on(commentable, comment)
    
    def get_tags(self, question: Question):
        return question.get_tags()
    
    def vote(self, user: User, question: Question, vote_type: str):
        question.add_vote(user, vote_type)
    
    def get_votes(self, votable: Votable):
        return votable.get_votes()
    
    def add_tag(self, question: Question, tag: str):
        question.add_tags(tags=tag)
        
    def answer_questions(self, user: User, question: Question, content: str) -> Answer:
        answer = user.answer_question(question, content)
        self.answers[answer.id] = answer
        return answer
        
    def get_reputation_score_of_user(self, user: User):
        return user.get_reputation()
        
    def search(self, keywords, tags: tp.Union[str, tp.List[str]], user: User):
        return [question for question in self.questions.values() 
                if question.author == user 
                or any(tag.tag in question.tags for tag in tags)]
        
    
        
    
    
        
