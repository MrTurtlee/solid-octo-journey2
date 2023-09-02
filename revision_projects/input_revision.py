



# 1) Create a program, which gets the user input and prints it
input_test = input()
print(input_test)
# 2) Create a list with 5 numbers amnd print the list itself
list_test = [1,2,3,4,5]
print(list_test)
# 3) print each item in the list you created above through a loop
index = 0
while index < 5:
    print(list_test[index])
    index = index + 1
# 4) create 2 or more lists with 5 items each
#       (one with only strings and the other with just numbers)
rand_list = ["apple", "banana", "egg", "air", "monkey" ]
som_list = [0,1,2,3,4,]

# 5) Make a program which asks the user, which list they want to print
#        and print the list they want (with the loop method)

user_input = input("choose a random list")
if user_input == "test":
    print(list_test)
elif user_input == "rand":
    print(rand_list)
elif user_input == "som":
    print(som_list)
# 6) Choose a list of numbers you just made and print
#      the squared value of each item (use a while loop for this)


# 7) Make 2 list with 4 numbers in each and print the 
#    multipliacation of every item combination between the 2 lists