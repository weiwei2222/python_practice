# my_list = [1, 2, 3, 4]
# for my_list in range(4, 0, -1):
#     print(my_list)


numbers = [1, 2, 3, 4, 5, 6, 7]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

new_list = [n + 1 for n in numbers]
print(new_list)

range_list = [n*2 for n in range(5, 15)]
print(range_list)

names = ["Mike", "Beth", "Lily", "Freddie", "Caroline"]
short_names = [name for name in names if len(name) <= 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)