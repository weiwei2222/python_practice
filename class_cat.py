# 学习class

class Cat:
    food_band = ["small cat food", "adult cat food", "old cat food"]

    def __init__(self, user_cat_name, age, color):
        self.name = user_cat_name
        self.age = age
        self.color = color

    def display_cat(self, max_age, other_cat):
        print(f"my cat name is {self.name}. he is {self.age} and he is {self.color}. "
              f"he will be {max_age} in the future." 
              f"he like to play with {other_cat.name}")

    def feed_cat(self):
        if self.age <= 1:
            print(f"{self.name} feed cat food is {self.food_band[0]}.")
        elif 1 < self.age < 10:
            print(f"{self.name} feed cat food is {self.food_band[1]}.")
        elif self.age > 10:
            print(f"{self.name} feed cat food is {self.food_band[2]}.")


cats = [
    Cat(user_cat_name="Tony", age=4, color="orange"),
    Cat("Felix", 1, "black and white"),
    Cat("Garfield", 40, "ugly"),
]

best_cat = Cat("Bob", 15, "gray")

for cat in cats:
    cat.display_cat(10, best_cat)
    cat.feed_cat()
# cat_a = Cat("Tony", 4, "orange")
# cat2 = Cat("Felix", 1, "black and white")
#
# cat_a.display_cat(10, cat2)
# cat2.display_cat(9, cat_a)
#
# cat_a.feed_cat()
# cat2.feed_cat()



def week_pay(hour_pay, hour):
    salary = hour_pay * hour
    return salary


Emplyee_salary_Mike = week_pay(20.29, 40)
print(f"your weekpay is {Emplyee_salary_Mike:.2f}")
