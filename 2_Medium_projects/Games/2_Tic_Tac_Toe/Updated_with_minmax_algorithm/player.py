import math, random

class Player:
    def __init__ (self, letter):
        # X or O
        self.letter = letter
        
    def getMove(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__ (self, letter):
        super().__init__(letter)
        
    def getMove(self, game):
        square = random.choice(game.availableMoves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getMove(self,game):
        validSquare = False
        val = None
        while not validSquare:
            square = input('Please, choose square(0-9): ')
            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print ('Invalid square. Try again')
                
        return val
    
class AiComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getMove(self, game):
        if len(game.availableMoves()) == 9:
            square = random.choice(game.availableMoves())
        else:
            # get the square based off the minmax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        maxPlayer = self.letter # player
        otherPlayer = 'O' if player == 'X' else 'X'
        
        if state.currentWinner == otherPlayer:
            return { 'position':None,
                    'score': 1 * (state.numEmptySquares() + 1) if otherPlayer == maxPlayer else -1 * (state.numEmptySquares() + 1)

                }
            
        elif not state.emptySquares():
            return {'position':None, 'score': 0}
        
        # initialize dictionaries
        if player == maxPlayer:
            best = {'position':None, 'score': -math.inf} # each score should maximalize
        else:
            best = {'position':None, 'score': math.inf} # each score should minimalize
            
        for possibleMove in state.availableMoves():
            # 1. make a move, try that spot
            state.makeMove(possibleMove, player)
            
            # 2. recurse using minmax to simulate a game after making that move
            simScore = self.minimax(state,otherPlayer)
            
            # 3. undo the move
            state.board[possibleMove] = ' '
            state.currentWinner = None
            simScore['position'] = possibleMove
            
            # 4. update the dict if necessary
            if player == maxPlayer:
                if simScore['score'] > best['score']:
                    best = simScore # replace best score
            else:
                if simScore['score'] < best['score']:
                    best = simScore # replace best score
                    
                    
        return best