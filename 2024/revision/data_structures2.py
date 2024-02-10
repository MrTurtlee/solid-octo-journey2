#########################################################################
#               REVISION FOR:                                           #
#                            FURTHER VARIABLE AND INPUT USAGE           #
#                            FURTHER LISTS,                             #
#                            DICTIONARIES,                              #
#########################################################################

#################################
#             Setup             #
#################################      
# 3a) Make a list called 'starter_pokemons' containing: 'charmander', 'squirtle', 'bulbasaur'
starter_pokemon = ['charmander', 'squirtle', 'bulbasaur']
# 3b) Make an empty dictionary called 'characters'
characters = {}

#######################################
#   Pokemon Red, Blue, Yellow Intro   #
#######################################

# 3c) print the following:
#       Note: You can split the below into multiple prints or put them all into one
#           "Hello there! Welcome to the world of Pokémon! 
#           My name is Oak! People call me the Pokémon Prof! 
#           This world is inhabited by creatures called Pokémon! 
#           For some people, Pokémon are pets. Other use them for fights. 
#           Myself… I study Pokémon as a profession. 
#           But first, tell me a little about yourself.
#           Now tell me. Are you a boy?
#           Or are you a girl?

print("Hello there! Welcome to the world of Pokémon!")
print(" My name is Oak! People call me the Pokémon Prof!")
print("This world is inhabited by creatures called Pokémon!")
print("For some people, Pokémon are pets. Other use them for fights.")
print("Myself… I study Pokémon as a profession.")
print("But first, tell me a little about yourself.")
print("Now tell me. Are you a boy?")
print("Or are you a girl?")



# 3d) edit the 'characters' dictionary so that there is:
#           a new key named: 'main_character' 
#           and an empty dictionary as its value

characters["main_character"] = {}


# 3e) create a variable to store the player's gender and give it the input()

gender = input().lower()


# 3f) add a 'gender' key to the 'main_character' key and give it the value we got in 3e)
#       Clue 1: to visualise, this is what the dictionary should look like:
#           characters = {
#                           'main_character' = {
#                               'gender' = 'something',
#                            },
#                        }
#       Clue 2: if you have done 3d), you should know that to edit a dictionary, you can just do:
#               dictionary_name[key_name] = whatever_value

#               to edit a dictionary in a dictionary you can do:
#               dictionary_name[sub_dict_name][sub_dict_key] = whatever_value 

characters["main_character"]["gender"] = gender


# 3g) print the following:
#       "What is your name?"

print("what is your name")

# 3h) make a variable to store the player name and give it to the 'main_character' dictionary like in 3f)
#       but make the key name as 'name'

name = input()
characters["main_character"]["name"] = name

# 3f) print the following:
#           "Right! So your name is <player>! 
#            This is my grandson. He's been your rival since you were a baby. 
#            …Erm, what is his name again? 

print(f"Right! So your name is {characters['main_character']['name']}!")
print("This is my grandson. He's been your rival since you were a baby.")
print("…Erm, what is his name again?")

# 3g) make a variable to store the rival name

rival_name = input()

# 3h) edit the 'characters' dictionary so that there is:
#           a new key named: 'rival' 
#           and an empty dictionary as its value

characters['rival'] = {}

# 3i) similar to 3f) and 3h), add the rival's name into his 'rival' dictionary 
#       make sure the key for his name is also just 'name'

characters['rival']["name"] = rival_name

# 3j) print the following:
#       "That's right! I remember now! 
#        His name is <rival>! <player>! 
#        Your very own Pokémon legend is about to unfold! 
#        A world of dreams and adventures with Pokémon awaits! Let's go!
#        [Skip to selecting pokemon]"

print("That's right! I remember now!")
print(f"His name is {characters['rival']['name']}! {characters['main_character']['name']}!")
print("Your very own Pokémon legend is about to unfold!")
print("A world of dreams and adventures with Pokémon awaits! Let's go!")
print("[Skip to selecting pokemon]")

###################################
#        Selecting Pokemon        #
#  while, input, print, variables #
###################################  

# 3k) print the following:
#       "Here, <player>! There are 3 Pokémon here! Haha! 
#       They are inside the Poké Balls. 
#       When I was young, I was a serious Pokémon trainer! 
#       In my old age, I have only 3 left, but you can have one!
#       Now, <player>, which Pokémon do you want?"

print(f"Here, {characters['main_character']['name']}! There are 3 pokémon here! Haha!")
print("They are inside the Poké Balls.")
print("When I was young, I was a serious Pokémon trainer!")
print("In my old age, I have only 3 left, but you can have one!")
print(f"Now, {characters['main_character']['name']}, Which Pokémon do you want?")

# 3l) print the list itself

print(starter_pokemon)

# 3m) make a variable for player_choice and make it equal to input
player_choice = input().lower()

# 3n) for the above code make sure you lower the string to all lowercase
#       you can do this by adding .lower() at the end of input()
#       you can find this function in previous codes we have done


# 3o) make a program which setups the 
#       Steps:
#           1) make a while loop condition which checks if player_choice is not in the list 'pokemon'
#           2) if the above while condition is true,
#               i) ask for a valid pokemon again
#               ii) and call the player_choice with a new input
#           3) outside the while loop (which will happen if a valid pokemon is typed)
#               i) print "So! You want <selected pokemon name>? This Pokémon is really energetic!"

while(not player_choice in starter_pokemon):
    print("choose again")
    player_choice = input().lower()
print("so! You want", player_choice, "? This Pokémon is really energetic!")

# 3p) add a 'pokemon' key to the 'main_character' and set its value to what you picked"
characters["main_character"]["Pokémon"] = player_choice

# 3q) print the characters dictionary:
print(characters)

###################################
#    Editing starter_pokemons     #
#                                 #
###################################  
# 3p) delete the starter pokemon from the starter_pokemon list