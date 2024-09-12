# make a program which asks you one random addition math question
# and asks you until you get the answer correct
# every time you run the program, you should be asked a new question

# The program should end when you get the answer correct

# clue files:
# - guessing .py for using random import
# - guessing.py for using while loops until a
#      certain condition is met

import random

random_number1 = random.randint(1,10)
random_number2 = random.randint(1,10)
answer = random_number1 + random_number2
user_input = "i"

print("what is", random_number1, "+", random_number2, "?")
user_input = int(input())

if (user_input == answer):
    print("You are correct")
else:
    print("You are not correct")

