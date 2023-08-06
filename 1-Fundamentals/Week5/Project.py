from Game_setup_pkg.Game_menu import start_menu, game_menu, warrior_menu, mage_menu, rogue_menu
from Game_setup_pkg.Character_stats import Character, Mage, Rogue, Warrior, Boss1, Boss2, Boss3, FinalBoss
import sys



user_input = 0
print("Welcome to Dungeons and Dragons")
game_menu()
while True:
    user_input = input()
    if user_input == "1":
        break
    elif user_input == "2":
        print("Are you sure you wish to Quit, Quitting will cause program to terminate")
        user_input = input(""" 1. Yes
                               2. No
                  """)
        if user_input == "1":
            sys.exit()
        else:
            break
    else:
        print("Unknown Choice, Try again")
user_input = 0
while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "Warrior" and user_input != "Mage" and user_input != "Rogue":
    start_menu()
    user_input = input("Choose your character: ")
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "Warrior" and user_input != "Mage" and user_input != "Rogue":
        print("Unknown Choice, Try again")
print("Choice Confirmed")
print("")

if user_input == "1":
    my_character = Warrior
elif user_input == "2":
    my_character = Mage
elif user_input == "3":
    my_character = Rogue
elif user_input == "Warrior":
    my_character = Warrior
elif user_input == "Mage":
    my_character = Mage
elif user_input == "Rogue":
    my_character = Rogue

print("Your Character is:", my_character.name)
print("Your Health is:", my_character.hp)
print("Your Attack is:", my_character.damage)
print("Your Defense is:", my_character.defense)
if my_character == Warrior:
    warrior_menu() 
elif my_character == Mage:
    mage_menu()
elif my_character ==  Rogue:
    rogue_menu()
print("")
print("Starting 1st Boss Battle...")
while Boss1.hp > 0:
    if my_character.hp < 0:
        print("Game Over!!")
        sys.exit()
    turn_counter = 0
    perk_turn_counter = 0
    if my_character == Warrior:
        warrior_menu()
    elif my_character == Mage:
        mage_menu()
    elif my_character ==  Rogue:
        rogue_menu()
    turn_counter += 1
    print("The Boss's Health is: ",Boss1.hp)
    print("Your Health is: ",my_character.hp)
    print("Turn:",turn_counter) 
    user_input = input("Choose your skill: ")
    if user_input == "1":
        if my_character == Warrior:
            Boss1.hp -= (my_character.damage - Boss1.defense)
        elif my_character == Mage:
            Boss1.hp -= (my_character.damage - Boss1.defense)
        elif my_character == Rogue:
            Boss1.hp -= (my_character.damage - Boss1.defense)
    elif user_input == "2":
        if my_character == Warrior:
            while perk_turn_counter < 2:
                my_character.defense *= 2 
                perk_turn_counter += 1
                if perk_turn_counter == 2:
                    perk_turn_counter = 0
                    my_character.defense = 200
                break
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.defense *= 1.5
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.defense = 100
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                Boss1.hp -= (my_character.damage / 6)
                Boss1.hp -= (Boss1.hp / 20)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
    elif user_input == "3":
        if my_character == Warrior:
            while perk_turn_counter != 4:
                Boss1.hp -= (my_character.damage / 4)
                Boss1.defense -= (Boss1.defense / 5)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 4:
                perk_turn_counter = 0
                Boss1.defense = 200
        elif my_character == Mage:
            my_character.hp += 800
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                Boss1.hp -= (my_character.damage / 8)
                Boss1.damage / 1.75 
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
                Boss1.damage = 400
    elif user_input == "4":
        if my_character == Warrior:
            my_character.hp += 600
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.damage *= 1.75
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.damage = 1200
        elif my_character == Rogue:
            Boss1.hp -= ((my_character.damage / 5) - Boss1.defense)
            Rogue.hp += ((my_character.damage / 5) - Boss1.defense)
    my_character.hp -= (Boss1.damage - my_character.defense)
    print("Boss strikes back, you've taken ", Boss1.damage - my_character.defense)
    print("Your Character is:", my_character.name)
    print("Your Health is:", my_character.hp)
    print("Your Attack is:", my_character.damage)
    print("Your Defense is:", my_character.defense)
