from .cell import Cell
from .symbol import Symbol
from .move import Move

class Board:
    def __init__(self):
        self.grid = self._create_board()
        self.moves = 0
    
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
    
    def make_move(self, move: Move):
        if not self.is_full():
            cell = move.get_cell()
            symbol = move.get_person().get_symbol()
            cell.set_piece(symbol)
            self.moves += 1
        else:
            raise ValueError("No. of Moves finished")
    
    def is_full(self):
        return self.moves == 9
    
    def mo(self):
        ...
    
    def display(self):
        for i in range(3):
            for j in range(3):
                print(self.grid[i][j].get_piece(), " ")
            print("\n")
        
    def check_for_win(self, move: Move):
        piece = move.get_person().get_symbol()
        x, y = move.get_cell().get_coordinates()
        
        match_found = True
        for i in range(3):
            if self.grid[i][y].get_piece() != piece:
                match_found = False
                break
        if match_found:
            return True
        
        match_found = True
        for j in range(3):
            if self.grid[x][j].get_piece() != piece: 
                match_found = False
                break
            
        if match_found:
            return True
        
        match_found = True
        for i in range(3):
            if self.grid[i][i].get_piece() != piece:
                match_found = False
                break
        
        if match_found:
            return True
        
        i, j = 0, 2
        match_found = True
        while j > 0:
            if self.grid[i][j].get_piece() != piece:
                match_found = False
                break 
            i += 1
            j -= 1
        if match_found:
            return True
        
        return False
    
    
    
    