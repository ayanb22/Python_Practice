def lcm(a, b):
    c = abs(a)
    d = abs(b)

    least_common_multiple = 0

    if c == 0 and d == 0:
        return 0
    elif c == 0 or d == 0:
        least_common_multiple = 0
        return least_common_multiple
    
    m = min(c,d)
    
    for i in range(m, 0, -1):
        if(c % i == 0 and d % i == 0):
            hcf = i
            break

    least_common_multiple = (c * d) // hcf

    return least_common_multiple

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

least_common_factorial = lcm(a,b)
if(a == 0 and b == 0):
    print("The least common multiple is : Undefined")
else:
    print(f"The least common multiple of {a} and {b} is : {least_common_factorial}")
