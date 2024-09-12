words = input()
random_list = []

while words != 'done':
    random_list.append(words)
    # how will you get a new input here into your words
    words = input()
    
print(random_list)