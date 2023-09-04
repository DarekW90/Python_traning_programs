import random


class Board():
    def __init__(self, dimSize, numBombs):
        self.dimSize = dimSize
        self.numBombs = numBombs
        
        self.board = self.makeNewBoard()
        
        self.dug = set()
        
    def makeNewBoard(self):
        board = ([None for x in range(self.dimSize) for x in range(self.dimSize)])
        
        
        bombPlanterd = 0
        while bombPlanterd < self.numBombs:
            loc = random.randint(0, self.dimSize**2-1)
            row = loc // self.dimSize
            col = loc % self.dimSize
            
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            bombPlanterd += 1
    
        return board

# play the game
def play(dimSize=10, numBombs=10):
    pass

