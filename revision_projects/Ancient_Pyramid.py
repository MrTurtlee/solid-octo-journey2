# make at least 3 rooms
# 1 room must have at least 2 sub rooms
# 1 room / subroom must have at least a riddle
# 1 room / subroom must be the winning exit
# 1 room / subroom must be the doom room (loose automatically)

# you do not need to use a while loop for this, but you can if you want

import random
print("You are in a ancient pyramid in egypt")
print("You have lost you way out and don't know where to go")
print("In front of you there are 3 doors, you must choose one")

player_choice = 0

player_choice = input("Choose 1, 2, 3 or 4\n")
if player_choice == "1":
    print("You open the first door to find a giant sphinx")
    print("The sphinx asks you a riddle")
    print("What is full of holes but still holds water?")
    player_choice = input("Choose a: a rock, b: a sponge, c: cheese\n")
    if player_choice == "a":
        print("The sphinx laughs and tells you that you are wrong")
        print("The floor opens up and you are dropped into a pit of spikes")
        print("YOU LOSE")
    elif player_choice == "b":
        print("The sphinx tells frowns and tells you that you are right")
        print("A door opens up behind the sphinx, it leads to outside the pyramid")
        print("YOU WIN")
    elif player_choice == "c":
        print("The sphinx laughs and tells you that you are wrong")
        print("The floor opens up and you are dropped into a pit of spikes")
        print("YOU LOSE")
elif player_choice == "2":
    print("You open up the second door to find a room full of treasure and an exit to the pyramid")
    print("You now have enough money for the rest of your life")
    print("YOU WIN")
elif player_choice == "3":




print("Run the game again to play again")   
