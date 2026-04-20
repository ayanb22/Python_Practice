def reverse_number(n):
    n = abs(n) 
    power = len(str(n)) - 1
    reverse = 0
    if n == 0:
        return reverse
    reverse =  (n % 10)
    return reverse * 10 **power +  reverse_number(n // 10)

number = int(input("Enter the number : "))
result = reverse_number(number)
print(result)
