print("""Menu:
1,Salad  $5.99
2,Soup  $6.95
3,Pizza  $10.59
4,Burger  $8.66
""")
menu = {"Salad": 5.99, "Soup": 6.95, "Pizza": 10.59, "Burger": 8.66, "Beer": 7.99}


order = []
while len(order) == 0 or input("Input “finish” when you finish your order.") != "finish":
    dishes = ""
    while dishes not in menu.keys():
        try:
            dishes = input("Please input the dishes name!")
        except ValueError:
            print("You only can input the dishes name!")

    quantity = 0
    while quantity not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        try:
            quantity = int(input("""Please input your dishes quantity. The max quantity is 10!"""))
        except ValueError:
            print("You only can input the quantity number!")
    order.append((dishes, quantity))
print("I finish order!")


def total(order):
    total_price = 0
    for (dishes, quantity) in order:
        total_price = total_price + menu[dishes] * quantity
    return total_price


print(f"The total price is {total(order):.2f}")
