def fibonacci (n = int(input("Enter the range of fibonacci series : "))):
    first_digit = 0
    second_digit = 1
    fibonacci_Series = []
    while first_digit < n:
        fibonacci_Series.append(first_digit)
        next_digit = first_digit + second_digit
        first_digit = second_digit
        second_digit = next_digit
        
    print(fibonacci_Series)

fibonacci()