"""
Utilities for game
Date: 02-02-2021
"""

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

def getInt(prompt):
    """get a positive integer"""
    n = input(prompt)
    if n.isdigit():
        return int(n)
    else:
        return getInt(prompt)