import numpy as np

n = 5
pattern_array = np.zeros([n,n])
# print(pattern_array)

row = 1
column = 0
flag_decrease = False
flag_increase = True
level_of_column = n
level_for_row = 1
value = 1

for i in range(0,((n**n)+(n-1))):
    if flag_increase and column < level_of_column:
        column+=1
        # print(row,column)
        pattern_array[row-1,column-1] = value
        value += 1
    elif flag_increase and row < n:
        row+=1
        # print(row,column)
        pattern_array[row-1,column-1] = value
        value += 1
    elif row == n and column == level_of_column and flag_increase:
        level_for_row += 1
        level_of_column -= 1
        flag_increase = False
        flag_decrease = True
        column -= 1
    elif flag_decrease and row > level_for_row:
        #  print(row,column)
         pattern_array[row-1,column-1] = value
         value += 1
         row -= 1
    elif flag_decrease and column >= 1:
            # print(row,column)
            pattern_array[row-1,column-1] = value
            value += 1
            column-= 1
    elif flag_decrease and row == level_for_row and column == 0:
        row += 1
        flag_decrease = False
        flag_increase = True
        level_for_row += 1
        level_of_column -= 1
        
print(pattern_array)