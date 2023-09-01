import random

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
    print("Not ready yet")
    
    
    
    
    
    

