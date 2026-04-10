def factorial(n):
    counter = 1
    for i in range(n, 0, -1):
        counter = i * counter
    
    return counter

number = int(input("Enter the number : "))
result = factorial(number)

print(result)