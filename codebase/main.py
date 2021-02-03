"""
The main file that executes the game.
Date: 02-02-2021
"""

from utils import *

def main():
    intro()
    cfoot = 0

    count = 0
    while count < 3: #simulates the one week runtime of the game
        daily_menu()
        count+=1
        print("\nDay", count, "is finished.")
        print("Your carbon footprint is now:", cfoot)
#-----------------------------------------------------------------
"""
intro
prints the welcome message
"""
def intro():
    print("Welcome to [gamename]!")

#-----------------------------------------------------------------
"""
daily_menu
Handles the choices a player makes for a given day.
"""
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
        
#-----------------------------------------------------------------   
"""
def userInputCheck(userChoice, availableChoices):
    """
    #This function returns true if the user selects a choice
    #that is available. If not, it returns false
    """

    for i in range(len(availableChoices)):
        if userChoice not in availableChoices:
            return False
    
    return True
"""
#-----------------------------------------------------------------

#create item/choice class

main()