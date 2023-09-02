import random
import time

def isWin(player, opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def getUserChoice():
    choices = {'r' : 'Rock', 'p' : 'Paper', 's' : 'Scissors'}
    while True:
        user = input ("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
        if user in choices:
            return user, choices[user]
        else:
            print ('Please enter correct value (r,p,s) ...')
            
            
def play1():
    user, userChoice = getUserChoice()
    
    choices = {'r' : 'Rock', 'p' : 'Paper', 's' : 'Scissors'}
    
    computerChoice = list(choices.keys())
    computer = random.choice(computerChoice)
    computerChoice = choices[computer]
    
    print ('\nYour choice is: ' + userChoice)
    print ('Computer choice is: ' + computerChoice)
    
    if user == computer:
        return '>> It\'s a tie <<'
    
    if isWin (user, computer):
        return '>> You won! <<'
    
    return '>> You lost! <<'


def play2():
    
    player1 = input('Set name for Computer1: ')
    player2 = input('Set name for Computer2: ')
    
    i = int(input("Ile rund ma zostać rozegranych? : "))
    ties = 0
    player1Wins = 0
    player2Wins = 0
    
    for x in range(i):
        print(f'\n ***** Round:{x+1} *****')
        
        choices = {'r' : 'Rock', 'p' : 'Paper', 's' : 'Scissors'}
        
        computer1Choice = list(choices.keys())
        computer2Choice = list(choices.keys())
        computer1 = random.choice(computer1Choice)
        computer2 = random.choice(computer2Choice)
        computer1Choice = choices[computer1]
        computer2Choice = choices[computer2]
        
        print (f'\n{player1} choice is: {computer1Choice}')
        print (f'\n{player2} choice is: {computer2Choice}')
        
        
        #print ('Computer choice is: ' + computerChoice)
        
        if computer1 == computer2:
            print ('\n>> It\'s a tie <<')
            ties += 1
        elif isWin (computer1, computer2):
            print(f'\n>> {player1} won! <<')
            player1Wins += 1
        else: 
            print(f'\n>> {player2} won! <<')
            player2Wins += 1
        time.sleep(1)
            
    print (f'\nFinal Score {player1} wins {player1Wins} times, {player2} wins {player2Wins} times, and there were {ties} ties')
    
    if player1Wins > player2Wins:
        print(f">>> {player1} is a winner! <<<")
    elif player1Wins < player2Wins:
        print(f'>>> {player2} is a winner! <<<')
    else:
        print('Its a Tie!')
    
    
    
    
    
    

