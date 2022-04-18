from Day14_art import logo, vs
from Day14_game_data import data
import random
from replit import clear


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr}, from{account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    elif a_followers < b_followers:
        return user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")

    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    follower_account_a = account_a["follower_count"]
    follower_account_b = account_b["follower_count"]
    is_correct = check_answer(guess, follower_account_a, follower_account_b)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right!Current score:{score}")
    else:
        game_should_continue = False
        print(f"Sorry,that's wrong.Final score:{score}")
