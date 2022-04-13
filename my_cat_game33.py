import random


class Cat:
    cat_category = ["American Shorthair", "British Shorthair", "Persian cat", "Devon Rex"]
    cat_game = ["running with you", "play toll with you", "sleeping in your lap", "hiding to you"]
    food_band = ["small cat food", "adult cat food", "old cat food"]

    def __init__(self, name, category, age):
        self.name = name
        self.category = category
        self.age = age

    def display_cat(self):
        print(f"Congratulations, you just adopted a lovely cat!\n"
              f"your cat 😺 name is {self.name}. he is {self.category} cat and he is {self.age} years old.")

    def play_cat(self):
        self = random.choice(Cat.cat_game)
        return self

    def feed_cat(self):
        if self.age <= 1:
            return self.food_band[0]
        elif 1 < self.age < 10:
            return self.food_band[1]
        elif self.age > 10:
            return self.food_band[2]


class CatGame:

    def __init__(self, cat):
        self.cat = cat

    @classmethod
    def ask_for_cat(cls):
        user_cat_name = input("Please type your cat name:")
        user_cat_category = int(input("Please type cat category.\n"
                                      "1,American Shorthair  2,British Shorthair  3,Persian cat  4,Devon Rex\n")) - 1
        user_cat_age = int(input("Please type your cat age.\n"))
        user_cat = Cat(user_cat_name, Cat.cat_category[user_cat_category], user_cat_age)
        user_cat.display_cat()
        return cls(cat=user_cat)

    def play_feed_cat_game(self):
        message = f"Your cat {self.cat.name} is hungry now."
        cat_game_continue = True
        while cat_game_continue:
            user_feed = int(input(f"{message}\n"
                                  f"Please feed food.\n"
                                  f"1,small cat food  2,adult cat food  3,old cat food\n")) - 1
            if Cat.food_band[user_feed] == self.cat.feed_cat():
                print(f"Your cat 😽 {self.cat.name} is full now. ")
                cat_game_continue = False
            else:
                message = f"Your cat 😾 {self.cat.name} doesn't like {Cat.food_band[user_feed]}.\n"

    def play_play_cat_game(self):
        message = f"Your cat {self.cat.name} wants to play now."
        cat_game_continue = True
        while cat_game_continue:
            user_play = int(input(f"{message}\n"
                                  f"Please choice.\n"
                                  f"1,running with you  2,play toll with you  3,sleeping in your lap 4,hiding to you\n")) - 1
            if Cat.cat_game[user_play] == self.cat.play_cat():
                print(f"Your cat 😽 {self.cat.name} is happy now. ")
                cat_game_continue = False
            else:
                print(f"your cat like {self.cat.play_cat()}")
                message = f"Your cat 😾 {self.cat.name} doesn't like {Cat.cat_game[user_play]}.\n"


game1 = CatGame.ask_for_cat()
game2 = CatGame.ask_for_cat()

game1.play_play_cat_game()
game2.play_play_cat_game()
