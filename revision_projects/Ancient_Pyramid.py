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
while player_choice != "exit":
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
        print("You open up the third door to find a room full of venomous snakes")
        print("All the snakes in the room go right for you")
        print("YOU LOSE")
    elif player_choice == "4":
        print("You open up the door to find a T intersection")
        print("You hear a rumbling noise behind you")
        print("You look behind you to find a giant boulder rolling towards you forcing you to go in the fourth door")
        player_choice = input("Choose quicky do you want to go left, turn around and run towards the boulder(type boulder to go to the boulder) or turn right")
        if player_choice == "left":
            print("You turn left at the T intersection to find another door")
            print("You look behind you to see the giant boulder blocking your way")
            print("With no other choice you open the door in front of you")
            print("You open up the door to find a room with a 23 metre tall dragon oni with a spiked club")
            print("In one swift swing your head was perfectly blown off")
            print("YOU LOSE")
        if player_choice == "boulder":
            print("You do a full 360 and turn around to face the giant boulder")
            print("The boulder effortlessly rolls over you")
            print("ARE YOU AN IDIOT???")
            print("YOU LOSE")
        if player_choice == "right":
            print("You turn right at the T intersection to find another door")
            print("You look behind you to see that the boulder is blocking your way from going back")
            print("with no where else to go you decide to go though the door in front of you")
print("Run the game again to play again")  