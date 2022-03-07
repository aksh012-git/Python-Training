# Find the elements of the given list which are exactly the same as the entire product of the list except itself
# A = [1, 5, 1, 10, 50]
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8

num_list = [1, 2, 8,4, 1]

for i in range(len(num_list)-1):
    if num_list[i] > num_list[i+1]:
        num_list[i],num_list[i+1] = num_list[i+1],num_list[i]

multiplication = 1    
for i in range(len(num_list)):
    if multiplication == num_list[len(num_list)-1]:
         print(multiplication)
         break
    multiplication *= num_list[i]
        
        
        