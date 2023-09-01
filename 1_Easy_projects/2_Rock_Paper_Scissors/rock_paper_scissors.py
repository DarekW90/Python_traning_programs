import random

def play():
    user = input ("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    if computer == 'r':
        computer_choice = 'Rock'
    elif computer == 'p':
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'
        
        
    print ('Computer choice is: ' + computer_choice)
    if user == computer:
        return 'It\'s a tie'
    
    if isWin (user, computer):
        return 'You won!'
    
    return f'You lost!'

def isWin(player, opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
        
        
print(play())