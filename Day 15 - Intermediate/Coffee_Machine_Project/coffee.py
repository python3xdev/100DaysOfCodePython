from data import MENU, resources


def calc_coins(coffee_choice):
    print(f"Coffee cost: ${MENU[coffee_choice]['cost']}")
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    change = total_coins - MENU[coffee_choice]['cost']
    print(f'Total Given: ${round(total_coins, 2)}')
    if change >= 0:
        print(f'Here is ${round(change, 2)} in change.')
        return True
    return False


def machine():
    while True:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_type == 'off':
            break
        elif coffee_type == 'report':
            print(f"""
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
""")
        elif coffee_type == 'espresso' and resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] > MENU['espresso']['ingredients']['coffee']:
            if calc_coins('espresso'):
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                print("Here is your espresso ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif coffee_type == 'latte' and resources['water'] >= MENU['latte']['ingredients']['water'] and resources['coffee'] > MENU['latte']['ingredients']['coffee'] and resources['milk'] > MENU['latte']['ingredients']['milk']:
            if calc_coins('latte'):
                resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
                print("Here is your latte ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif coffee_type == 'cappuccino' and resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['coffee'] > MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] > MENU['cappuccino']['ingredients']['milk']:
            if calc_coins('cappuccino'):
                resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
                print("Here is your cappuccino ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if resources['water'] >= MENU[coffee_type]['ingredients']['water']:
                print("Sorry there is not enough water.")
            elif resources['coffee'] > MENU[coffee_type]['ingredients']['coffee']:
                print("Sorry there is not enough coffee.")
            elif resources['milk'] > MENU[coffee_type]['ingredients']['milk']:
                print("Sorry there is not enough milk.")


machine()
