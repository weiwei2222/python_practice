import random
from Day7_hangman_words import logo, word_list, stages
from replit import clear

print(logo)
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
# for letter in chosen_word:
#     display += "_"
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}!")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])