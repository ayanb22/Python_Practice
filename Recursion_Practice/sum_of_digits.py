def sum_of_digits(n):

    n = abs(n)
    if n == 0:
        return 0

    return n % 10 +sum_of_digits(n // 10) 

number = int(input("Enter the number : "))
result = sum_of_digits(number)
print(f"The sum of digit is : {result}")