# There are 2 programs to code for this hw:

# Task 1:
# Code a program which checks if what you typed is rude
# This will run until you type 'done'
# For eg:
# if i typed: 'hello', the program will say: 'safe'
# if i typed: 'fuck', the program will say: 'that's rude'
# if i typed: 'done', the program will say: 
#               'The program has been terminated'
#               and will finish

print('Give me a random word')

user_input =  input()
while user_input != "fuck":
    print("safe")       
    user_input = input()


# Answer
# while user_input != "done":
#     if user_input == "fuck":
#         print("thats pretty rude")
#     else:
#         print("safe")
# print("the program has been terimnated")
