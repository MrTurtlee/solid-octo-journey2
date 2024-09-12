# make a list with these items:
# [10,3,2,100,34,84,132,1234,54,657,34,54536,345,65,3453,234]

# make a program which counts how many even numbers there are in 
# this list and print it

# clues:
#  - you could make a counter variable
#  - you can use a loop to check each item in the list


numbers = [10,3,2,100,34,84,132,1234,54,657,34,54536,345,65,3453,234]
counter = 0
for i in numbers:
    if i % 2 == 0:
        counter = (counter + 1)

print(counter)