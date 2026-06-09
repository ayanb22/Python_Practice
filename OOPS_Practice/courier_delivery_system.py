class CourierDelivery:
    @staticmethod
    def service_name():
        print("Welcome to ABC Courier Service....")
    
    def __init__(self, name, package_weight, delivery_type):
        self.name = name
        self.package_weight = package_weight
        self.delivery_type = delivery_type

    def delivery_charge(self):
        package_weight = self.package_weight
        delivery_type = self.delivery_type
        delivery_type = delivery_type.lower()
        if delivery_type == "standard":
            charge = package_weight * 50
        elif delivery_type == "express":
            charge = package_weight * 100
        elif delivery_type == "sameday":
            charge = package_weight * 150
        
        return charge
    
    def extra_charge(self):
        package_weight = self.package_weight
        if package_weight > 10:
            charge = 200
        elif package_weight > 5:
            charge = 100
        else:
            charge = 0
        
        return charge

    def final_charge(self):
        delivery_charge = self.delivery_charge()
        extra_charge = self.extra_charge()
        final_fee = delivery_charge + extra_charge
        return final_fee
    
name = input("Enter Your Name : ")
weight = int(input("Enter Your Package Weight : "))
while True:
    delivery_type = input("Enter Your Delivery Type : ")
    delivery_type = delivery_type.lower()
    if delivery_type == "standard" or delivery_type == "express" or delivery_type == "sameday":
        break
    else:
        print("That is an Invalid Input.....Try Again")

customer = CourierDelivery(name, weight, delivery_type)
print()
customer.service_name()
print(f"Name : {customer.name}")
print(f"Weight : {customer.package_weight} kg")
print(f"Delivery Type : {customer.delivery_type}")
print()
print(f"Delivery Charge : ₹{customer.delivery_charge()}")
print(f"Extra Charge : ₹{customer.extra_charge()}")
print(f"Final Charge : ₹{customer.final_charge()}")


