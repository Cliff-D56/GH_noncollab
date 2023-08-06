import random

def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    while tries != 0:
        print("You have ",tries," remaining.")
        guess = int(input("Guess your number: "))
        if guess == random_number:
            print("You've guessed correctly")
            return
        elif guess > random_number:
            print("Guess Lower")
        elif guess < random_number:
            print("Guess Higher")
        tries -= 1
        if tries == 0:
            print("You've failed to guess correct number.")


def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    while tries != 0:
        for guess in range(start, stop):
            if tries == 0:
                print("Program failed to guess correct number.")
                break
            print("Program has",tries,"remaining.")
            print("Program is guessing.....",guess)
            if guess == random_number:
                print("Program guessed correctly")
                return
            elif guess > random_number:
                print("Guess Lower")
            elif guess < random_number:
                print("Guess Higher")
            tries -= 1

def guess_random_num_binary(tries,start,stop):
    random_number = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop 
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = (range(start, stop))[pivot]
        if tries == 0:
            print("Program failed to guess correct number.")
            break
        print("Program has",tries,"remaining.")
        print("Program is guessing.....",pivot_value)
        if pivot_value == random_number:
            print("Program guessed correctly")
            return pivot
        elif pivot_value > random_number:
            print("Guess Lower")
            upper_bound = pivot - 1
        elif pivot_value < random_number:
            print("Guess Higher")
            lower_bound = pivot + 1
        tries -= 1

guess_random_num_binary(10, 0, 10000)