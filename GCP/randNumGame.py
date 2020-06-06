#!/usr/bin/env python3

# PURPOSE: simple number guessing game

import os
import random

# set initial variables
goAgain = 'Y'
goAgainTemp = None
maxGuess = 3
outcome = None
status = ['win', 'lose']

# Play the game

while (goAgain == 'Y'):
    os.system('clear')
    print("Guess a number bewteen 1-100. You have {attempt} attempts, make 'em count!.\n".format(attempt=maxGuess))
    guessThisNum = random.randint(1,100)
    # print('Test round. The number is: {number}.\n\n'.format(number=guessThisNum)) # disable for real game

    count = 1
    while (count < maxGuess):
        guess = int(input('Guess #{attempt}: '.format(attempt=count)))
        if guess == guessThisNum:
            print("You nailed it! You're pretty good at this.\n")
            outcome = status[0]
            break
        else:
            print('WRONG ANSWER! Try again.')
            count += 1
    while (count == maxGuess):
        guess = int(input('Last chance...you better get it right! '))
        if guess == guessThisNum:
            print('Whew! That was close. You got it!')
            outcome = status[0]
            break
        else:
            print('Nope. The number was: {number}. You lose!'.format(number = guessThisNum))
            outcome = status[1]
            break

    goAgainTemp = input('Do you want to play again? (Y/N) ')
    goAgain = goAgainTemp.capitalize()

if outcome == status[0]:
    print('Well done! Come back and play again another day!\n')
else:
    print('\nCome back when you grow a spine.\n')

### Opportunties for improvement ###
# Create 'easy'. 'med' 'hard' option for player to choose (harder has broader number range)
