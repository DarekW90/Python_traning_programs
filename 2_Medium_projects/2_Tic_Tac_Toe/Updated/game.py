from player import HumanPlayer, RandomComputerPlayer, AiComputerPlayer
import time
import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.currentWinner = None

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
        row = self.board[rowInd*3: (rowInd + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        colInd = square % 3
        column = [self.board[colInd+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of thease fail
        return False

    def emptySquares(self):
        return self.board.count(' ')

    def numEmptySquares(self):
        return len(self.availableMoves())

    def makeMove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False
    
    
def modeSelect():
    print('Please select mode:\n')
    print('1. Player vs Player - in development')
    print('2. Player vs Computer - Easy')
    print('3. Player vs Computer - Hard')
    
    return int(input('\nPlease choose game mode(1/2/3): '))
    
def menu():
    print('Who start??\n')
    print('1. Player')
    print('2. Computer')
    print('3. Random choice')

    whoStart =  int(input('\nPlease choose who start(1/2/3): '))
    return whoStart
    
def play(game, x_player, o_player, printGame=True):

    #modeSelect()
    whoStart = menu()
    
    if printGame:
        game.printBoardNums()
        
    if whoStart == 1:
        letter = 'O'
    elif whoStart == 2:
        letter = 'X'
    else:
        letter = random.choice(['X', 'O'])

    while game.emptySquares():
        if letter == 'X':
            square = o_player.getMove(game)
        elif letter == 'O':
            square = x_player.getMove(game)


        if game.makeMove(square, letter):
            if printGame:
                print(letter + f' makes a move to square {square}')
                game.printBoard()
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

        # tiny break
        time.sleep(0.75)

    if printGame:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    gameMode = modeSelect()
    if gameMode == 1:
        o_player = HumanPlayer('O')
    elif gameMode == 2:
        o_player = RandomComputerPlayer('O')
    elif gameMode == 3:
        o_player = AiComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, printGame=True)
