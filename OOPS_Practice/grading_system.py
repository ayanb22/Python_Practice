class Grade():
    @staticmethod
    def college():
        print("Welcome to ABC College...")

    def __init__(self, name, sub_marks):
        self.name = name
        self.sub_marks = sub_marks


    def average(self):
        total = sum(self.sub_marks)
        average = round(total / len(self.sub_marks))
        print(f"Your Average is : {average}")
        return average
    
    def remarks(self):
        average = self.average()
        if average > 80:
            remarks = "A"
        elif average > 70:
            remarks = "B"
        elif average > 60:
            remarks = "C"
        elif average > 40:
            remarks = "D"
        else:
            remarks = "Fail"
        print(f"Your Remarks is : {remarks}") 
    
name = input("Enter Your Name : ")
count = int(input("How many subjects you have : "))
subject_marks = []
i = 1
while i <= count:
    marks = int(input("Enter your marks : "))
    subject_marks.append(marks)
    i += 1
s1 = Grade(name, subject_marks)
s1.college()
s1.average()
s1.remarks()

    

