from cgitb import reset

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
    "money": 0
}



def print_resources():
    for resource in resources:
        if resource == "money":
            print(f"Money: ${resources[resource]:.2f}")
        else:
            print(f"{resource.capitalize()}: {resources[resource]}")

def check_resources(beverage):
    for resource in resources:
        if resource in MENU[beverage]["ingredients"]:
            if MENU[beverage]["ingredients"][resource] > resources[resource]:
                print(f"Sorry, we don't have enough {resource}.")
                return False

    print(f"We have enough resources for {beverage}.")
    return True


def process_payment(beverage):
    print(f"Please insert ${MENU[beverage]['cost']:.2f} for a {beverage}.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_payment = quarters*.25 + dimes*.10 + nickels*.05 + pennies*.01
    if total_payment < MENU[beverage]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change_total = total_payment - MENU[beverage]["cost"]
        print(f"Here's ${change_total:.2f} in change")
        resources["money"] += MENU[beverage]["cost"]
        return True


def make_drink(beverage):
    for resource in resources:
        if resource in MENU[beverage]["ingredients"]:
            resources[resource] -= MENU[beverage]["ingredients"][resource]






serving_drinks = True
while serving_drinks:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink.lower() == 'off':
        serving_drinks = False
        continue
    elif drink.lower() == 'report':
        print_resources()
        continue
    elif drink.lower() in MENU:

        enough_resources = check_resources(drink.lower())
        if enough_resources:

            enough_money = process_payment(drink.lower())
            if enough_money:

                make_drink(drink.lower())
                print(f"Here's your {drink.lower()}. Enjoy!")
    else:
        print("Sorry, that's not on the menu.")
