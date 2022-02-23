# Sort given array of three random elements. 0,1 & 2. Without any sorting algorithm. Time complexity: O(n)
# Sample: [1,0,2,2,0,1,0,1,2,0,0]
# Output: [0,0,0,0,0,1,1,1,2,2,2]

list_num = [1,0,2,2,0,1,0,1,2,0,0]
l1=[]
l2=[]
l3=[]

for item in list_num:
    if item == 0:
        l1[len(l1):] = [item]
    elif item == 1:
        l2[len(l2):] = [item]
    else:
        l3[len(l3):] = [item]
        
list_num = l1+l2+l3
print(list_num)