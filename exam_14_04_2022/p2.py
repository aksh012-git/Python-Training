arr_1 =[1,2,3,6,7,9]
arr_2 = [3,5,8,10,11]

arr_1 =[4,7,9,15,20]
arr_2 = [3,5,9,17]

loop_countting = len(arr_1) + len(arr_2)
merged_array = []

# print(loop_countting)
index_of_arr_1 = 0
index_of_arr_2 = 0

for i in range(0,loop_countting):
    if index_of_arr_2 < len(arr_2) and index_of_arr_1 < len(arr_1) and arr_1[index_of_arr_1] < arr_2[index_of_arr_2]:
        # print(arr_1[index_of_arr_1],index_of_arr_1,'----')
        merged_array.append(arr_1[index_of_arr_1])
        index_of_arr_1 += 1
    elif index_of_arr_1 < len(arr_1) and index_of_arr_2 < len(arr_2) and arr_1[index_of_arr_1] > arr_2[index_of_arr_2]:
        # print(arr_2[index_of_arr_2],index_of_arr_2)
        merged_array.append(arr_2[index_of_arr_2])
        index_of_arr_2 += 1
    elif index_of_arr_1 < len(arr_1) and index_of_arr_2 < len(arr_2) and arr_1[index_of_arr_1] == arr_2[index_of_arr_2]:
        # print(arr_2[index_of_arr_2])
        merged_array.append(arr_2[index_of_arr_2])
        merged_array.append(arr_2[index_of_arr_2])
        index_of_arr_2 += 1
        index_of_arr_1 += 1
    
# print(index_of_arr_1,index_of_arr_2, len(arr_1),len(arr_2))

if index_of_arr_1 != len(arr_1):
    print(merged_array + arr_1[index_of_arr_1:len(arr_1)])
elif index_of_arr_2 != len(arr_2):
    print(merged_array + arr_2[index_of_arr_2:len(arr_2)])
else:
    print(merged_array)
    
    