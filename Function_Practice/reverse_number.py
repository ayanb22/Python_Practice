def reverse_number(n):
    reverse = 0

    while n > 0:
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = n // 10

    return(reverse)

number = int(input("Enter the number : "))
print(f"The reverse number is : {reverse_number(number)}")