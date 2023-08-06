def show_balance(balance):
    print("Your Current Balance is: $" + str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return float(balance) + float(amount)

def withdraw(balance):
    withdraw = input("Enter amount to withdraw: ")
    if float(withdraw) < float(balance):
        return float(balance) - float(withdraw)
    else:
        print("Not enough funds.")

def logout(name):
    print("Goodbye " + name + "!")