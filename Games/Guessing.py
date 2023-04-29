import random

print("Guess a number between 1 and 20")
guess_Number = random.randint(1,20)
guess = -1

while guess != guess_Number:
    guess = int(input("What number do you choose?"))

    number = random.randint(1,20)
    if guess == number:
        print("You guessed the right number")
    if guess < guess_Number:    
        print("Your guess is too low")
    if guess > guess_Number:
        print("Your guess is too high")




