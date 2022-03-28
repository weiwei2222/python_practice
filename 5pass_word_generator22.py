import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input("How many symbols would you like?\n"))
user_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for get_random in range(1, user_letters+1):
    # letter_random = random.choice(letters)
    # password = password + letter_random
    password_list += random.choice(letters)

for get_random in range(1, user_symbols+1):
    password_list += random.choice(symbols)

for get_random in range(1, user_numbers+1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(password_list)

user_password = ""
for password_char in password_list:
    user_password = user_password + password_char
    # user_password += password_char

print(f"Your password is {user_password}")