print("Starting 2nd Boss Battle...")
while Boss2.hp > 0:
    if my_character.hp < 0:
        print("Game Over!!")
        sys.exit()
    turn_counter = 0
    perk_turn_counter = 0
    if my_character == Warrior:
        warrior_menu() 
    elif my_character == Mage:
        mage_menu()
    elif my_character ==  Rogue:
        rogue_menu()
    turn_counter += 1
    print("The Boss's Health is: ",Boss2.hp)
    print("Your Health is: ",my_character.hp)
    print("Turn:",turn_counter) 
    user_input = input("Choose your skill: ")
    if user_input == "1":
        if my_character == Warrior:
            Boss2.hp -= (my_character.damage - Boss2.defense)
        elif my_character == Mage:
            Boss2.hp -= (my_character.damage - Boss2.defense)
        elif my_character == Rogue:
            Boss2.hp -= (my_character.damage - Boss2.defense)
    elif user_input == "2":
        if my_character == Warrior:
            while perk_turn_counter < 2:
                my_character.defense *= 2 
                perk_turn_counter += 1
                if perk_turn_counter == 2:
                    perk_turn_counter = 0
                    my_character.defense = 200
                break
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.defense *= 1.5
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.defense = 100
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                Boss2.hp -= (my_character.damage / 6)
                Boss2.hp -= (Boss2.hp / 20)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
    elif user_input == "3":
        if my_character == Warrior:
            while perk_turn_counter != 4:
                Boss2.hp -= (my_character.damage / 4)
                Boss2.defense -= (Boss2.defense / 5)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 4:
                perk_turn_counter = 0
                Boss2.defense = 200
        elif my_character == Mage:
            my_character.hp += 800
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                Boss2.hp -= (my_character.damage / 8)
                Boss2.damage / 1.75 
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
                Boss2.damage = 400
    elif user_input == "4":
        if my_character == Warrior:
            my_character.hp += 600
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.damage *= 1.75
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.damage = 1200
        elif my_character == Rogue:
            Boss2.hp -= ((my_character.damage / 5) - Boss2.defense)
            Rogue.hp += ((my_character.damage / 5) - Boss2.defense)
    my_character.hp -= (Boss2.damage - my_character.defense)
    print("Boss strikes back, you've taken ", Boss2.damage - my_character.defense)
    print("Your Character is:", my_character.name)
    print("Your Health is:", my_character.hp)
    print("Your Attack is:", my_character.damage)
    print("Your Defense is:", my_character.defense)
print("Starting 3rd Boss Battle...")
while Boss3.hp > 0:
    if my_character.hp < 0:
        print("Game Over!!")
        sys.exit()
    turn_counter = 0
    perk_turn_counter = 0
    if my_character == Warrior:
        warrior_menu() 
    elif my_character == Mage:
        mage_menu()
    elif my_character ==  Rogue:
        rogue_menu()
    turn_counter += 1
    print("The Boss's Health is: ",Boss3.hp)
    print("Your Health is: ",my_character.hp)
    print("Turn:",turn_counter) 
    user_input = input("Choose your skill: ")
    if user_input == "1":
        if my_character == Warrior:
            Boss3.hp -= (my_character.damage - Boss3.defense)
        elif my_character == Mage:
            Boss3.hp -= (my_character.damage - Boss3.defense)
        elif my_character == Rogue:
            Boss3.hp -= (my_character.damage - Boss3.defense)
    elif user_input == "2":
        if my_character == Warrior:
            while perk_turn_counter < 2:
                my_character.defense *= 2 
                perk_turn_counter += 1
                if perk_turn_counter == 2:
                    perk_turn_counter = 0
                    my_character.defense = 200
                break
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.defense *= 1.5
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.defense = 100
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                Boss3.hp -= (my_character.damage / 6)
                Boss3.hp -= (Boss3.hp / 20)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
    elif user_input == "3":
        if my_character == Warrior:
            while perk_turn_counter != 4:
                Boss3.hp -= (my_character.damage / 4)
                Boss3.defense -= (Boss3.defense / 5)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 4:
                perk_turn_counter = 0
                Boss3.defense = 200
        elif my_character == Mage:
            my_character.hp += 800
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                Boss3.hp -= (my_character.damage / 8)
                Boss3.damage / 1.75 
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
                Boss3.damage = 400
    elif user_input == "4":
        if my_character == Warrior:
            my_character.hp += 600
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.damage *= 1.75
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.damage = 1200
        elif my_character == Rogue:
            Boss3.hp -= ((my_character.damage / 5))
            Rogue.hp += ((my_character.damage / 2))
    my_character.hp -= (Boss3.damage - my_character.defense)
    print("Boss strikes back, you've taken ", Boss3.damage - my_character.defense)
    print("Your Character is:", my_character.name)
    print("Your Health is:", my_character.hp)
    print("Your Attack is:", my_character.damage)
    print("Your Defense is:", my_character.defense)
