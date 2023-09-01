import random
import time


print('Welcome to Secret Games:\n\nRules are simple:\nin first game you are guessing number that computer choice,\nin second game you are picking a number and then giving feedback to computer to letting computer guess.\nin third game you are giving a number and then watch that computer is playing\n')
print('Input 1: You vs Computer')
print('Input 2: Computer vs You')
print('Input 3: Computer vs Computer')

choice = int(input("\nPlease make a choice: "))


if choice == 1:
    while True:
        def guess(x):
            random_number = random.randint(1, x)
            guess = 0
            while guess != random_number:
                guess = int(input(f'Guess a number between 1 and {x}: '))
                if guess < random_number:
                    print('Sorry, guess again. Too low.')
                elif guess > random_number:
                    print('Sorry, guess again. Too high.')

            print(f'Congrats! You have guessed the number {random_number} correctly')
        guess(1000)
        escape = str(input('Continue??? Press Y to continue or N to exit: ').lower())
        if escape == 'y':
            continue
        elif escape == 'n':
            print ("Thank you for playing!")
            break
        else:
            print ("Please press y or n")



elif choice == 2:
    while True:
        print ('Think about number between 1 and 1000, and let computer guess it\n')
        def computer_guess(x):
            low = 1
            high = x
            feedback = ''
            while feedback != 'c':
                if low != high:
                    guess = random.randint(low,high)
                else:
                    guess = low
                feedback = input(f'Computer: {guess}: too high (H), too low (L), or correct (C): '.lower())

                while feedback not in ('h' , 'l' , 'c'):
                    guessedValue = guess
                    print ("Please enter correct value!")
                    feedback = input(f'Computer: {guessedValue} too high (H), too low (L), or correct (C): ').lower()

                if feedback == 'h':
                    high = guess - 1
                elif feedback == 'l':
                    low = guess + 1

            print (f'The computer guessed your number, {guess}, correctly!!!')

        computer_guess(1000)
        escape = str(input('Continue??? Press Y to continue or N to exit: ').lower())
        if escape == 'y':
            continue
        elif escape == 'n':
            print ("Thank you for playing!")
            break
        else:
            print ("Please press y or n")