




def sum_list(num_list):
    total = 0
    for number in num_list:
        total = total + number    
    
    return total

def multiply_list(num_list):
    total = 1
    for number in num_list:
        total = total * number

    return total

def find_highest_number(num_list):

    i = 0
    find_highest_number = 0
    while index < 7:
        if highest_number <  num_list[index]:
           highest_number =  num_list[index]
        index +=1

    return highest_number

def main():
    # make a list with 7 random numbers
    num_list = [10,12,13,14,15,16,17]

    # function to add all numbers in list
    total = sum_list(num_list)
    print("The total is", total)

    # function to multiply all numbers in list
    product = multiply_list(num_list)
    print("The product is", product)

    # Medium: function to find the highest number in the list
    product = multiply_list(num_list)
    print("The highest number is", product)

    # Medium: funtion to find the lowest number in the list

    # Medium: function to print every 2nd number in the list

    # Medium: function to print every 3rd number in the list

    # Hard: function to print every item in the list backwards
    # - dont need to do this one

    # Hard: function to add every number by 1, then multiply it to total


main()