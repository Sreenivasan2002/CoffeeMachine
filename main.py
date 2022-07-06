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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient(order_incrediants):
    print(order_incrediants)
    for items in order_incrediants:
        if order_incrediants[items] > resources[items]:
            print("Sorry there is not enough water")
            return False
        return True

def process_coins(drink,choice):
    global profit
    print("Incert coins:")
    quarters=float(input("Quarters $"))
    dimes = float(input("Dimes $"))
    nickles = float(input("Nickles $"))
    pennies = float(input("Pennies $"))
    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(f"Amount paid: ${total}")
    price = drink["cost"]
    print(f"cost for the drink {price}")
    if total < price:
        print("Sorry that's not enough money. Money refunded")
        coffee_machine()

    else:
        balance =round(total - price,3)
        print(f"Balance: ${balance}")
        print(f"Here is your {choice}.Enjoy!")
        profit =profit+ price




def coffee_machine():
    is_on = True
    while is_on:
        choice=input("What would you like? (espresso/latte/cappuccino):")
        if choice=="off":
            is_on = False
        elif choice=="report":
            print(f"Water: {resources['water']}ml ")
            print(f"Milk: {resources['milk']}ml ")
            print(f"Coffee: {resources['coffee']}ml ")
            print(f"Money: {profit}")
        else:
            drink=MENU[choice]
            is_sufficient(drink["ingredients"])
            process_coins(drink,choice)
coffee_machine()

