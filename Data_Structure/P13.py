# Return the array which contains the elements which are greater than from its right side
# 	Sample = [5, 17, 2, 6, 3]
# 	Output = [17, 6, 3] 

num_list = [5, 17, 2, 6, 3]
final_lst = []


for i in range(len(num_list)):
    flag = False
    for j in range(i+1,len(num_list)):
        if num_list[i] > num_list[j]:
            flag = True
        else:
            flag = False
            break
    if flag:
        final_lst.append(num_list[i])
        
final_lst.append(num_list[len(num_list)-1])   
print(final_lst)
            
    
# def check_greater(value,starting_index,ending_index):
#     flag = False
#     if starting_index == ending_index:
#         return flag
#     elif value > num_list[starting_index]:
#         flag = True
#         print(value)
#         return check_greater(value,starting_index+1,ending_index)
#     elif value <= num_list[starting_index]:
#         flag = False
#         return flag    
    
    
# for i in range(len(num_list)):
#     if check_greater(num_list[i],i+1,len(num_list)):
#         final_lst.append(num_list[i])
    
# final_lst.append(num_list[len(num_list)-1])   
# print(final_lst)
    