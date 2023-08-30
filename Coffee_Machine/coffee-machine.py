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
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_suffecient(order_ingredients):
    """Checks Whether the resource are available to make item (returns True / False)"""
    for item in order_ingredients:
      if order_ingredients[item] >= resources[item]:
       print(f"Sorry Insuffecient Resource - {item}")
       return False
    return True

def process_coins():
    """Returns The Total Calculated Based On The Coins Inserted"""
    print("Please Insert Coins!")
    total = int(input("How Many Quarters?: ")) * 0.25
    total += int(input("How Many Dimes?: ")) * 0.2
    total += int(input("How Many Nickels?: ")) * 0.05
    total += int(input("How Many Pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your Drink, Enjoy!  ")
def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment accepted or False if Insuffecient Money"""
    if money_received >= drink_cost:
        change = round(money_received -drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is your change ${change} ")
        return True
    else:
        print("Sorry Not Enough Money, Your Money is refunded! ")
        return False

is_on = True

while is_on:
  choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
  if choice == "off":
      is_on = False
  elif choice == "report":
      print(f"Water: {resources['water']}ml")
      print(f"Milk: {resources['milk']}ml")
      print(f"Coffee: {resources['coffee']}g")
      print(f"Profit: ${profit}")
  else:
      drink = MENU[choice]
      if is_resource_suffecient((drink['ingredients'])):
          payment = process_coins()
          if is_transaction_successful(payment, drink['cost']):
              make_coffee(drink, drink['ingredients'])


