from guess_def import guess, computer_guess, computer_computer

def main():
    print('Welcome to Secret Games:\n\nRules are simple:\nin the first game, you are guessing a number that the computer chooses,\nin the second game, you are picking a number and then giving feedback to the computer to let the computer guess.\nin the third game, you are giving a number and then watching the computer play\n')
    
    while True:
        print('Input 1: You vs Computer')
        print('Input 2: Computer vs You')
        print('Input 3: Computer vs Computer')
        
        choice = input("\nPlease make a choice (1/2/3): ")
        
        if choice == '1':
            guess(1000)
        elif choice == '2':
            computer_guess(1000)
        elif choice == '3':
            computer_computer(1000)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        escape = input('Continue? Press Y to continue or N to exit: ').lower()
        
        while escape not in ('y','n'):
            print ("Please enter correct value: ")
            escape = input('Continue? Press Y to continue or N to exit: ').lower()
        if escape != 'y':
            print("\nThank you for playing!")
            break

if __name__ == "__main__":
    main()
