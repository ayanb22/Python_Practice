def perfect_number(n):
    actual_number = n
    sum_of_divisors = 0

    if n < 0 :
        return False

    for i in range(1, n):
        if(n % i == 0):
            sum_of_divisors = sum_of_divisors + i
    
    return sum_of_divisors == actual_number

number = int(input("Enter the number : "))
if perfect_number(number):
    print("This is a perfect number")
else:
    print("This is not a perfect number")