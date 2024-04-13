# Given a list of integers nums and an integer target, 
# return the indexes of the two numbers such that they add up to target.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums, target):
    # Holiday hw - convert this to print indicies instead
    # First loop through the first value in nums
    for value in nums:
        # find the difference between the target ad current alue
        # to then search if that difference is in the list
        diff = target - value
        # check if any value in nums is equal to diff and print it
        for value2 in nums:
            if value2 == diff:
                return [value, value2]
    
    return 1

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))