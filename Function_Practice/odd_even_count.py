def odd_even_count(n):
    num = abs(n)
    even_count = 0
    odd_count = 0
    even_digit = []
    odd_digit = []
    if num == 0:
        return 1, [0], 0, []
    

    while num > 0:
        remainder = num % 10
        if(remainder % 2 == 0):
            even_count += 1
            even_digit.append(remainder)
        else:
            odd_count += 1
            odd_digit.append(remainder)
        num = num // 10

    even_digit.reverse()
    odd_digit.reverse()
    
    return even_count, even_digit, odd_count, odd_digit


number = int(input("Enter the number : "))
even_count, even_digit, odd_count, odd_digit = odd_even_count(number)
    

print(f"The number of even digits : {even_count}")
print(f"The even digits are : {even_digit}")
print(f"The number of odd digits : {odd_count}")
print(f"The odd digits are: {odd_digit}")