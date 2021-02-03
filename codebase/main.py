"""
The main file that executes the game.
Date: 02-02-2021
"""
from utils import *
from player import *
import random

def main():
    player = intro()

    #load a scenario
    c_list = loadChoices("choices.txt")
    random.shuffle(c_list)
    
    for i in range(len(c_list)):
        print("\n%s" %c_list[i].getScenario())
        opts = ["Yes", "No", "Quit"]
        pick = menu(opts)
        if pick == 1:
            player.addChoice(c_list[i].getTag(), True) #add choice to player data
            if c_list[i].getPTag() in player.choices: #check if prereq exists
                player.setExp(c_list[i].getExpAlt()) #update player expenditure
                player.setCarbonFoot(c_list[i].getCarbonFootAlt()) #update player carbon footprint
                print("\n%s" %c_list[i].getConsqAlt())
            else:
                player.setExp(c_list[i].getExp()) #update player expenditure
                player.setCarbonFoot(c_list[i].getCarbonFoot()) #update player carbon footprint
                print("\n%s" %c_list[i].getConsq())
            print("\nYour resulting Expenditure:", player.getExp())
            print("Your resulting Carbon Footprint Score:", player.getCarbonFoot(),"\n")
        elif pick == 2:
            print("Nothing chosen.")
        else:
            print("Thx for playing!")
            print("\nYour final Expenditure:", player.getExp())
            print("Your final Carbon Footprint Score:", player.getCarbonFoot(),"\n")
            break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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


main()