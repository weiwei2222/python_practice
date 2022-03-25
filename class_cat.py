# 学习class

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def display_name(self):
        print("my cat name is " + self.name)

    def display_age(self):
        print("my cat age is " + str(self.age))

    def display_color(self):
        print("my cat color is " + self.color)

    def cat_play(self):
        print(f"cat {self.name} is very happy now.")


Cat_a = Cat("tony", 3, "orange")
Cat_a.display_name()
Cat_a.display_age()
Cat_a.display_color()
Cat_a.cat_play()


def week_pay(hour_pay, hour):
    salary = hour_pay * hour
    return salary


Emplyee_salary_Mike = week_pay(20.29, 40)
print(f"your weekpay is {Emplyee_salary_Mike:.2f}")
