'''Cho-Han, by AI Swelgart al@inventwithpython.com
The traditional Japanese game of even-odd.'''

import random, sys

japanese_numbers= {1:'ICHI', 2:'NI', 3:'SAN',
                   4:'SHI', 5:'GO', 6:'ROKU'}

print('''Cho-Han, by AI Swelgart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo cup by the
dealer sitting in thee floor. The player must guess if the dice total to an even(cho) 
or odd(han) number.''')

purse=5000

while True: # Main game loop
    #Place your bet
    print(f'You have {purse} won. How much do you bet? (or QUIT)')

    while True:
        pot= input('>')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            #This is a valid bet
            pot=int(pot) # convert pot to an interger.
            break #Exit loop once a valid bet is placed.
    

    # Roll the dice
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)

    print('The dealer swirls the cup and you hear the rattle if dice.')
    print('The dealer slams the cup on the floor, still covering dice and asks for yur bet.')
    print()
    print('     CHO(even) or HAN(odd)?')

    # Let the player bet cho or han
    while True:
        bet= input('>').upper()
        if bet != 'CHO' and bet !='HAN':
            print('Please enter either "CHO" or "HAN".' )
            continue
        else:
            break

    # Reveal the dice results
    print('The dealer lifts the cup to reveal:')
    print(f'   {japanese_numbers[dice1]} - {japanese_numbers[dice2]}')
    print(f'        {dice1}  -  {dice2}')

    # Determine if player won
    rollsEven= (dice1 + dice2)/2==0
    if rollsEven:
        correctBet='CHO'
    else:
        correctBet='HAN'

    playerWon= bet == correctBet

    # Display the bet results
    if playerWon:
        print(f'You won! You take {pot} mon')
        purse= purse + pot # add the pot from player's purse.
        print(f'The house collects a {pot// 10} non fee')

        purse= purse- (pot // 10) #the house fee is 10%
    else:
        purse= purse-pot # subtract the pot from the player's purse.
        print('You lost!')

    # Check if the player has run out of money
    if purse == 0:
        print('YOu have run out of money!')
        print('Thanks for playing!')
        sys.exit()