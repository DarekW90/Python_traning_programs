import random, string
from words import wordsEng, wordsPol



def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(word)
        
    return word.upper()

def gameSelect():
    print('Please type 1 for English words or 2 for Polish words')
    print('Wpisz 1 dla słow słownika Angielskiego, lub 2 dla słownika Polskiego')
    language = int(input('Select (1/2): '))
    
    if language == 1:
        return getValidWord(wordsEng)
    elif language == 2:
        return getValidWord(wordsPol)
    else:
        print('Invalid selection. Please choose 1 or 2.')
        return gameSelect()

def hangman():
    
    word = gameSelect()
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase + 'ĄĆĘŁŃÓŚŹŻ')
    usedLetters = set()
    
    lives = 10
    
    while len(wordLetters) > 0 and lives > 0:
        print ('You have', lives, 'lives left and you have used thease letters: ', ' '.join(usedLetters))
        
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print ('\nCurrent word: ', ' '.join(wordList),'\n')
    
        #getting user input
        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
                
            else:
                lives = lives - 1 
                
        elif userLetter in usedLetters:
            print('You have already used that character. Please try again.')
            
        else:
            print('Invalid character.')
    if lives == 0:        
        print ('\nYou died. The word is: ',word,'!!!')
    else:
        print('\nYou guessed the word',word,'!!!')
    
hangman()