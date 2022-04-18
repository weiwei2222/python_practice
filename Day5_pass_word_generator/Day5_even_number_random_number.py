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
for char in range(0, 3):
    char = random.choice(numbers)
    my_numbers = my_numbers + char
    # my_numbers += random.choice(numbers)
print(my_numbers)


numbers = ["Mike", "Mary", "Jack", "Rose"]
char1 = random.choice(numbers)
print(char1)