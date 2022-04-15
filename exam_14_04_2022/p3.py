num_list = [-2,1,-3,4,-1,2,1,-5,4]

sum_of_all_value = sum(num_list)

for i in range(1,len(num_list)+1):
    for j in range(len(num_list)):
        if j+i <= len(num_list):
            if sum(num_list[j:j+i]) >= sum_of_all_value:
                sum_of_all_value = sum(num_list[j:j+i])
        else:
            break
            
print(sum_of_all_value)