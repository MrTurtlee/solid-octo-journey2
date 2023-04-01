import random

print("Guess a number between 1 and 20")
guess_Number = int(input("What number do you choose?"))

number = random.randint(1,20)
if guess_Number == number:
    print("What number do you choose?")







