def prime_number(n):
    prime_digit = []
    for i in range(2, n+1):
        not_prime = False
        for j in range(2, i):
            if(i % j == 0):
                not_prime = True
                break
        if not_prime == False:
            prime_digit.append(i)
    return prime_digit

number = int(input("Enter the highest number : "))
print(prime_number(number))           
         



