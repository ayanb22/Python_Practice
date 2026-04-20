def reverse_number(n):
    if n < 0:
        raise ValueError("Invalid - Negative Number")
    power = len(str(n)) - 1
    reverse = 0
    if n == 0:
        return reverse
    reverse =  (n % 10)
    return reverse * 10 **power +  reverse_number(n // 10)

try:
    number = int(input("Enter the number : "))
    result = reverse_number(number)
    if number == result:
        print("This is a palindrome number")
    else:
        print("This is not a palindrome number")
except ValueError as error:
    print(error)