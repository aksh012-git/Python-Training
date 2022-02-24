# Create a function to reverse the entire list without any function and also do not use any indexing or slicing shortcut. Time Complexity O(logn)

num_lst = [1,2,3,4,5,6,7]
num_lst_length = len(num_lst)-1

for i in range(len(num_lst)):
    if num_lst_length <= i:
        break
    num_lst[i],num_lst[num_lst_length] = num_lst[num_lst_length],num_lst[i]
    num_lst_length -= 1
    
print(num_lst)   
    
