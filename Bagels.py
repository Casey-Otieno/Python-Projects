''' Bagels, by AI Sweigart al@inventwithpython.com
A deductive logic game where you must quess a number based on clues.'''

import random

#secret number is a three-digit number
num_digits=3
max_quesses= 5 #you have 5 tries to guess the secret number


def main():
    print(''' Bagels, a deductive logic game.
 by AI Sweigart al@inventwithpython.com

 I am thinking of a three_digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say:        That means:
 Pico               One digit is correct but in the wrong position.
 Fermi              One digit is correct and in the correct position.
 Bagels             No digit is correct.
    ''')

    while True: #main game loop
        #This stores the secret number the player needs to guess
        secret_num= getSecretnum()
        print('I have thought of a number')
        print(f'You have {max_quesses} guesses to get it.')

        num_guesses=1
        while num_guesses <= max_quesses:
            guess=''
            #Loop untill they enter a valid guess.
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess #{num_guesses}')
                guess= input('>')

            clues= getClues(guess, secret_num)
            print(clues)
            num_guesses +=1

            if guess== secret_num:
                break #They're correct, so break out of this loop
            if num_guesses > max_quesses:
                print('You ran out of guesses.')
                print(f'The answer was {secret_num}')

    #Ask player if they want to play again
        print('Do you want to play again (yes or no)')
        if not input('>').lower().startswith('y'):
            break
print('Thanks for playing!')


def getSecretnum():
    '''Returns a string made up of num_digits uniques ranom digits.'''

    numbers=list('0123456789') #create a list of digits 0 to 9.
    random.shuffle(numbers) #Shuffle into random order

    #Get digits in the list for the secret numder
    secret_num=''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num


def getClues(guess, secret_num):
    '''Returns a string with pico, fermi, bagels for a guess and a secreet number pair.'''

    if guess == secret_num:
        return 'You got it!'

    clues=[]

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            #A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the wrong place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits.
    else:
        # Sort the clues into alphabetical order so their original order doesnt give information away.
        clues.sort()
        # Make a single string from the list of string clues
        return ''.join(clues)


#if the program is run(instead of impoerted), run the game:
if __name__ == '__main__':
    main()


