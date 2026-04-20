def power_function(n, x):
    if n == 0 and x < 0:
        raise ValueError("undefined")
    x = abs(x)

    if x == 0:
        return 1

    return n * power_function(n ,x-1)

try :
    base = int(input("Enter the base : "))
    power = int(input("Enter the power : "))
    result = power_function(base, power)
    if power < 0:
        result = 1 / result
    print(f"The result is : {result}") 
except ValueError as e:
    print(e)
    





