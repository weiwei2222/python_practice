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
        if self.category == "American Shorthair":
            return self.cat_game[0]
        elif self.category == "British Shorthair":
            return self.cat_game[1]
        elif self.category == "Persian cat":
            return self.cat_game[2]
        elif self.category == "Devon Rex":
            return self.cat_game[3]

    def feed_cat(self):
        if self.age <= 1:
            return self.food_band[0]
        elif 1 < self.age < 10:
            return self.food_band[1]
        elif self.age > 10:
            return self.food_band[2]


user_cat_name = input("Please type your cat name:")
user_cat_category = int(input("Please type cat category.\n"
                              "1,American Shorthair  2,British Shorthair  3,Persian cat  4,Devon Rex\n"))-1
user_cat_age = int(input("Please type your cat age.\n"))
user_cat = Cat(user_cat_name, Cat.cat_category[user_cat_category], user_cat_age)
user_cat.display_cat()


user_feed = int(input(f"Your cat {user_cat.name} is hungry now."
                      f"Please feed food.\n"
                      f"1,small cat food  2,adult cat food  3,old cat food\n")) - 1
cat_game_continue = True
while cat_game_continue:
    if Cat.food_band[user_feed] == user_cat.feed_cat():
        print(f"Your cat 😽 {user_cat.name} is full now. ")
        cat_game_continue = False
    else:
        cat_game_continue = True
        user_feed = int(input(f"Your cat 😾 {user_cat.name} doesn't like {Cat.food_band[user_feed]}.\n"
                              f"Please feed food.\n"
                              f"1,small cat food  2,adult cat food  3,old cat food\n")) - 1


user_play = int(input(f"Your cat {user_cat.name} wants to play now."
                      f"Please choice.\n"
                      f"1,running with you  2,play toll with you  3,sleeping in your lap 4,hiding to you\n"))-1
cat_game_continue = True
while cat_game_continue:
    if Cat.cat_game[user_play] == user_cat.play_cat():
        print(f"Your cat 😽 {user_cat.name} is happy now. ")
        cat_game_continue = False
    else:
        cat_game_continue = True
        user_play = int(input(f"Your cat 😾 {user_cat.name} doesn't like {Cat.cat_game[user_play]}.\n"
                              f"Please choice.\n"
                              f"1,running with you  2,play toll with you  3,sleeping in your lap 4,hiding to you\n"))-1