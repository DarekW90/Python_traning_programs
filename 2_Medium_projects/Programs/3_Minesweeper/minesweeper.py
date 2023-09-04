import random, re


class Board():
    def __init__(self, dimSize, numBombs):
        self.dimSize = dimSize
        self.numBombs = numBombs
        
        self.board = self.makeNewBoard()
        self.assignValuesToBoard()
        
        self.dug = set()
        
    def makeNewBoard(self):
        board = [[None for x in range(self.dimSize)] for x in range(self.dimSize)]
        
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
        for r in range(max(0,row-1),min(self.dimSize-1,row+1)+1):
            for c in range(max(0,col-1),min(self.dimSize-1,col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    numNeighboringBombs += 1
                    
        return numNeighboringBombs

    def dig(self,row,col):
        self.dug.add((row,col))
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0,row-1),min(self.dimSize-1,row+1)+1):
            for c in range(max(0,col-1),min(self.dimSize-1,col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
                
        return True
        
    def __str__(self) -> str:
        visibleBoard = [[None for x in range(self.dimSize)] for x in range(self.dimSize)]
        for row in range(self.dimSize):
            for col in range(self.dimSize):
                if (row,col) in self.dug:
                    visibleBoard[row][col] = str(self.board[row][col])
                else:
                    visibleBoard[row][col] = ' '
                    
                    
    # put this together in a string
        stringRep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dimSize):
            columns = map(lambda x: x[idx], visibleBoard)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dimSize)]
        indicesRow = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indicesRow += '  '.join(cells)
        indicesRow += '  \n'
        
        for i in range(len(visibleBoard)):
            row = visibleBoard[i]
            stringRep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            stringRep += ' |'.join(cells)
            stringRep += ' |\n'

        str_len = int(len(stringRep) / self.dimSize)
        stringRep = indicesRow + '-'*str_len + '\n' + stringRep + '-'*str_len

        return stringRep                
        
# play the game
def play(dimSize=10, numBombs=10):
    board = Board(dimSize, numBombs)
    
    safe = True
    
    while len(board.dug) < board.dimSize ** 2 - numBombs:
        print(board)
        # 0,0..... 0,  0 ...... 0    ,     0
        userInput = re.split(',(\\s)*', input('Where would you like to dig? input as row, col: '))
        row, col = int(userInput[0]), int(userInput[-1])
        if row < 0 or row >= board.dimSize or col < 0 or col >= dimSize:
            print('Invalid location. Try again')
            continue
        
        safe = board.dig(row,col)
        if not safe:
            #BOMB!
            break #game over
        
    if safe:
        print('CONGRATS!!! You win!!!')
    else:
        print('Sorry, GameOver :(')
        board.dug = [(r,c) for r in range(board.dimSize) for c in range(board.dimSize)]
        print(board)
        
if __name__ == '__main__':
    play()