number = (input("Enter the number : "))
n = int(number)
original_number = int(n)
sum_of_digits = 0

while n > 0:
    remainder = n % 10
    sum_of_digits = (remainder **len(number)) + sum_of_digits
    n = n // 10

if(original_number == sum_of_digits):
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")