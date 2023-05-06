# data types: strings, numbers, list


# list of strings in the variable: spacelist
spacelist = ["rocket", "planet", "astroid", "alien"]
#  index        0          1          2          3

# list of numbers
numberlist = [0,1,2,3,4,5]

# list of lists
list_list = [ ["a", "b", "c"], [1,2,3]]

# try and not do this
listexample = ["string", 0]

# print the first item / index 0 of spacelist
print(spacelist[0])

##############################################################
#                  Looping lists                             #
##############################################################

# example with while loop:
#spacelist = ["rocket", "planet", "astroid", "alien"]

index = 0
while (index <4):
    print(spacelist[index])
    index = index + 1

# example with for loops:
# assigning a te,poray variable called 'item' for each
#item in the list
for item in spacelist:
    print(item)

#############################################################
#                 replacing items in list                   #
#############################################################
 
examplelist2 = [1,2,3]
# index:        0 1 2

# replacing item 0 to value of 7
examplelist2[0] = 7
