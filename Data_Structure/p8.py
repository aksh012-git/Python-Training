#  Return the sum of duplicates elements from the given List
# 			Ex. L = [3, 5, 6, 11, 12, 3, 5, 2,2]
# 			Output = 8 (3+5)

num_lst = [3,5,6,3,3,11,12,3,5,2,2,2]
dictonary = {}
count = 0
tuple_format = ''

for i in num_lst:
    if i not in dictonary.keys():
        dictonary[i] = 1
    else: 
        x = dictonary[i]
        dictonary[i] = x+1

for key,value in dictonary.items():
    if value>1:
        count += int(key)
        tuple_format = tuple_format + '+' + str(key)
    
tuple_format = '('+tuple_format[1:]+')'  
print(count,tuple_format)
        
        
        
        
    
    