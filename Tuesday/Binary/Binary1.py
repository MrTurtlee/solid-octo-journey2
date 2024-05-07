import random

sortedList = []
for i in range(1,101):
    sortedList.append(random.randint(1,1000))
sortedList.sort()

# x = input("What number do you want to check for?")
# middle = sortedList[int(len(sortedList)/2)]

total = 0
print(sortedList)
user_input = input("Do you want to Add or Multiply?")
if user_input == "add":
    for i in sortedList:
        total = i + total
    print(total)

if user_input == "multiplay":
    for j in sortedList:
        total = j * total
    print(total)
