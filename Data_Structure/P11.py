# Return product of minimum of odd and maximum of even from a given list.
#        Sample = [7, 5,  2, 3, 12, 9, 15, 24]
#        Output = 72          #  (24 max even * 3 min odd)

num_lst = [7, 5,  2, 3, 12, 9, 15, 24]
even_max = []

for item in num_lst:
    if item % 2 == 0:
        even_max.append(item)
        num_lst.remove(item)

print(max(even_max)*min(num_lst))
    
    
    