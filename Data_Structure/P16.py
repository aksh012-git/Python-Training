# Find the elements of the given list which are exactly the same as the entire product of the list except itself
# A = [1, 5, 1, 10, 50]
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8

num_list = [1, 2, 4, 8, 1]

for i in range(len(num_list)):
    temp_product = 1
    for j in range(len(num_list)):
        if i == j:
            continue
        else:
            temp_product *= num_list[j]
    if temp_product == num_list[i]:
        print(num_list[i])
        break
        