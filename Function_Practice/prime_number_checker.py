def prime_number(n= int(input("Enter the number : "))):
    not_prime = False

    for i in range(2, n):
        if(n % i == 0):
            not_prime = True
            break
    if not_prime:
        print("Not Prime Number")
    else:
        print("Prime Number")


prime_number()