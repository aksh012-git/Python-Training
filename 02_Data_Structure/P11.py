# Return product of minimum of odd and maximum of even from a given list.
#        Sample = [7, 5,  2, 3, 12, 9, 15, 24]
#        Output = 72          #  (24 max even * 3 min odd)

num_lst = [7, 5,  2, 3, 12, 9, 15, 24]
even_max = []
odd_min = []


for item in num_lst:
    if item % 2 == 0:
        if len(even_max) ==0:
            even_max.append(item)
        elif even_max[0] < item:
            even_max[0] = item      
    else:
       if len(odd_min) ==0:
            odd_min.append(item)
       elif odd_min[0] > item:
            odd_min[0] = item  

print(even_max[0] * odd_min[0])
            
    
    
    