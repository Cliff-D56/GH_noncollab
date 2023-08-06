from donations_pkg.homepage import show_homepage, show_donations
from donations_pkg.user import login, register, donate
database = {"admin":"password123"}
donations = []
authorized_user = ""




while(True):
    show_homepage()
    user_input = input("Choose an option: ")
    if user_input == "1":
        print("Enter Username and Password")
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = login(database,username,password)
    elif user_input == "2":
        print("Enter Username and Password")
        username = input("Username: ")
        password = input("Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[authorized_user] = password
    elif user_input == "3":
        if authorized_user == "":
            print("You must be logged in to donate.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif user_input == "4":
        show_donations(donations)
    elif user_input == "5":
        print("Goodbye!")
        break
    elif user_input == "6":
        print(database.keys())