print("Starting Final Boss Battle...")
while FinalBoss.hp > 0:
    if my_character.hp < 0:
        print("Game Over!!")
        sys.exit()
    turn_counter = 0
    perk_turn_counter = 0
    if my_character == Warrior:
        warrior_menu() 
    elif my_character == Mage:
        mage_menu()
    elif my_character ==  Rogue:
        rogue_menu()
    turn_counter += 1
    print("The Boss's Health is: ",FinalBoss.hp)
    print("Your Health is: ",my_character.hp)
    print("Turn:",turn_counter) 
    user_input = input("Choose your skill: ")
    if user_input == "1":
        if my_character == Warrior:
            FinalBoss.hp -= (my_character.damage - FinalBoss.defense)
        elif my_character == Mage:
            FinalBoss.hp -= (my_character.damage - FinalBoss.defense)
        elif my_character == Rogue:
            FinalBoss.hp -= (my_character.damage - FinalBoss.defense)
    elif user_input == "2":
        if my_character == Warrior:
            while perk_turn_counter < 2:
                my_character.defense *= 2 
                perk_turn_counter += 1
                if perk_turn_counter == 2:
                    perk_turn_counter = 0
                    my_character.defense = 200
                break
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.defense *= 1.5
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.defense = 100
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                FinalBoss.hp -= (my_character.damage / 6)
                FinalBoss.hp -= (FinalBoss.hp / 20)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
    elif user_input == "3":
        if my_character == Warrior:
            while perk_turn_counter != 4:
                FinalBoss.hp -= (my_character.damage / 4)
                FinalBoss.defense -= (FinalBoss.defense / 5)
                perk_turn_counter += 1
                break
            if perk_turn_counter == 4:
                perk_turn_counter = 0
                FinalBoss.defense = 200
        elif my_character == Mage:
            my_character.hp += 800
        elif my_character == Rogue:
            while perk_turn_counter != 3:
                FinalBoss.hp -= (my_character.damage / 8)
                FinalBoss.damage / 1.75 
                perk_turn_counter += 1
                break
            if perk_turn_counter == 3:
                perk_turn_counter = 0
                FinalBoss.damage = 400
    elif user_input == "4":
        if my_character == Warrior:
            my_character.hp += 600
        elif my_character == Mage:
            while perk_turn_counter != 2:
                my_character.damage *= 1.75
                perk_turn_counter += 1
                break
            if perk_turn_counter == 2:
                perk_turn_counter = 0
                my_character.damage = 1200
        elif my_character == Rogue:
            FinalBoss.hp -= ((my_character.damage / 5) - FinalBoss.defense)
            Rogue.hp += ((my_character.damage / 5) - FinalBoss.defense)
    my_character.hp -= (FinalBoss.damage - my_character.defense)
    print("Boss strikes back, you've taken ", FinalBoss.damage - my_character.defense)
    print("Your Character is:", my_character.name)
    print("Your Health is:", my_character.hp)
    print("Your Attack is:", my_character.damage)
    print("Your Defense is:", my_character.defense)

print("Congrats You've defeated the boss rush!!!")