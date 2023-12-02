# make a program which rearranges a given list in ascending order

def ascending(given_list):
   # empty list
    new_list = []
   
    for j in range (0, len(given_list)):
        # algorithm for finding the lowest number in given_list
        min = given_list[0]
        for i in given_list:
            if min > i:
                min = i
    
        # append / add minium number to my new list
        new_list.append(min)
        given_list.remove(min)

    # return new list
    return new_list





random_list = [5, 3, 9, 1, 2, 10, 7, 8, 6, 2]
new_list = ascending(random_list)
print(new_list)