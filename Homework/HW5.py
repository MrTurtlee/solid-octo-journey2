# make a program where you join 2 lists together and 
# produce a new list in descending order

def descending(given_list):
    # empty list
    new_list = []
   
    for j in range (0, len(given_list)):
        # algorithm for finding the lowest number in given_list
        max = given_list[0]
        for i in given_list:
            if max < i:
                max = i
    
        # append / add minium number to my new list
        new_list.append(max)
        given_list.remove(max)

    # return new list
    return new_list

random_list = [5, 3, 9, 1, 2, 10, 7, 8, 6, 2]
random_list_2 = [4, 15, 32, 72, 56, 1, 100, 93]
# add code to join the lists together
random_list_3 = random_list + random_list_2

new_list = descending(random_list_3)  # fix the brackets (something should be in it)
print(new_list)