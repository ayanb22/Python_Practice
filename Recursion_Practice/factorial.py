def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)
    

try:
    number = int(input("Enter the number : "))
    result = factorial(number)
    print(f"The factorial of {number} : {result}")
except ValueError as error:
    print(error)
