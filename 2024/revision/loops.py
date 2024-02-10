#########################################################################
#               REVISION FOR:                                           #
#                            WHILE LOOPS,                               #                         
#                            FOR LOOPS,                                 #                        
#                            LISTS,                                     #
#########################################################################
# Task 2:
# 2a) print the following: "Counting numbers from 0 to 9 with a while loop"
print("Counting numbers from 0 to 9 with a while loop")
# 2b) make a variable called counter and make it equal to 0
# 2c) make a while loop with the following condition:
#               [counter is less than 10]
# 2d) within the while loop print the following as long as the above condition is true
#               [print the counter variable]
counter = 0
while (counter < 10):
    print(counter)
    counter = counter + 1

# 2e) print the following: "Counting numbers from 0 to 9 with a for loop"
print("Counting numbers from 0 to 9 with a for loop")
# 2f) make a for loop which does the same thing (printing numbers from 0-9)
for i in range(0,10):
    print(i)


# 2g) print the following: "When I look around the room I can see:"
print("When I look around the room I can see:")

# 2g) make a variable called room_items and make it equal to a list containing
#       10 items which you can see in the room you are in
room_items = ["table", "chair", "bed", "laptop", "pillow", "blanket", "windows", "wood floor"]

# 2h) using a while loop, print each item in the list
#       * think about how index works in lists
#       * you can make a variable like in the previous while loop task 
#           which can be used to access the list items
index = 0
while (index != 10):
    print(room_items[index])
    index = index +1


# 2i) using a for loop, print each item in the list
#       * basically same thing as previous for loop task
    
for i in room_items:
    print(i)