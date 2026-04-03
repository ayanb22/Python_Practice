n = int(input("Enter the number : "))
original_number = n
sum_of_factorial = 0

while n > 0:
    remainder = n % 10
    i = 1
    factorial_of_digit = 1
    while i <= remainder:
        factorial_of_digit = i * factorial_of_digit
        i += 1
    sum_of_factorial = factorial_of_digit + sum_of_factorial
    n = n // 10

if(sum_of_factorial == original_number):
    print("This is a strong number")
else:
    print("This is not a strong number")