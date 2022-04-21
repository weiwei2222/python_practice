# new_list = [new_item for item in list]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [s*s for s in numbers]
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

with open("file1.txt") as file1:
    file_1_date = file1.readlines()

with open("file2.txt") as file2:
    file_2_date = file2.readlines()

result = [int(number) for number in file_1_date if number in file_2_date]

print(result)
