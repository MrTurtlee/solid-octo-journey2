#################################################################
#                       Homework Description:                   #
#################################################################
# for hw, you guys will be doing a bit about permutation
# math, you can search it up if you want

# Specifically, code 10P2 and print the answer which we will
# compare in class

#################################################################
#                           Clues                               #
#################################################################
# the format for 10P2 is related to [ nPr = n! / (n-r)! ] 
# where the ! means for eg:
# 10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1

# so you can substitute 10 into n, and 2 into r

# if you still don't understand, you can search the math up on google
# to get the answer and the working out solution, 
# but you still need to code it


# code for 10!
numerator =  1
for i in range (1,11):
    numerator = numerator * i


other_num =  1
for i in range (1,9):
    other_num = other_num * i

print(numerator/other_num)

