# TODO 1: print art
from art import coffee
from inventory import MENU, profit, resources

print(coffee)
# TODO 2: Prompt - use end to stop execution
should_continue = True


# TODO 3: print report


def report():
    return f"Water:{resources['water']}\nMilk:{resources['milk']}\nCoffee: {resources['coffee']} \nProfit:{profit} "


# TODO 4: Check resources sufficient
def resource_check(drink):
    w = MENU[drink]['ingredients']['water']
    c = MENU[drink]['ingredients']['coffee']

    if w > resources['water']:
        print("Sorry there is not enough Water.")
        return False

    if c > resources['coffee']:
        print("Sorry there is not enough coffee.")
        return False

    if drink == "latte" or drink == "cappuccino":
        m = MENU[drink]['ingredients']['milk']
        if m > resources['milk']:
            print("Sorry there is not enough Milk.")
            return False

    return True


# TODO 5: Check transaction successful
# TODO 7: Make coffee
def process_coins(drink):
    cost = MENU[drink]['cost']
    print("Please insert coins")
    five_rs = int(input("How many five rupees: "))
    ten_rs = int(input("How many ten rupees: "))
    fifty_rs = int(input("How many fifty rupees: "))
    hundred_rs = int(input("How many hundred rupees: "))
    calculation = 5 * five_rs + 10 * ten_rs + 50 * fifty_rs + 100 * hundred_rs
    if cost > calculation:
        print("Sorry that's not enough money refunded!")
        return False
    else:
        change_in_turn = calculation - cost
        print(f"Here is your change Rs.{change_in_turn}.\n Here is your {drink} ☕.")
        global profit
        profit += cost
        return True


# TODO 6: Update resource
def update_resource(drink):
    resources['water'] = resources['water'] - MENU[drink]['ingredients']['water']
    resources['coffee'] = resources['coffee'] - MENU[drink]['ingredients']['coffee']
    if drink != "espresso":
        resources['milk'] = resources['milk'] - MENU[drink]['ingredients']['milk']


while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_input == 'report':
        print(report())
    elif user_input == 'off':
        print("Session closed!")
        should_continue = False
    else:
        available = resource_check(user_input)

        if available:
            change = (process_coins(user_input))
            if change:
                update_resource(user_input)
