from rock_paper_scissors import play1, play2

def printMenu():
    print('Welcome to Rock Paper Scissors Game:')
    print('Game one: You vs Computer: you pick one of three possibilities and check your luck vs computer')
    print('Game two: You set how many games will be played in Computer vs Computer game and then you watch.')
    
    
def getChoice():
     while True:
        print ('\nInput 1: You vs Computer')
        print ('Input 2: Computer vs Computer')
        choice = input("\nPlease make a choice (1/2): ")
        
        if choice in ('1', '2'):
            return choice
        else:
            print('\nInvalid value: please enter 1 or 2')
        
def main():
    printMenu()
    
    while True:
        choice = getChoice()
        
        if choice == '1':
            result = play1()
            print('\n' + result)
        elif choice == '2':
            result = play2()
            print(result)
    
        escape = input('\nContinue? Press Y to continue or N to exit: ').lower()
        while escape not in ('y','n'):
            print ("Please enter correct value: ")
            escape = input('Continue? Press Y to continue or N to exit: ').lower()
        if escape != 'y':
            print("\nThank you for playing!")
            break
        
if __name__ == "__main__":
    main()