import random, re


class Board():
    def __init__(self, dimSize, numBombs):
        self.dimSize = dimSize
        self.numBombs = numBombs
        
        self.board = self.makeNewBoard()
        self.assignValuesToBoard()
        
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

    def assignValuesToBoard(self):
        for r in range (self.dimSize):
            for c in range(self.dimSize):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.getNumNeighboringBombs(r,c)
                           
    def getNumNeighboringBombs(self,row,col):
        numNeighboringBombs = 0
        for r in range(max(0,row-1),(min(self.dimSize-1,row+1)+1)):
            for c in range(max(0,col-1),(min(self.dimSize-1,col+1)+1)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    numNeighboringBombs += 1

    def dig(self,row,col):
        self.dug.add((row,col))
        
        if self.board([row][col]) == '*':
            return False
        elif self.board([row][col]) > 0:
            return True
        
        for r in range(max(0,row-1),(min(self.dimSize-1,row+1)+1)):
            for c in range(max(0,col-1),(min(self.dimSize-1,col+1)+1)):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
                
        return True
        
    def __str__(self) -> str:
        visibleBoard = [[None for x in range(self.dimSize)] for x in range(self.dimSize)]
        for row in range(self.dimSize):
            for col in range(self.dimSize):
                for col in range(self.dimSize):
                    if (row,col) in self.dug:
                        visibleBoard[row][col] = str(self.board[row][col])
                    else:
                        visibleBoard[row][col] = ' '
    
# play the game
def play(dimSize=10, numBombs=10):
    board = Board(dimSize, numBombs)
    
    safe = True
    
    while len(board.dug) < board.dimSize ** 2 - numBombs:
        print(board)
        # 0,0..... 0,  0 ...... 0    ,     0
        userInput = re.split(',(\\s)*', input('Where whould you like to dig? input as row, col: '))
        row, col = int(userInput[0]), int(userInput[-1])
        if row < 0 or row >= board.dimSize or col < 0 or col >= dimSize:
            print('Invalid location. Try again')
            continue
        
        safe = board.dig(row,col)
        
        

