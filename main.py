from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "owner":
        password = input("Enter the password:") == "Saravanan"
        attempt = 5
        ran_out = False
        while not ran_out:
            if password == "Saravanan" or attempt == 0:
                ran_out = True
                break
            password = input("Enter the correct password:")
            attempt -= 1
        if attempt == 0:
            print("You're out of attempts.")
        if password == "Saravanan" and input("What you want to do:") == "take_money" :
            money_machine.take_money()
    elif choice == "fill":
        coffee_maker.fill()
    else:
        drink = menu.find_drink(choice.title())
        if drink:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
