import random


with open("questions.txt", "w") as file:
    file.write("")

with open("questions.txt", "a") as file:
    for n in range(1,11):
        for i in range(1,11):
            file.write(f"{n} x {i} =\n")
        # file.write("\n")

# random question generator
with open("random.txt", "w") as file:
    file.write("")

with open("random.txt", "a") as file:
    for i in range(0,100):
        
        random_number_1 = random.randint(0,10)
        random_number_2 = random.randint(0,10)
        file.write()

# make another file called answers.txt
# 1x1=1
# 1x2=2
with open("answers.txt", "w") as file:
    file.write("")

with open("answers.txt", "a") as file:
    for n in range(1,11):        
        for i in range(1,11):
            answer = n * i
            file.write(f"{n} x {i} = {answer}\n")
        file.write("\n")

