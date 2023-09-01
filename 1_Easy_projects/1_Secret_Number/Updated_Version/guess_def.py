import random 

def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0
    while user_guess != random_number:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        if user_guess < random_number:
            print('Sorry, guess again. Too low.')
        elif user_guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Congrats! You have guessed the number {random_number} correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Computer: {guess}: too high (H), too low (L), or correct (C): ').lower()

        while feedback not in ('h', 'l', 'c'):
            guessedValue = guess
            print("Please enter a correct value!")
            feedback = input(f'Computer: {guessedValue} too high (H), too low (L), or correct (C): ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly!!!')

def computer_computer(x):
    print ('Sorry not available yet .... :( )')