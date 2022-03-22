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


Cat_a = Cat("tony", 3, "orange")
Cat_a.display_name()
Cat_a.display_age()
Cat_a.display_color()


class Restaurant:
    def __init__(self, name, style, business_time):
        self.name = name
        self.style = style
        self.business_time = business_time

    def show_name(self):
        print("餐厅的名字是" + self.name)

    def show_style(self):
        print("餐厅的主营系是" + self.style)

    def show_business_time(self):
        print("餐厅在" + self.business_time)


Restaurant_duck = Restaurant("全聚德", "烤鸭", "营业中")
Restaurant_duck.show_name()
Restaurant_duck.show_style()
Restaurant_duck.show_business_time()
