class MobileRecharge:
    @staticmethod
    def centre_name():
        print("Welcome to ABC Recharge centre..")
    
    def __init__(self, name, mobile_number, recharge_value):
        self.name = name
        self.mobile_number = mobile_number
        self.recharge_value = recharge_value

    def validity(self):
        recharge = self.recharge_value
        if recharge >= 499:
            day = 84 
        elif recharge >= 199:
            day = 28
        else:
            day = 14

        return day
    
    def bonus(self):
        recharge = self.recharge_value
        if recharge >= 999:
            bonus_data = 3
        elif recharge >= 499:
            bonus_data = 1
        elif recharge >= 199:
            bonus_data = 0.5 
        else:
            bonus_data = 0
        return bonus_data
    

name = input("Enter Your Name : ")
recharge = int(input("Enter your Recharge Value : "))
mobile_number = input("Enter your Number : ")
print()
print("------------------------")


customer = MobileRecharge(name,mobile_number, recharge)
customer.centre_name()
print(f"Customer: {customer.name}")
print(f"Mobile Number {customer.mobile_number}")
print(f"Recharge: ₹{customer.recharge_value}")
print()
print(f"Validity: {customer.validity()} days")
print(f"Bonus Data: {customer.bonus()} GB")






            