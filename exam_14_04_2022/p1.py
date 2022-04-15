list_of_cap_direction = ['F','B','F','F','F','F','F','F','B','B','B','B','F','B']
# list_of_cap_direction = ['F','B','F','F','F','B','B','B','B']
# list_of_cap_direction = ['F','B','F','F','F','F','F','F','B','B','B','B','F','B','B','B','B']
# list_of_cap_direction = ['F','F','B']
temp_filp_for_F = []
temp_filp_for_B = []
output_filp = [[],[]]
forward_counter = 0
backward_counter = 0
flag_start = True

def addValueInForwardArray(index):
    if (index+1) not in temp_filp_for_F:
        temp_filp_for_F.append(index+1)
    
def addValueInBackwardArray(index):
     if (index+1) not in temp_filp_for_B:
            temp_filp_for_B.append(index+1)
    
def printOutput(array_2d):
    print(len(array_2d))
    for array in array_2d:
        if len(array) == 1:
            print(f'Flip {array[0]}')
        else:
            print(f'Flip {array[0]} to {array[1]}')
    
for index_of_list,cap_direction in enumerate(list_of_cap_direction):
    if cap_direction == 'F':            
        if ((len(list_of_cap_direction)-1) == index_of_list or cap_direction == list_of_cap_direction[index_of_list+1]) and flag_start:
            addValueInForwardArray(index_of_list)
            flag_start = False
        if ((len(list_of_cap_direction)-1) == index_of_list or cap_direction != list_of_cap_direction[index_of_list+1]):
            addValueInForwardArray(index_of_list)
            flag_start = True   
        forward_counter += 1     
    else:
        if ((len(list_of_cap_direction)-1) == index_of_list or cap_direction == list_of_cap_direction[index_of_list+1]) and flag_start:
            addValueInBackwardArray(index_of_list)
            flag_start = False
        if ((len(list_of_cap_direction)-1) == index_of_list or cap_direction != list_of_cap_direction[index_of_list+1]):
            addValueInBackwardArray(index_of_list)
            flag_start = True 
        backward_counter += 1
            
    if len(temp_filp_for_B) and flag_start:
        output_filp[1].append(temp_filp_for_B)
        temp_filp_for_B = []
    if len(temp_filp_for_F) and flag_start:
        output_filp[0].append(temp_filp_for_F)
        temp_filp_for_F = []
        
# print(output_filp[0],'---',output_filp[1],forward_counter,backward_counter)

if len(output_filp[0])<len(output_filp[1]):
    printOutput(output_filp[0])
elif len(output_filp[0])>len(output_filp[1]):
    printOutput(output_filp[1])
else:
    if forward_counter<backward_counter:
        printOutput(output_filp[0])
    else:
        printOutput(output_filp[1])
        
        
