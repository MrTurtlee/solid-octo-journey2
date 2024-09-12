# Task:
# Code a program which asks the following:
# Would you like to flip a coin or roll the dice? [1, 2]

# if the user types 1, 
# the program will either give "heads" or "tails"

# if the user types 2, 
# the program will give a random number between 1 and 6 inclusive.

# if the user types something different, then it will 

import random

coin = random.randint(1,2)
dice = random.randint(1,6)

print('would you like to flip a coin or roll a dice?')
print('type 1 for coin and 2 for dice')
player_chice = input()
if player_chice == '1':
    print(coin)
elif player_chice == '2':
    print(dice)