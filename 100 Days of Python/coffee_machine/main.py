MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: check if coins provided is sufficient for the order
def payment_success(num_quarters, num_dimes, num_nickels, num_pennies):
    total_payment = (num_quarters * 0.25) + (num_dimes * 0.10) + (num_nickels * 0.05) + (num_pennies * 0.01)
    return round(total_payment - price, 2)


# TODO: Check resources are sufficient for the order
def resources_sufficient():
    for ingredient in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
            print(f"  Sorry there is not enough {ingredient}.")
            return False
        return True


# TODO: calculate how much resources are used
def resources_used(item_ordered):
    """given the name of a beverage, this function calculates how much resources are used and returns a tuple as the
    answer"""
    water_used = MENU[item_ordered]["ingredients"]["water"]
    if item_ordered == "milk":
        milk_used = MENU[item_ordered]["ingredients"]["milk"]
    else:
        milk_used = 0
    coffee_used = MENU[item_ordered]["ingredients"]["coffee"]
    return water_used, milk_used, coffee_used


# TODO: Print report of machine resources
def print_report():
    """prints a report of resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


machine_on = True
money = 0

while machine_on:

    # TODO: Prompt customer by asking what they want and figure out the cost
    order = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print_report()
        continue
    elif order == "off":
        break
    price = MENU[order]["cost"]

    if resources_sufficient():
        # TODO: process coins, give change back if customer overpaid
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    else:
        continue

    change = payment_success(num_quarters=quarters, num_dimes=dimes, num_nickels=nickels, num_pennies=pennies)

    if change >= 0:
        print(f"Here is ${change} in change")
        print(f"Here is your {order} ☕️. Enjoy!")

        # TODO: update resources
        index = 0
        for resource in resources:
            resources[resource] -= resources_used(order)[index]
            index += 1
        money += price

    else:
        print("Sorry that's not enough money. Money refunded.")
