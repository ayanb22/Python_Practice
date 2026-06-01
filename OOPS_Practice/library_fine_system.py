class LibraryFine:
    def __init__(self, name, days_late, book_name):
        self.name = name
        self.days_late = days_late
        self.book_name = book_name

    def fine_calculation(self):
        days_late = self.days_late
        if days_late > 10:
            fine = 30 * days_late
        elif days_late >5:
            fine = 20 * days_late
        elif days_late > 0:
            fine = 10 * days_late
        else:
            fine = 0
        return fine
    
    def book_status(self):
        days_late = self.days_late
        if days_late > 0:
            print("Returned Late")
        else:
            print("Returned in Time")
        
    
    
name = input("Enter Your Name : ")
days_late = int(input("Enter how many days you are late : "))
book_name = input("Enter Book Name : ")

student = LibraryFine(name, days_late, book_name)
print(f"Name : {student.name}")
print(f"Book Nmae : {student.book_name}")
print(f"Days Late : {student.days_late}")
student.book_status()
print(f"Fine : {student.fine_calculation()}")
