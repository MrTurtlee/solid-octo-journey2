sword = 0

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
    player_choice = input("Do you want to go back or go down the hallway\n").lower()
    if player_choice == "hallway":
        hallway1()
    elif player_choice == "back":
        doors()

def hallway1():
    player_choice = input("You walk down the hallway to come across a door with a mushroom engraving on it.\nDo you go through it?\n").lower()
    if player_choice == "yes":
        mushroom1()
    elif player_choice == "no":
        print("You walk past the door with the mushroom engraving")
        print("You continue to walk on down the hallway until you come across a stick the size of your arm")
        stick1()
        
def stick1():
    player_choice = input("Do you pick up the stick?").lower()
    if player_choice == "yes":
        print("test")
        sword + 1
        print("You pick up the stick")
        print("Since you can not go any further down the hallway, you decide to go back to the first room")
        doors()
    elif player_choice == "no":
        print("You leave the stick")
        print("Since you can not go any further down the hallway, you decide to go back to the first room")
        doors()


def mushroom1():
    print("You open the door to find nothing but a single mushroom in the cenetre of the room")
    player_choice = input("Do you eat the mushroom\n").lower()
    if player_choice == "yes":
            print("You take the mushroom and eat it")
            print("Your body starts to grow rapidly")
            print("Soon enough you get too large for the room and break through the roof and out of the castle")
            print("Even though you are massive and don't know how to go back to normal, you are now free")
            print("YOU WIN")
    elif player_choice == "no":
        print("You turn around and exit the room")
        hallway1()
        
def Door2():
    print("You open the second door to face a large indoor play place")
    print("")



doors()
