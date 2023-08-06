def login(database,username,password):
#The first half checks if the username is in the keys sections and the 
#second half the password is checking the database value is in the database
    if username in database.keys() and password == database[username]:
        print("Welcome")
        print("Logged in as: " + username)
        return username
#    elif username in database.keys() and password not in database[username]:
#        print("Wrong Password")
#    elif username not in database.keys() and password in database[username]:
#        print("Wrong Username")
    else:
        print("Failure to login")
        print("Register New User if needed")
        return ""

def register(database,username):
    if username in database.keys():
        print("Username already registered")
        return ""
    else:
        print("Username:", username, "has been registered")
        return username

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    if donation_amt == "":
        print("Invalid amount")
        return
    else:
      float(donation_amt)
      donation = username + " Donated $" + donation_amt
      print("Thank you for donation!")
      return donation


