import random

print("You are in a dark room in a mysterious castle")
print("In front of you are 4 doors. You must choose one.")

player_choice = 0

while player_choice != "exit":
    player_choice = input("Choose 1, 2, 3 or 4\n")
    if player_choice == "1":
        print("You find a room full of treasure. You're rich!")
        print("GAME OVER, YOU WIN!")
    elif player_choice =="2":
        print("The door opens and an angry ogre hits you with his club")
        print("GAME OVER, YOU LOSE!")
    elif player_choice =="3":
        print("You go into the room and find a sleeping dragon")
    
        print("You can either:")
        print("1) Try to steal some of the dragon's gold")
        print("2) Try to sneak around to the dragons exit")
    
        dragon_choice = input("Type 1 or 2\n ")

        if dragon_choice == "1":
            treasure_chance = random.randint(1, 10)
            if treasure_chance <= 4:
                print("You have stolen the gold successfully and escaped to the exit!")
                print("GAME OVER, YOU WIN!")
            else:        
                print("The dragon wakes up and eats you. You are delicious")
                print("GAME OVER, YOU LOSE!")   
        elif dragon_choice == "2":
            escape_chance = random.randint(1,10)
            if escape_chance <= 6:
                print("You sneak around the dragon and escape the castle, blinking in the sunshine")
                print("GAME OVER, YOU WIN!")
            else:
                print("The sound of you walking on the coins has woken up the dragon")
                print("The dragon eats you whole in one bite. You are delicious")
                print("GAME OVER, YOU LOSE!")
    
    elif player_choice =="4":
        print("You enter a room with a sphinx")
        print("It asks you to guess what number it is thinking of, between 1 and 10")

        sphinx_number = int(input("What number do you choose?"))
        if sphinx_number == random.randint(1,10):
            print("The sphinx hisses in disapointment and lets you go past")
            print("GAME OVER, YOU WIN!")
        else:
            print("The sphinx tells you that your guess is incorrect")
            print("You are now her captive forever")  
            print("GAME OVER, YOU LOSE!")         
    
    else:
        print("Sorry, you didn't enter 1, 2, 3 or 4")

print("Run the game again to have another go.")