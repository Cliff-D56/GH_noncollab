from banking_pkg.account import deposit, logout, show_balance, withdraw


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("=== Automated Teller Machine ===")
name = input("Enter Your name to register: ")
pin =input("Enter PIN: ")
balance = 0
print("Your account name is: ", name)
print("Your current balance is: $" + str(balance))

while True: 
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid Login Credentials")
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif option == "3":
        balance = withdraw(balance)
        show_balance(balance)
    elif option == "4":
        logout(name)
        break
    else:
        print("Invalid option")
