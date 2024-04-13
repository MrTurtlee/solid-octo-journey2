#########################################################################
#               REVISION FOR:                                           #
#                            FURTHER VARIABLE AND INPUT USAGE           #
#                            FURTHER LISTS,                             #
#                            DICTIONARIES,                              #
#########################################################################
# Task 3:
# 3a) Make a list called 'pokemon' containing: 'charmander', 'squirtle', 'bulbasaur'
pokemon = ['charmander', 'squirtle', 'bulbasaur']
# 3b) print "Welcome Player! Pick your starter pokemon!"
print("Welcome Player! Pick your starter pokemon!")
# 3c) print the list itself
print(pokemon)
# 3d) make a variable for player_choice and make it equal to input
player_choice = input().lower()
# 3e) for the above code make sure you lower the string to all lowercase
#       you can do this by adding . at the end of input() and adding a different function
#       you can find this function in previous codes we have done

# 3f) make a while loop condition which checks if player_choice is not in the list 'pokemon'
while(not player_choice in pokemon):
    print("choose again")
    player_choice = input().lower()

print("Congratulations! You have picked:", player_choice)    
# 3g) so as long as the player does not pick a valid pokemon,
#       ask for a valid pokemon again
#       and call the player_choice with a new input

# 3h) outside the while loop (which will happen if a valid pokemon is typed)
#       print "Congratulations! You have picked:" add pokemon name
