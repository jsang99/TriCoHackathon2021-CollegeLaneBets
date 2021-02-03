"""
The main file that executes the game.
Date: 02-02-2021
"""

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
def menu(opts):
    """display menu, given a list, make sure we get valid menu input"""
    for i in range(len(opts)):
        print("%2d. %s" % (i+1,opts[i]))
    min = 1
    max = len(opts)
    while True:
        pick = getInt("Your choice? ")
        if pick >= min and pick <= max:
            return pick
        else:
            print("please enter a valid choice!!!")
#-----------------------------------------------------------------   

def getInt(prompt):
    """get a positive integer"""
    n = input(prompt)
    if n.isdigit():
        return int(n)
    else:
        return getInt(prompt)

main()