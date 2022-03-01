# Find the majority element of the given list.
# Majority element: count of the elements > N/2
# N = length of list
# A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
# Ans = 5

num_list = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
min_count = int(len(num_list)/2)
num_set = set(num_list)

for i in num_set:
    count = 0
    for j in num_list:
        if i==j:
            count+=1
    if count > min_count:
        print(i)
        break
            
            
    

