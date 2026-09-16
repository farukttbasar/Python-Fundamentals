MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0,
    }
}

profit = 0
current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100 
}

def print_reports(current_resources, current_profit):
    units = {"water": "ml", "milk": "ml", "coffee": "gr"}
    for item, amount in current_resources.items():
        unit = units.get(item, "unit")
        print(f"{item.capitalize()}: {amount}{unit}")
    print(f"Money: ${current_profit:.2f}")


def is_resoruce_sufficent(order_ingredients, current_resources):
    for item, amount in order_ingredients.items():
        if amount > current_resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")
        return True
    else:
        print("Sorry, that is not enough money. Money refunded.")
        return False


def insert_coins():
    while True:
        try:
            money = float(input("Please insert money (e.g. 2.5, 5): $"))
            if money <= 0:
                print("Please enter a positive amount!")
                continue
            return round(money, 2)
        except ValueError:
            print("Please enter a valid amount!")


def make_coffee(drink_name, order_ingredients, current_resources):
    for item, amount in order_ingredients.items():
        current_resources[item] -= amount
    print(f"Here is your {drink_name}. Enjoy!")


while True:
    print("""
----- COFFEE MACHINE -----
1-) Order a coffee
2-) Show the resources
3-) Exit
""")

    while True:
        try:
            choice = int(input("What would you like to do? "))
            if choice not in [1, 2, 3]:
                print("Please enter an option from the given menu!")
            else:
                break
        except ValueError:
            print("Please enter a number!")

    match choice:
        case 1:
            while True:
                coffee_choice = input("What would you like to drink? (espresso, latte, cappucino): ").strip().lower()
                if coffee_choice not in ["espresso", "latte", "cappucino"]:
                    print("Please choose one of them (espresso, latte, cappucino)!")
                else:
                    break

            coffee = MENU[coffee_choice]
            print(f"{coffee_choice.title()} is ${coffee['cost']:.2f}.")

            if is_resoruce_sufficent(coffee["ingredients"], current_resources):
                payment = insert_coins()
                if is_transaction_successful(payment, coffee["cost"]):
                    profit += coffee["cost"]
                    make_coffee(coffee_choice, coffee["ingredients"], current_resources)

        case 2:
            print_reports(current_resources, profit)

        case 3:
            print("Exiting system. Goodbye!")
            break
            
            
