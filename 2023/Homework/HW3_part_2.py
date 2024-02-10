# Task 2:
# Code a program which will copy what you type, but will stop
# when you type: 'done'
# For eg:
# if i typed: 'hi', the program will say 'hi'
# if i typed: 'asdfsdghrsea', the program will say 'asdfsdghrsea'
# if i typed: 'done', the program will say:
#               'The program has been terminated' 
#               and will finish


print("type some random stuff")
user_input = input()
while user_input != "done":
    print(user_input)
    user_input = input()
print("The program has been terminated")