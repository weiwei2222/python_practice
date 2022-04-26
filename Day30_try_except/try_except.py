# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["aaaa"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is error that I made up.")

# weight = float(input("input your weight (kg)："))
# height = float(input("input your height (m)："))
#
# if height > 3:
#     raise ValueError("Haman height should be not over 3 meters.")
#
# bmi = weight / (height) ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(f"{fruit} pie")


make_pie(4)
