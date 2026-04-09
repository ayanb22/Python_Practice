def palindrome_number(n = int(input("Enter the number : "))):
    actual_value = n
    reverse_value = 0

    while n > 0:
        remainder = n % 10
        reverse_value = (reverse_value * 10) + remainder
        n = n // 10
    
    if(reverse_value == actual_value):
        print("The number is a Palindrome Number")
    else:
        print("The number is not a Palindrome Number")

palindrome_number()