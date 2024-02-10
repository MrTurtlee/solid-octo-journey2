#########################################################################
#               REVISION FOR:                                           #
#                            PRINT,                                     #
#                            INT,                                       #
#                            INPUT,                                     #
#                            IF, ELIF,                                  #
#                            VARIABLES,                                 #
#                            MATH OPERATORS,                            #
#                            TERMINAL                                   #
#########################################################################
# Task 1:
# 1a) print "Hello World"
print("hello")
# 1b) print "What is (12 x 12 + 6) / 2 - 5 ?"
print("What is (12 x 12 + 6) / 2 - 5 ?")
# 1c) make a variable called answer and make it equal to (12 x 12 + 6) / 2 - 5
answer = (12 * 12 + 6) / 2 - 5
# 1d) make a variable called user_answer and make it equal to the input()
# *consider if you need int() as well
user_answer = int(input())
# 1e) make an if statement which checks if user_answer is equal to answer
# and if it is, print "Congratulations!"
if user_answer == answer:
    print("congratulations")
# 1f) make an elif statement which checks if the user_answer is not equal to answer
# and if it is, print ("Oh no! You got it wrong")
elif user_answer != answer:
    print("Oh no! You got it wrong")
# 1g) use the terminal to run the program. 
#       you cannot use the play button on the top right of the vsc
#     Clues for 1g:
#       i) you will first need to enter the folder which your program is in
#              terminal command: cd <folder name>
#      ii) you will then need to run your program
#              terminal command: python <program name>


