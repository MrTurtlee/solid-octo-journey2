# Functions
# functions are like a box to keep your code in

# they are created like this:
# def = function
# print_sentance = function name
# () = parameters

# first tu/ype
def print_sentance():
    print("hello world")

print_sentance()

# second type
def print_parameters(param1, param2):
    print(param1)
    print(param2)

print_parameters("hello", "world")

# third type
def return_value():
    random_num = 1
    return random_num
one = return_value
print(one)

# global variables, temporary variables
# global variables are declared outside and on top of your file
# and can be used everywhere in the file

# temporary variables are declared inside a function
# and can only be used in that function