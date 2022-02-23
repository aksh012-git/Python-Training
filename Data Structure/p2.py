# Count the occurrence of each element from a list
# Sample: [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

from collections import Counter
list_num = Counter([11, 45, 8, 11, 23, 45, 23, 45, 89])
print(dict(list_num))


#-----------------------------------------------------------------

list_num = [11, 45, 8, 11, 23, 45, 23, 45, 89]
set_num = set(list_num)
dictonary = {}

for i in set_num:
    x = 0
    for j in list_num:
        if i==j:
            x += 1
            dictonary[i] = x
                  
print(dictonary)