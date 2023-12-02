# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
import random

def print_two_num(nums, target):
    for i in nums:
        difference = target - 1
        checker = False
        # check if difference is in nums
        for j in nums:
            if difference == j:
                checker = True
                print(difference)
                break

            if checker == True:
                print(i)
                break
                
def randlist_generator(length):
    randlist = []
    for i in range(0, length):
        randlist.append(random.randint(0,20))
    return randlist

def main():
    print('Generated random list')
    random_list = randlist_generator(10)
    print(random_list)

    print('Enter target sum')
    target = int(input())

    print_two_num(random_list, target)

main()