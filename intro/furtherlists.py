# this is a list
spacelist = ["rocket", "planet", "asteroid", "alien"]

spacelist2 = [spacelist[0], spacelist[1]]
spacelist3 = [spacelist[2], spacelist[3]]
spacelist_moon = ["moon"]

spacelist4 = spacelist2 + spacelist_moon + spacelist3

# replace the first item
spacelist[0] = "planet zarg"

# delete item
del spacelist[0]

# add item to end of list
spacelist.append()

# print modified spacelist
for item in spacelist:
    print(item)