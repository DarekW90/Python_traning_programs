from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [ ' ' for x in range(9)]
        self.currentWinner = None ############################################################################
        
    def printBoard(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')
            
    def availableMoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        
    
    def winner(self, square, letter):
        
        # check row
        rowInd = square // 3
        row = self.board[rowInd*3 : (rowInd +1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        colInd = square % 3
        column = [self.board[colInd+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] # left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]] # right to left
            if all([spot == letter for spot in diagonal2]):
                return True
            
        #if all of thease fail
        return False
    
    def emptySquares(self):
        return self.board.count(' ')
    
    def numEmptySquares(self):
        return len(self.availableMoves())
    
    def makeMove(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False    
        
def play(game, x_player, o_player, printGame=True):
    if printGame:
        game.printBoardNums()
        
    letter = 'X'
    
    while game.emptySquares():
        if letter == 'O':
            square = o_player.getMove(game)
        else:
            square = x_player.getMove(game)
            
        if game.makeMove(square,letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.printBoard() ############################################################################
                print('')
                
            if game.currentWinner:
                if printGame:
                    print(letter + ' wins!')
                return letter
            
            letter = 'O' if letter == 'X' else 'X'
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'
        
        if printGame:
            print('It\'s a tie!')
            
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t,x_player,o_player,printGame=True)