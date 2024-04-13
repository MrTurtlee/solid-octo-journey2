example_list = [1,4,9,2,6,8,7,11]

# Exercise 1:
# Make an algorithm which prints every even number in the example_list:

for i in example_list:
    if i % 2 == 0:
        print(i)

# Exercise 2:
# Make an algorithm which prints the indices of every odd number in the example_list

i = 0
while i < len(example_list):
    if example_list[i] % 2 == 0:
        print(i)
        

# Exercise 3:
# Make an algorithm which prints every multiple combination in example_list.
# i.e.:
#   1x1, 1x4, 1x9, ..., 1x11, 4x1, 4x4, 4x9, ..., 4x11, 9x1, 9x4, ... 9x11, ... 11x11
 
for i in example_list:
    for j in example_list:
        print(i, 'x', j)
        

# Clue Files:
#   if you have no idea how to do this, we have done something similar in timestables.py
#   if you do not have this file, let me know and I will give you the python book for your
#   revision.

# Upon completion, do 1_twosum.py by yourself 