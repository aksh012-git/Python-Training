# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

list_tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for index_i , i in enumerate(list_tuple):
    for index_j , j in enumerate(list_tuple):
        if i[1] < j[1]:
            list_tuple[index_i],list_tuple[index_j] = list_tuple[index_j],list_tuple[index_i]
            
print(list_tuple)          