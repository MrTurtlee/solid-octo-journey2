# introduce the program
print('I am thinking of a 4 letter word')
print('You only have 10 attempts')

# while loop setup
attempts = 0
password = "word"

while attempts < 10:
    user_reply = input()
    if user_reply != password:
        print("Wrong, try again")
    else:
        break

    attempts = attempts + 1