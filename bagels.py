import random

from xdg.Locale import langs

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''
    Guess the number !
    Try to guess the number .Here are some clues :
    When I say :            That means:
        Pico                    One digit is correct but in the wrong position
        Fermi                   One digit is correct and in the right position
        Bagels                  No digit is correct

    ''')

    while True:
        secretNum = getSecretNum()
        print(f"You have {MAX_GUESSES} guess to get it")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess {numGuesses}')
                guess = input()

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You run out of guesses .")
                print(f'The answer Is {secretNum}')

        print('Do You Want to play again ? (Yes or no)')
        if not input('').lower().startswith('y'):
            break

    print('Thank You for Playing !')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return "You touch the Point"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bangels'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()