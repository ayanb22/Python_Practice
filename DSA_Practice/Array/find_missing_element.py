def missing_element(n):
    input_list = []
    seen_list = []
    i = 1
    
    while i < n:
        while True:
            number = int(input("Enter the number you want to add in the list : "))
            if number <= 0:
                print("It is an invalid input")  
            elif number > n:
                print("It is an invalid input")      
            else:
                if number not in seen_list:
                    input_list.append(number)
                    seen_list.append(number)
                    break
                else:
                    print("No Duplicate number is allowed")
        i += 1
    
    total = (n * (n+1))/2
    total = total // 10
    sum_input = sum(input_list)

    missing_element = total - sum_input

    return missing_element
    

number = int(input("the maximum number in the sequence : "))
print(missing_element(number))