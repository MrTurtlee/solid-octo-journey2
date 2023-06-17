


# dictinaries are similar to lists, but require a {key : value} link for each item
# each key represents the item's name and are usually in a string or interger data type
# while the label / value of the key can be in any data type
# data types include:
#    strings, intergers, booleans, lists, dictionaries

# creates dictionary
powers = {
    "The pigeon": "flight",
    "Brainzar": "mind reader",
    "Cyborg": "controls machines"
}

# prints item in dictionary by using its associated key (string)
print(powers["The pigeons"])
                   
# add item to dictionary
powers["Laser girl"] = "shoot lasers"

# print entire dictionary
print(powers)

# Deletees itme in a dictionary 
del powers["The pigeon"]

# Changing the value of and item in a dictionary
powers["brainzar"] = "seeing the future"