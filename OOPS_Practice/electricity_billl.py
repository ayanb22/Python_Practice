class ElectricityBill:
    def __init__(self, name, units_consumed):
        self.name = name
        self.units_consumed = units_consumed

    def bill_calculation(self):
        units_consumed = self.units_consumed
        if units_consumed <= 100:
            bill = units_consumed * 5
        elif units_consumed <= 300:
            bill = units_consumed * 7
        else:
            bill = units_consumed * 10
        return bill
    
    def surcharge_calculation(self):
        bill = self.bill_calculation()
        if bill <= 2000:
            surcharge = bill * 0.05
        elif bill <= 5000:
            surcharge = bill * 0.1
        else:
            surcharge = bill * 0.2
        return surcharge



name = input("Enter The user Name : ")
unit = int(input("Enter The Units Consumed : "))
print()
customer = ElectricityBill(name, unit)
print(f"customer : {customer.name}")
print(f"Units : {customer.units_consumed}")
print()
print(f"Bill Amount : {customer.bill_calculation()}")
print(f"Surcharge : {customer.surcharge_calculation()}")
print()
total = customer.bill_calculation() + customer.surcharge_calculation()
print(f"Total Payable Bill : {total}")






