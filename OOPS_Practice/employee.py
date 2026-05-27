class Employee:
    @staticmethod
    def bank_name():
        print("Welcome to ABC Bank...")

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def bonus_salary(self):
        salary = self.salary
        if salary > 50000:
            bonus = salary * 0.2
        elif salary > 30000:
            bonus = salary * 0.1
        else:
            bonus = salary * 0.05

        return bonus

  
name = input("Enter your name : ")
salary = int(input("Enter your salary : "))

emp = Employee(name, salary)
emp.bank_name()
print(f"Name : {emp.name}")
print(f"Basic Salary : {emp.salary}")
bonus = emp.bonus_salary()
print(f"Bonus : {bonus}")
print(f"Final Salary : {round(emp.salary + bonus)}")

    