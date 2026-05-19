def count_target_frequency(n):
    input_list = []
    i = 1
    count = 0

    
    while i <= n:
        number = int(input("Enter the number you want to add in the list : "))
        input_list.append(number)
        i += 1
    
    user_input = int(input("Enter the target number : "))

    for number in input_list:
        if number == user_input:
            count += 1


    return count

number = int(input("Enter the number of elements will be in the list : "))
print(count_target_frequency(number))
