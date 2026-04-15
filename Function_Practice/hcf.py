def hcf(a, b):
    c = abs(a)
    d = abs(b)

    highest_common_factor = 0
    if c == 0 and d != 0:
        highest_common_factor = d
        return highest_common_factor
    elif d == 0 and c != 0:
        highest_common_factor = c
        return highest_common_factor
    elif c == 0 and d == 0:
        highest_common_factor = 0
        return highest_common_factor

    m = min(c, d)

    for i in range(m, 0, -1):
        if(c % i == 0 and d % i == 0):
            highest_common_factor = i
            break

    return highest_common_factor

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

highest_common_factor = hcf(a,b)
if(highest_common_factor < 1):
    print(f"The highest common factor of {a} and {b} is : Undefined")
else:
    print(f"The highest common factor of {a} and {b} is : {highest_common_factor}")
