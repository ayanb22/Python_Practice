def largest_number(n):
    largest_digit = n % 10
    while n >0:
        remainder = n % 10
        if(remainder > largest_digit):
            largest_digit = remainder
        n = n // 10
    
    return(largest_digit)

number = int(input("Enter the number : "))
print(f"The largest digit is : {largest_number(number)}") 
            
    