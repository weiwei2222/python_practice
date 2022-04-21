# def add(*numbers):
#     n_sum = 0
#     for n in numbers:
#         n_sum += n
#     return n_sum
#
#
# print(add(1, 2, 3, 4, 5))


def calculate(w, **kwargs):
    print(kwargs)
    # for a, b in kwargs.items():
    #     print(a)
    #     print(b)
    w += kwargs["add"]
    w *= kwargs["multiply"]
    print(w)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        # self.band = kwargs["make"]
        # self.model = kwargs["model"]
        self.band = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.color)