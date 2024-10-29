class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = ""
        
    def set_piece(self, symbol) -> str:
        if self.symbol != "":
            raise ValueError("Cell already Full")
        self.symbol = symbol
        
    def get_piece(self) -> str:
        return self.symbol
        