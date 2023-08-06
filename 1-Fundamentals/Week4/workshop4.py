class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
#        user_input = input("Change the name of the user: ")
        self.name = name

    def change_pin(self, pin):
#        user_input = input("Change the pin of the user: ")
        self.pin = pin

    def change_password(self, password):
#        user_input = input("Change the password of the user: ")
        self.password = password

""" account1 = User("Bob", "1234", "password")
print(account1.name, account1.pin, account1.password)
account1.change_password("Hello")
account1.change_name("Clifford")
account1.change_pin("2662")
print(account1.name, account1.pin, account1.password) """

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has a balance of",self.balance)

    def withdraw(self, with_amt):
        self.balance -= with_amt
#        user_input = input(float("Put in amount to withdraw: "))
#        self.balance = self.balance - user_input

    def deposit(self, dep_amt):
        self.balance += dep_amt
#        user_input = float(input("Put in amount to deposit: "))
#        self.balance = self.balance + user_input

    def transfer_money(self, user, trans_amt):
        print("You are transferring", trans_amt, "to", user.name)
        print("Authentication required")
        while True:
            user_input = input("Type in "+ self.name + " Pin: ")
            if user_input == self.pin:
                print("Pin approved, Transfer authorized.")
                print("Transferring", trans_amt, "to", user.name)
                break
            else:
                print("Incorrect Pin")
        user.balance += trans_amt
        self.balance -= trans_amt
        print("")

    def request_money(self, user, req_amt):
        print(self.name,"is requesting ", req_amt, "from", user.name)
        print("Authentication required.")
        while True:
            user_input = input("Type in " + self.name + "'s Pin: ")
            if user_input == self.pin:
                user_input1 = input("Type in " + self.name + "'s password: ")
                if user_input1 == self.password:
                    print("Request Approved")
                    break
                else:
                    print("Incorrect Password, Transaction canceled.")
                    return
            else:
                print("Incorrect Pin")
        user.balance -= req_amt
        self.balance += req_amt
        print(self.name, " has sent $",req_amt,"to",user.name)
        print("")


bankaccount1 = BankUser("Clifford", "2662", "Anna")
bankaccount2 = BankUser("Anna", "3256", "Clifford")
#print(bankaccount1.name, bankaccount1.pin, bankaccount1.password, bankaccount1.balance)
bankaccount2.deposit(5000)
bankaccount2.show_balance()
bankaccount1.show_balance()
bankaccount2.transfer_money(bankaccount1, 500) 
bankaccount2.show_balance()
bankaccount1.show_balance()
bankaccount1.request_money(bankaccount2, 2000)
bankaccount1.show_balance()
bankaccount2.show_balance()