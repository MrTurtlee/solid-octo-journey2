# Functions is a term used to represent blocks of code with a 
# title attached to it.

# to make a function, use: def name() :
def printing_hello ():
    print ("hello")

# need to call the name of the function to run it
printing_hello()

# thre are 2 types of functions.
# one is void and the other is a return function
# The void function is a function that doesn't give anything like the
# function above

# This function is a return function
def return_value (input1):
    # where input1 is an int
    input1 = input1 * 10
    return input1

user_input = int(input("Give number"))
calculate_result = return_value(user_input)


# new coding terms:
# - function
# - perameters => represent the temporary variables within
# the function brackets
