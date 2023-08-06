import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    print("Pick a card or Press 'Q' to Quit")
    user_input = input()
    if user_input == "Q":
        break
    else:
        random_choice = random.choice(diamonds)
        print(random_choice)
        hand.append(random_choice)
        diamonds.remove(random_choice)
        print("Your hand: ",hand)
        print("Remaining cards: ",diamonds)
if not diamonds:
    print("There are no more cards")