class GymMembership:
    @staticmethod
    def gym_name():
        print("Welcome to ABC GYM...")
    
    def __init__(self, name, membership, monthly_fee):
        self.name = name
        self.membership = membership
        self.monthly_fee = monthly_fee
    
    def discount_value(self):
        fee = self.monthly_fee
        membership = (self.membership)
        membership = membership.lower()
        if membership == "platinum":
            discount = fee * 0.2
            final_fee = fee - discount
        elif membership == "gold":
            discount = fee * 0.1
            final_fee = fee - discount
        elif membership == "basic":
            discount = fee * 0
            final_fee = fee - discount
        else:
            discount=  "Invalid Input"
            final_fee = fee
        
        return discount, final_fee
    

name = input("Enter Your Name : ")
membership = input("Enter Your Membership Details : ")
monthly_fee = int(input("Enter Your Monthly Fee : "))

member = GymMembership(name, membership, monthly_fee)
member.gym_name()
print(f"Name: {member.name}")
print(f"Membership: {member.membership}")
print(f"Monthly Fee: {member.monthly_fee}")
print()
discount, final_fee = member.discount_value()
print(f"Discount: {discount}")
print(f"Final Fee: {final_fee}")








