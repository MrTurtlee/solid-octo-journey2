# 1) code a variable where it gets an input number from the user
#    make sure you convert it to int

# 2) make a function called multiplier(num)
# 3) make a variable outside of the 
#       function to equal to the function
#       that you just made

# 4) within the function, 
#       multiply num by 100 and return it
# 5) print the variable which you made
#       it equal to the function


print("Give me a random number")
user_answer = int(input())

def multiplier(num):
    a = num* 100
    return a

final_number = multiplier(user_answer)
print(final_number)