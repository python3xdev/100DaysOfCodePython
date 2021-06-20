from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_machine.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_machine.make_coffee(drink)
