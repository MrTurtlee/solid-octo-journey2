
# a program where there is a loop which inserts what the user 
# types into a list and when the user presses done, it ends the 
# loop and prints the list

# clue files:
#  - guessing.py for while loops
#  - furtherloops.py for adding, printing and making lists

# 1) establish a logic
# i.e:
#       a)  make a list
#       b)  ask the question / get an input
#       c) keep it into the list
#       d) keep on asking the asking question

turtle = []
flog = -1

while (flog != "done"):
    flog = input("flat floggy")
    turtle.append(flog)
    if (flog == "done"):
        break

for item in turtle:
    print(item)

