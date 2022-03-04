# Find the majority element of the given list.
# Majority element: count of the elements > N/2
# N = length of list
# A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
# Ans = 5

num_list = [5, 2, 3,3,3,3,3,3,3,3,3,3,3,3,3,3,3, 1, 5, 1, 2, 5, 5, 5]
min_count = int(len(num_list)/2)
print(min_count)
dictonary = {}

for i in num_list:
    if i not in dictonary.keys():
        dictonary[i] = 1
    else: 
        x = dictonary[i]
        dictonary[i] = x+1
        if x+1 > min_count:
            print(i)
            break

print(dictonary)

            
            
    

