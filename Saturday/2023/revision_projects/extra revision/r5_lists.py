# Task:
# Make a shopping list with the
# following items:
# apple, banana, crabs, donuts, eggplant

# Print the following story out.
# "Mother: Dear, I want you to buy these now!"
# [print list]
# "Father: How about some chocolate?"
# "Mother: You can buy those too if you want."
# "Father: So you want me to buy:"
# [print updated list]
# "Mother: Oh my bad, can you get rid of donuts"
# "Father: Fine, so you want me to buy:"
# [print updated list]
# "Mother: Yes, now off you go"

shopping_list = ['apple', 'banana', 'crabs', 'donuts', 'eggplant']
print('Mother: Dear, I want you to buy these now!', shopping_list)
print("Father: How about some chocolate?")
print("Mother: You can buy those too if you want.")
shopping_list.append("chocalate")
print("Father: So you want me to buy:", shopping_list)
print("Mother: Oh my bad, can you get rid of donuts")
del shopping_list[3]
print("Father: Fine, so you want me to buy:", shopping_list)
print("Mother: Yes, now off you go")
