"""
The main file that executes the game.
Date: 02-02-2021
"""
from utils import *
from player import *

def main():
    player = intro()

    #load a scenario
    c_list = loadChoices("choices.txt")
    print("\n", c_list[0].getScenario())

    pick = input("Y/N: ")
    if pick == "Y":
        player.setExp(c_list[0].getExp())
        player.setCarbonFoot(c_list[0].getCarbonFoot())
        print("\n", c_list[0].getConsq())
        print("\nYour resulting Expenditure:", player.getExp())
        print("Your resulting Carbon Footprint Score:", player.getCarbonFoot(),"\n")
    
    
    #print("\nDay", count, "is finished.")
    #print("Your carbon footprint is now:", cfoot)
#-----------------------------------------------------------------
"""
intro
prints the welcome message
"""
def intro():
    print("Welcome to Carbon President!")
    print("\nGame Description.\n")
    
    name = input("Enter your name: ")
    country_name = input("Enter your country's name: ")

    player = Player(name, country_name)
    return player

#-----------------------------------------------------------------
"""
daily_menu
Handles the choices a player makes for a given day.

def daily_menu():
    transport_opts = ["bus", "bike", "horse", "car"]
    food_opts = ["waffle", "burger", "salad", "coffee", "water"]
    waste_opts = ["recycle", "compost", "trash"]
    energy_opts = ["solar", "Room Light", "Charge Phone", ]

    #Ask about transport
    print("\nMake your TRANSPORT choice for the day.")
    choice = menu(transport_opts)
    print("You chose:", transport_opts[choice-1])

    #Ask about food
    print("\nMake your FOOD choice for the day.")
    choice = menu(food_opts)
    print("You chose:", food_opts[choice-1])

    #Ask about waste
    print("\nMake your WASTE choice for the day.")
    choice = menu(waste_opts)
    print("You chose:", waste_opts[choice-1])

    #Ask about energy
    print("\nMake your ENERGY choice for the day.")
    choice = menu(energy_opts)
    print("You chose:", energy_opts[choice-1])
"""    
#-----------------------------------------------------------------   


main()