class ATM:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        while True:
            if amount > 0:
                
                self.balance += amount
                print(f"Amount Rs.{amount} is credited")
                break
            else:
                print("Try again that is an invalid amount....")
                amount = int(input("Enter the amount you want to deposit : "))
    
    def withdraw(self, amount):
        balance = self.balance
        self.amount = amount
        while True:
            if amount > balance:
                print("Try again that is an invalid amount....")
                amount = int(input("Enter the amount you want to withdraw : "))
            else:
                self.balance -= amount               
                print(f"Amount Rs.{amount} is debited")
                break
        

    def checkbalance(self):
        print(f"Your Current Balance is {self.balance}")


name = input("Enter your name : ")
balance = int(input("Enter your current balance : "))
customer = ATM(name, balance)
while True:
    response = int(input("Type what you want to do 1 for 'Check balance', 2 for 'Withdraw' and 3 for deposit :"))
    if response == 1:
        customer.checkbalance()
        break
    elif response == 2:
        amount = int(input("Enter the amount you want to withdraw : "))
        customer.withdraw(amount)
        customer.checkbalance()
        break
    elif response == 3:
        amount = int(input("Enter the amount you want to deposit : "))
        customer.deposit(amount)
        customer.checkbalance()
        break
    else:
        print("Invalid input try again....")

        


