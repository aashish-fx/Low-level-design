from .tic_tac_toe_game import TicTacToe
from .person import Person
class TicTacToeDemo:
    
    @staticmethod
    def run():
        game = TicTacToe()
        person1 = Person("A")
        person2 = Person("C")
        game.play([person1, person2])
        game_info = game.game_info()
        print(game_info.to_string())
        
if __name__ == "__main__":
    TicTacToeDemo.run()