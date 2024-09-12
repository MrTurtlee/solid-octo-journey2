previous = 1
seconds = 0
hundred = 100
odd = 1
total_age = 0
ages = [14,14,13,22,75,6,8]


# for x in ages:
#     total_age = total_age + x

# total_age = 100 - total_age
# print(total_age)


# for x in ages:
#     if x % 2 ==1:
#         odd = odd * x
# print(odd)


# for x in ages:
#     if x % 2 == 0:
#         hundred = hundred + x
#     elif x % 2 != 0:
#         hundred = hundred - x
# print(hundred)


# for x in ages:
#     seconds += 1
#     if seconds % 2 == 1:
#         total_age = total_age + x
# print(total_age)


for x in ages:
    total_age = total_age * previous * 2
    previous = x
print(total_age)