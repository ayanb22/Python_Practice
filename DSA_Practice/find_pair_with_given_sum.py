def find_pair_of_given_sum(n):
        input_list = []
        output_list = []
        i = 1
        while i <= n:
            number = int(input("Enter the number you want to add in the list : "))
            input_list.append(number)
            i += 1

        target_sum = int(input("Enter the target sum : "))


        for index_one in range(len(input_list)):
            for index_two in range(index_one+1, len(input_list)):
                if input_list[index_one] + input_list[index_two] == target_sum:                       
                    output_list.append(input_list[index_one])
                    output_list.append(input_list[index_two])

            

        return output_list

number = int(input("Enter the number of elements in the list : "))
print(find_pair_of_given_sum(number))
