# Functions
# functions are like a box to keep your code in

# they are created like this:
# def = function
# print_sentance = function name
# () = parameters

def print_sentance():
    print("hello world")

print_sentance()

def print_parameters(param1, param2):
    print(param1)
    print(param2)

print_parameters("hello", "world")

# the parameters are temporary variables that are used only in 
# the function


# usage of global variable:
def print_bananans():
    print(num_bananas)

num_bananas = 2

print_bananans()

def multiply_bananas():
    # update the variable to 3 times the original num_bananas
    num_bananas = 3*num_bananas
    print_bananans()



