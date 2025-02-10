"""
Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.

This code is available at https://nostarch.com/big-book-small-python-programming
A version of this game is featured in the book, "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython

Tags: short, game, puzzle
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10 

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

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer was {secretNum}.')
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """
    Generates and returns a secret number with NUM_DIGITS unique random digits.
    """
    numbers = list('0123456789')  
    random.shuffle(numbers) 

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

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()



'''                    Answering the Questions for the Project

What happens when you change the NUM_DIGITS constant?
    Changing the NUM_DIGITS constant would change the number of digits that are in the secret number
What happens when you change the MAX_GUESSES constant?
    Changing the MAX_GUESSES constant allows for more or less guesses for the problem
What happens if you set NUM_DIGITS to a number larger than 10?
    Setting the NUM_DIGITS to a number larger than 10 would result in a out of range index error
What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?
    Replacing the secret number with '123' would result in the secret number being '123' permanently and would make the random completely useless
What error message do you get if you delete or comment out numGuesses = 1 on line 34?
    "UnboundLocalError: local variable 'numGuesses' referenced before assignment"
What happens if you delete or comment out random.shuffle(numbers) on line 62?
    The numbers will always be 012 if there are three digits as you are not changing its order
What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?
    The player would never be able to know if there answer is correct
What happens if you comment out numGuesses += 1 on line 44?
    There would be an infinite loop as the numGuesses will always be less than the max guess as you are not increasing it





'''
