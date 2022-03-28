import random

# sum_even = 0
# for number in range(2, 101, 2):
#     sum_even = sum_even + number
#     # sum_even += number
# print(sum_even)


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# my_numbers = random.choice(numbers)
# print(my_numbers)
my_numbers = ""
for char in range(0, 5):
    my_numbers += random.choice(numbers)
print(my_numbers)