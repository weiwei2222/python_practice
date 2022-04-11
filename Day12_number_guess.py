import random
from random import randint
from Day12_art import logo

level_easy = 10
level_hard = 5


def check_answer_number(user_answer, answer_number, my_turns):
    if user_answer > answer_number:
        print("Too high!")
        return my_turns - 1
    elif user_answer < answer_number:
        print("Too low!")
        return my_turns - 1


def game_level(user_level):
    if user_level == "easy":
        return level_easy
    if user_level == "hard":
        return level_hard


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
    answer = random.randint(1, 101)
    # print(answer)
    leve_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = game_level(leve_choice)
    game_continue = True
    while game_continue:
        user_guess = int(input("Please make a guess:"))
        turns = check_answer_number(user_guess, answer, turns)
        if user_guess == answer:
            print(f"You got it! The answer was {answer}")
            game_continue = False
        elif turns == 0:
            print("You've run out of guesses, you lose.")
            game_continue = False
        elif user_guess != answer:
            print(f"You have {turns} attempts remaining to guess the number.")


game()
