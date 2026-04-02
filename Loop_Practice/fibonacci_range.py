n = int(input("Enter the largest number : "))
fibonacci = []

first_number = 0
second_number = 1

while first_number < n:
        fibonacci.append(first_number)
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
    
print(f"The fibonacci series : {fibonacci}")
