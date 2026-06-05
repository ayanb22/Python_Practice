class HotelBooking:
    def __init__(self, name, room_type, days):
        self.name = name
        self.room_type = room_type
        self.days = days

    def room_charge(self):
        days = self.days
        room_type = self.room_type
        room_type = room_type.lower()
        if room_type == "standard":
            charge = 1000 * days
        elif room_type == "deluxe":
            charge = 2500 * days
        elif room_type == "suite":
            charge = 3500 * days
        
        return charge
    
    def final_discount(self):
        days = self.days
        charge = self.room_charge()
        if days >= 20:
            discount = round(0.18 * charge)
        elif days >= 10:
            discount = round(0.12 * charge)
        elif days >= 5:
            discount = round(0.07 * charge)
        else:
            discount = 0 
        
        return discount
    
    def final_bill(self):
        discount = self.final_discount()
        charge = self.room_charge()
        return (charge - discount)
    
    @staticmethod
    def hotel_name():
        print("Thanks for visiting ABC hotel......")
    

name = input("Enter your name: ")

while True:
    room_type = input("Enter the type of room you want: ")
    room_type = room_type.lower()
    if room_type == "standard" or room_type == "deluxe" or room_type == "suite":
        break
    else:
        print("Thats an invalid room type.....Try Again")

days = int(input("How many days you will stay in the hotel: "))

customer = HotelBooking(name, room_type, days)
print(f"Customer: {customer.name}")
print(f"Room Type: {customer.room_type}")
print(f"Days: {customer.days}")
print()
print(f"Room Charge: ₹{customer.room_charge()}")
print(f"Discount: ₹{customer.final_discount()}")
print(f"Final Bill: ₹{customer.final_bill()}")
customer.hotel_name()




