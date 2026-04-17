def second_highest_digit(n):
    num = abs(n)
    highest = -1
    second_highest = -1    

    while num > 0:
        remainder = num % 10
        if highest < remainder:
            second_highest = highest
            highest = remainder            
        elif second_highest < remainder and highest != remainder:
            second_highest = remainder
        num = num // 10
    
    return second_highest

number = int(input("Enter the number : "))
result = second_highest_digit(number)

if result == -1:
    print("There is no 2nd highest number")
else:
    print(f"The second highest number is : {result}")