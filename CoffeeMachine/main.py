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
money =0


def latte():
    global resources,money
    if resources["water"]>=200 and resources["milk"]>=150 and resources["coffee"]>=24:
     print("Please insert coins")
     q = float(int(input("How many quarters?:")) * 0.25)
     d = float(int(input("How many dimes?:"))    * 0.10)
     n = float(int(input("How many nickles?:"))  * 0.05)
     p = float(int(input("How many pennies?:"))  * 0.01)
     sum = q + d + n + p
     if sum > 2.5:
         money = money + 2.5
         print(f"Here is ${sum-2.5} in change")
         print("This is your Latte, Enjoy!!")
         resources["water"] = resources["water"] - 200
         resources["milk"] = resources["milk"] - 150
         resources["coffee"] = resources["coffee"] - 24
     else:
      print(("Sorry that's not enough money. Money refunded."))
    else:
        print("Sorry there is not enough ingredients")

def espresso():
    global resources,money
    if resources["water"]>=50 and resources["coffee"]>=18:
     print("Please insert coins")
     q = float(int(input("How many quarters?:")) * 0.25)
     d = float(int(input("How many dimes?:"))    * 0.10)
     n = float(int(input("How many nickles?:"))  * 0.05)
     p = float(int(input("How many pennies?:"))  * 0.01)
     sum = q + d + n + p
     if sum > 1.5:
         money = money + 1.5
         print(f"Here is ${sum-2.5} in change")
         print("This is your espresso, Enjoy!!")
         resources["water"] = resources["water"] - 50
         resources["coffee"] = resources["coffee"] - 18
     else:
         print(("Sorry that's not enough money. Money refunded."))
    else:
        print("Sorry there is not enough ingredients")

def cappuccino():
    global resources,money
    if resources["water"]>=250 and resources["milk"]>=100 and resources["coffee"]>=24:
     print("Please insert coins")
     q = float(int(input("How many quarters?:")) * 0.25)
     d = float(int(input("How many dimes?:"))    * 0.10)
     n = float(int(input("How many nickles?:"))  * 0.05)
     p = float(int(input("How many pennies?:"))  * 0.01)
     sum = q + d + n + p
     if sum > 3.0:
         money = money + 3.0
         print(f"Here is ${sum-3.0} in change")
         print("This is your Cappuccino, Enjoy!!")
         resources["water"] = resources["water"] - 250
         resources["milk"] = resources["milk"] - 100
         resources["coffee"] = resources["coffee"] - 24
     else:
      print(("Sorry that's not enough money. Money refunded."))
    else:
        print("Sorry there is not enough ingredients")

while True:
 req = input("What would you like? (espresso/latte/cappuccino)  ")
 if req == "report":
    print(resources)
    print(f"Money: ${money}")
 elif req == "latte":
    latte()
 elif req == "espresso":
    espresso()
 else:
     cappuccino()



