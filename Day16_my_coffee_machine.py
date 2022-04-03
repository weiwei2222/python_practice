from Day16_menu import Menu, MenuItem
from Day16_coffee_maker import CoffeeMaker
from Day16_money_machine import MoneyMachine


my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()
is_on = True


while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like?{options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_machine.is_resource_sufficient(drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_machine.make_coffee(drink)