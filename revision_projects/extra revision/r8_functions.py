# copy the code from r4_import_random.py
# put the code for dice and coin into separate functions

# put the if conditions and other code into 
#another function called main

# you should have 3 functions in total and a code which starts
# the main function


import random


def coin_function(coin):
    print(coin)

def dice_function(dice):
    print(dice)

def main():
    coin = random.randint(1,2)
    dice = random.randint(1,6)

    print('would you like to flip a coin or roll a dice?')
    print('type 1 for coin and 2 for dice')
    player_choice = input()
    if player_choice == '1':
        if coin == 1:
            print("heads")
        else:
            print("tails")
    elif player_choice == '2':
        dice_function(dice)
