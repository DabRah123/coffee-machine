import asciiart
print(asciiart.ascii_art)
menu = {
    "espresso": {
        "small": {
            "ingredients": {
                "water": 30, 
                "coffee": 10,
            },
            "cost": 100,
        },
        "medium": {
            "ingredients": {
                "water": 50, 
                "coffee": 18,
            },
            "cost": 150,
        },
        "large": {
            "ingredients": {
                "water": 70, 
                "coffee": 25,
            },
            "cost": 200,
        },
    },
    "latte": {
        "small": {
            "ingredients": {
                "water": 150, 
                "milk": 100, 
                "coffee": 20,
            },
            "cost": 200,
        },
        "medium": {
            "ingredients": {
                "water": 200, 
                "milk": 150, 
                "coffee": 24,
            },
            "cost": 250,
        },
        "large": {
            "ingredients": {
                "water": 250, 
                "milk": 200, 
                "coffee": 30,
            },
            "cost": 300,
        },
    },
    "cappuccino": {
        "small": {
            "ingredients": {
                "water": 200, 
                "milk": 80, 
                "coffee": 20,
            },
            "cost": 300,
        },
        "medium": {
            "ingredients": {
                "water": 250, 
                "milk": 100, 
                "coffee": 24,
            },
            "cost": 350,
        },
        "large": {
            "ingredients": {
                "water": 300, 
                "milk": 150, 
                "coffee": 30,
            },
            "cost": 400,
        },
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 200,
}
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}!")
            return False
    return True

def coins():
    print("Please insert coins")
    total = int(input("How many ₹10 notes? ")) * 10
    total += int(input("How many ₹50 notes? ")) * 50
    total += int(input("How many ₹100 notes? ")) * 100
    total += int(input("How many ₹200 notes? ")) * 200
    total += int(input("How many ₹500 notes? ")) * 500
    return total

def is_transaction_successful(money_received, cost_of_drink):
    if money_received >= cost_of_drink:
        global profit
        change = round(money_received - cost_of_drink, 2)
        print(f"Here is ₹{change} in change.")
        profit += cost_of_drink
        return True
    else:
        print("Sorry, you don't have enough money :(")
        return False

def make_coffee(drink_name, size, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {size} {drink_name}. Enjoy!")

machine_on = True
while machine_on:
    print("\nAvailable Drinks:")
    for drink, sizes in menu.items():
        print(f" - {drink.title()}: Small ₹{sizes['small']['cost']}, Medium ₹{sizes['medium']['cost']}, Large ₹{sizes['large']['cost']}")

    user_choice = input("\nWhat would you like to have? (Espresso/Latte/Cappuccino or 'report' to view resources, 'off' to exit): ").lower()

    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} gm")
        print(f"Profit: ₹{profit}")
    elif user_choice in menu:
        size = input("Choose a size (small/medium/large): ").lower()
        if size in menu[user_choice]:
            drink = menu[user_choice][size]
            if is_resource_sufficient(drink["ingredients"]):
                payment = coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(user_choice, size, drink["ingredients"])
        else:
            print("Invalid size. Please enter small, medium, or large.")
    else:
        print("Please enter a correct option.")
