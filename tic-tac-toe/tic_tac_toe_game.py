from .board import Board
from .person import Person
from .move import Move
from .game_info import GameInfo

import typing as tp
class TicTacToe:
    _instance = None
    def __call__(cls):
        if not cls._instance:
            cls._instance = super(cls).__call__(cls, TicTacToe)
            cls.board = Board()
            cls.game_info = GameInfo()
            cls.moves = []
            
        return cls._instance
    
    def play(self, players: tp.List[Person]):
        while True:
            try:
                for player in players:
                    print(f"{player.get_name()} Turn")
                    print("Please Enter Move:")
                    row = self._get_valid_input("Enter row val b/w (0-2)")
                    col = self._get_valid_input("Enter col val b/w (0-2)")
                    self.make_manual_move(row, col, person=player)
            except Exception as e:
                print(str(e))
                break
             
    def _get_valid_input(self, message):
        while True:
            try:
                inp = int(input(message))
                if 0 <= inp <= 2:
                    return inp
                print("Please enter a valid input between (0-2)")
            except ValueError:
                print("Please enter a valid input between (0-2)")
    
    def make_manual_move(self, x: int, y: int, person: Person):
        cell = self.board.grid[x][y]
        move = Move(person, cell)
        self.moves.append(move.to_string())
        self.board.make_move(move)
        won = self.board.check_for_win()
        if won:
            self.game_info.set_winner(person)
            self.game_info.is_over()
            return self.announce(f"{person.get_name()} has won the game")
        if self.board.is_full():
            self.game_info.is_draw()
            self.game_info.is_over()
            return self.announce(f"Game is a draw")
        
    def get_game_info(self) -> GameInfo:
        return self.game_info
            
    def display(self):
        return self.board.display()
        
    def announce(self, message):
        return message
    
    def check_for_draw(self):
        return self.game_info.is_draw()
    
    def check_for_win(self):
        return self.game_info.is_won()

    def get_winner(self):
        return self.game_info.winner()
    
    def get_all_moves(self):
        return self.moves
    