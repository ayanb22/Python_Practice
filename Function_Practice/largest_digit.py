def largest_number(n):
    num = abs(n)
    largest_digit = num % 10
    while num >0:
        remainder = num % 10
        if(remainder > largest_digit):
            largest_digit = remainder
        num = num // 10
    
    return(largest_digit)

number = int(input("Enter the number : "))
print(f"The largest digit is : {largest_number(number)}") 
            
    