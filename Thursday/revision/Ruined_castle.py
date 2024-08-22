print("You are in a castle and must find your way out. In front of you are 3 doors. Which door do you choose")

def doors():
    player_choice = input("Which of the 3 doors do you choose? (1,2,3) \n")
    if player_choice == "1":
        Door_1()
    elif player_choice == "2":
        Door2()
    elif player_choice == "3":
        Door3()
    else:
        doors()



def Door_1():
    print("You open the door to face a long hallway")
    player_choice = input("Do you want to go back or go down the hallway\n").lower
    if player_choice == "hallway":
        hallway()
    elif player_choice == "back":
        doors()

def hallway():
    player_choice = input("You walk down the hallway to come across a door with a mushroom engraving on it.\n Do you go through it?\n").lower()
    if player_choice == "yes":
        mushroom()

def mushroom():
    print("You open the door to find nothing but a single mushroom in the cenetre of the room")
    player_choice = input("Do you eat the mushroom\n").lower
    if player_choice == "yes":
            print("You take the mushroom and eat it")
            print("Your body starts to grow rapidly")
            print("Soon enough you get too large for the room and break through the roof and out of the castle")
            print("Even though you are massive and don't know how to go back to normal, you are now free")
            print("YOU WIN")
    elif player_choice == "no":
        print("You turn around and exit the room")
        hallway()
        


doors()
