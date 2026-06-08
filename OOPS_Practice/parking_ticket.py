class ParkingTicket:
    @staticmethod
    def parking_name():
        print("Welcome to ABC Parking Plaza....")
    
    def __init__(self, name, vehicle_type, parking_hour):
        self.name = name
        self.vehicle_type = vehicle_type
        self.parking_hour = parking_hour

    def parking_charge(self):
        vehicle_type = self.vehicle_type
        vehicle_type = vehicle_type.lower()
        parking_hour = self.parking_hour 
        if vehicle_type == "bike":
            rate = 20 * parking_hour
        elif vehicle_type == "car":
            rate = 50 * parking_hour
        elif vehicle_type == "bus":
            rate = 100 * parking_hour
        return rate
    
    def discount(self):
        parking_hour = self.parking_hour 
        charge = self.parking_charge()
        if parking_hour > 10:
            discount_available = round(0.15 * charge)
        elif parking_hour > 5:
            discount_available = round(0.05 * charge)
        else:
            discount_available = 0

        return discount_available
    
    def final_amount(self):
        charge = self.parking_charge()
        discount = self.discount()
        final_price = charge - discount
        return final_price
    


name = input("Enter your name : ")
while True:
    vehicle_type = input("Enter your vehicle type : ")
    vehicle_type = vehicle_type.lower()
    if vehicle_type == "bike" or vehicle_type == "car" or vehicle_type == "bus":
        break
    else:
        print("That is an invalid input")

parking_hour = int(input("Enter the time you used the parking plaza : "))

customer = ParkingTicket(name, vehicle_type, parking_hour)
customer.parking_name()
print("--------------------------")
print(f"Owner : {customer.name}")
print(f"Vehicle : {customer.vehicle_type}")
print(f"Hours : {customer.parking_hour}")
print()
print(f"Parking Charge : ₹{customer.parking_charge()}")
print(f"Discount : {customer.discount()}")
print(f"Final Amount : {customer.final_amount()}")
