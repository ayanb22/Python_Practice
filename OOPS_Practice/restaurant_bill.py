class RestaurantBill:
    @staticmethod
    def restaurant_name():
        print("Welcome to ABC Restaurant....")

    def __init__(self, name, bill):
        self.name = name
        self.bill = bill
    
    def service_charge(self):
        bill = self.bill
        if bill >= 2000:
            service = round(bill * 0.1)
        elif bill >= 500:
            service = round(bill * 0.05)
        else:
            service = 0
        return service
        
    def final_bill(self):
        bill = self.bill
        service_charge = self.service_charge()
        bill = bill + service_charge 
        return bill
    
name = input("Enter Your name : ")
bill = int(input("Enter Your Bill Amount : "))

customer = RestaurantBill(name, bill)
customer.restaurant_name()

print(f"Name : {customer.name}")
print(f"Bill : ₹{customer.bill}")
print()
print(f"Service Charge : ₹{customer.service_charge()}")
print(f"Final Bill : ₹{customer.final_bill()}")
    