print("Welcome to Dungeons and Dragons")
# Declaring Variables Stage

# Characters
wizard = "Wizard"
human = "Human"
elf = "Elf"

# Health
wizard_health = 70
human_health = 150
elf_health = 100
dragon_health = 300

# Damage
wizard_damage = 150
human_damage = 20
elf_damage = 100
dragon_damage = 50

# My stats
my_health = 0
my_damage = 0

user_input = 0
my_character = 0
# While loops will always loop if true.
while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "Wizard" and user_input != "Human" and user_input != "Elf":
    print("")
    print("Character Selection")
    print("1) Wizard")
    print("2) Human")
    print("3) Elf")
    print("")
    user_input = input("Choose your character: ")
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "Wizard" and user_input != "Human" and user_input != "Elf":
        print("Unknown Choice, Try again")
print("Choice Confirmed")
print("")

# Character Stats Binding Code
if user_input == "1":
    my_character = wizard
    my_health = wizard_health
    my_damage = wizard_damage
elif user_input == "2":
    my_character = human
    my_health = human_health
    my_damage = human_damage
elif user_input == "3":
    my_character = elf
    my_health = elf_health
    my_damage = elf_damage
elif user_input == "Wizard":
    my_character = wizard
    my_health = wizard_health
    my_damage = wizard_damage
elif user_input == "Human":
    my_character = human
    my_health = human_health
    my_damage = human_damage
elif user_input == "Elf":
    my_character = elf
    my_health = elf_health
    my_damage = elf_damage

print("Your Character is:", my_character)
print("Your Health is:", my_health)
print("Your Attack is:", my_damage)
print("")

# Dragon Battle Code
while dragon_health > 0:
    dragon_health = dragon_health - my_damage
    print("Your attack did", my_damage, "To Dragon")
    print("Dragon has", dragon_health, "Health Remaining")
    print("")
    if dragon_health > 0:
        my_health = my_health - dragon_damage
        print("The dragon has struck back, you've taken", dragon_damage, "damage")
        print("Your health is now", my_health)
        print("")
        if my_health <= 0:
            print("You've ran out of heatlh, Game Over.")
            break
    else:
        print("The Dragon has been defeated")
        print("")
        break
