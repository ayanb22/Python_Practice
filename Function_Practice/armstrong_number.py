def armstrong_number(num):
    number = abs(num)
    m = len(str(number))
    
    actual_number = number
    armstrong = 0
    while number > 0:
        remainder = number % 10
        armstrong = (remainder **m) + armstrong
        number = number // 10

    return actual_number == armstrong

number_input = int(input("Enter the number : "))
if armstrong_number(number_input):
    print("This is a armstrong number")
else:
    print("This is not an armstrong number")


