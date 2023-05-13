# create a list with numbers ranging from 1 to 5
# and call it num_list
num_list = [1, 2, 3, 4, 5]

# create amother list with 5 consecutive odd numbers
# and call it odd_list
odd_list = [1, 3, 5, 7, 9 ]

# manually prints the difference of the first item in
# both lists
# this is a clue
print(odd_list[0] - num_list[0])

# for loop to print the difference of every item in
# both lists
for i in range(0,5):
    print(odd_list[i] - num_list[i])
