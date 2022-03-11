# Find the max sum of sub array
# 			Ex L = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]
# 			Output = 49

num_list = [5, 4, 7, -2, 5, 0, 6, 9, 15, -3]

sum_of_all_value = sum(num_list)

for i in range(1,len(num_list)+1):
    for j in range(len(num_list)):
        if j+i <= len(num_list):
            if sum(num_list[j:j+i]) >= sum_of_all_value:
                sum_of_all_value = sum(num_list[j:j+i])
        else:
            break
            
print(sum_of_all_value)