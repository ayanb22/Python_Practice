class Bank():
    @staticmethod
    def bank_name():
        print("Welcome to ABC Bank")
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit (self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Rs.", amount, "was debited")


    def credit (self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")

    
    def check_balance(self):
        print("Your current balance is : ", self.balance)  

c1 = Bank(50000, 785465)
c1.bank_name()
debit = int(input("Enter the amount you want to debit : "))
c1.debit(debit)
credit = int(input("Enter the amount you want to credit : "))
c1.credit(credit)
c1.check_balance()