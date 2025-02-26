import random


words = ['mom', 'burger', 'rat', 'bat', 'bear', 'sister']

def getWord(wordList):
    return random.choice(wordList)

def displayBoard(missedLetter, corLetters, secretWord):
    print('Missed letters:', ' '.join(missedLetter))
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in corLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    print('Current word:', ' '.join(blanks))

def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('No. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playHangmanGame():
    print('Welcome to Hangman!')
    secretWord = getWord(words)
    missedLetter = ''
    corLetters = ''
    maxGuesses = 6

    while True:
        displayBoard(missedLetter, corLetters, secretWord)
        guess = getGuess(missedLetter + corLetters)

        if guess in secretWord:
            corLetters += guess
            if all(letter in corLetters for letter in secretWord):
                print(f'Woohhoooo! "{secretWord}"! You have won!')
                break
        else:
            missedLetter += guess
            if len(missedLetter) == maxGuesses:
                displayBoard(missedLetter, corLetters, secretWord)
                print(f'Insufficient chances! The word was "{secretWord}".')
                break

playHangmanGame()