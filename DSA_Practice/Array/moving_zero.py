def move_zero(n):
    number_list = []
    final_list = []
    zero_count = 0
    i = 1
    while i <= n:
        number = int(input("Enter the number : "))
        number_list.append(number)
        i += 1

    for number in number_list:
        if number != 0:
            final_list.append(number)
        else:
            zero_count += 1

    for i in range(zero_count):
        final_list.append(0)

    return final_list



number = int(input("Enter the highest number of element in the list : "))
print(move_zero(number))