def armstrong_number(n):
    m = len(n)
    num = int(n)
    actual_number = num
    armstrong = 0
    while num > 0:
        remainder = num % 10
        armstrong = (remainder **m) + armstrong
        num = num // 10
    
    return actual_number == armstrong

number = input("Enter the number : ")
if armstrong_number(number):
    print("This is a armstrong number")
else:
    print("This is not an armstrong number")


