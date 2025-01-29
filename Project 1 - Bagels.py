"""
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.

This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython

Tags: short, game, puzzle
"""

import random

#Constants for the game settings
NUM_DIGITS = 3  #Number of digits in the secret number (e.g., try 1 or 10).
MAX_GUESSES = 10  #Maximum number of guesses allowed (e.g., try 1 or 100).

def main():
    """
    Main function to run the Bagels game. Explains the rules, generates
    a secret number, and handles the main game loop.
    """
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.''')

    while True:  #Main game loop.
        #Generate the secret number
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep prompting the player until a valid guess is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')

            #Get and display clues for the player's guess
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            #Check if the guess is correct
            if guess == secretNum:
                break  # Exit the loop if guessed correctly
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNum}.')

        #Ask the player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """
    Generates and returns a secret number with NUM_DIGITS unique random digits.
    """
    numbers = list('0123456789')  #Create a list of digits from 0 to 9
    random.shuffle(numbers)  #Shuffle the list into a random order

    #Form the secret number using the first NUM_DIGITS digits
    secretNum = ''.join(numbers[:NUM_DIGITS])
    return secretNum

def getClues(guess, secretNum):
    """
    Returns a string of clues for a given guess and secret number pair.
    Clues:
        - 'Fermi': A correct digit in the correct position.
        - 'Pico': A correct digit in the wrong position.
        - 'Bagels': No correct digits.
    """
    if guess == secretNum:
        return 'You got it!'

    clues = []

    #Compare each digit in the guess to the secret number
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Correct digit in the correct position
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Correct digit in the wrong position
            clues.append('Pico')

    #Return 'Bagels' if no digits are correct
    if len(clues) == 0:
        return 'Bagels'
    else:
        #Sort clues alphabetically to avoid revealing digit positions
        clues.sort()
        return ' '.join(clues)

#Run the game if the script is executed directly
if __name__ == '__main__':
    main()
