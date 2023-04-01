aliens = 2
password = "ALIENS"

print("Quickly! Aliens are invading the planet.")
print("You need to activate the global defense platforms.")
print("Hope you know the password, for Earth's sake...\n")
print("------------------------------------------------------------")
print("           WELCOME TO THE GLOBAL DEFENCE NETWORK            ")
print("------------------------------------------------------------")

# .upper() : converts strings to all uppercase
guess = input("please enter the password: ").upper()

while guess != password:
    print("\nINCORRECT PASSWORD.\n")
    
    # aliens = aliens ^ 2


    aliens = aliens ** 2
    print("There are", aliens, "aliens are now on Earth. Try again! ")

    # If there are more than 8 billion aliens, break loop
    if aliens > 8 * 10**9:
        break

    # GIve clue if there are more than 200 aliens
    # alternate condition: aliens == 256
    if aliens > 200 and aliens < 60000:
        option = input("Choose a clue you want: A, B, or C".upper())
        if option == "A":
            print("Weird looking thing")
        elif option == "B":
            print("They're here")
        elif option == "C":
            print("What's the name of the game you are playing?")
        else:
            print("You wasted your chance and type the wrong clue")
   
    # If there are more than 60,000 aliens, give clue
    if aliens > 6 * 10**4:
        print("\nPassword hint: the things that are attacking us.\n")    
   
    # print guess input line again
    guess = input("please enter the password: ").upper()
# After while loop breaks, check the number of aliens and print a certain line
if aliens > 8 * 10**9:
    print("Nooooooo! The aliens have outnumberedus. All is lost")
else:
    print("Hooray! We won the fight and the world is saved!")
