# Task:
# Code a program which asks this riddle:
# "What walks on four legs in the morning, 
# two legs in the afternoon, three legs in the evening, 
# and no legs at night?"

# Before the program asks for user input it should print this:
# "Give your answer in all lower case."

# if the user types: "human"
# the program will say: "you are correct!"
# however if the user types something different, 
# the program will say: "you are incorrect"


print('What walks on four legs in the morning, two legs in the afternoon , three legs in the evening, and no legs at night?')
user_input = input()
if user_input == "human":
    print('You are correct')
elif user_input != 'human':
    print('Youw are wrong')