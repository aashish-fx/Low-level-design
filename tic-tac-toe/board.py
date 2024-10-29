from .cell import Cell
from .symbol import Symbol

class Board:
    def __init__(self):
        self.board = self._create_board()
    
    def _create_board(self):
        board = []
        for i in range(3):
            rows = []
            for j in range(3):
                rows.append(Cell(i, j))
            board.append(rows)
        return board
    
    def get_cell(self, x, y) -> Cell:
        return self.board[x][y]
    
    def move(self, x, y, symbol: Symbol):
        self.board[x][y].set_piece(symbol)