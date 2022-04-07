import numpy as np

poly_1 = [[-10,30],[10,20],[15,10],[-20,10]]
poly_2 = [[-20,25],[15,25],[15,15],[-20,20]]

#print(False in (np.array([10,5])>np.array([9,4])))
# r = point_p1 - point_p2

max_x = 0

for cord_index_1 in range(0,len(poly_1)):
    for cord_index_2 in range(cord_index_1+1,len(poly_1)):
        #print(abs(poly_1[cord_index_1][0] - poly_1[cord_index_2][0]))
        distance_of_abs_x_point = abs(poly_1[cord_index_1][0] - poly_1[cord_index_2][0])
        if max_x < distance_of_abs_x_point:
            max_x = distance_of_abs_x_point
            
for cord_index_1 in range(0,len(poly_2)):
    for cord_index_2 in range(cord_index_1+1,len(poly_2)):
        #print(abs(poly_2[cord_index_1][0] - poly_2[cord_index_2][0]))
        distance_of_abs_x_point = abs(poly_2[cord_index_1][0] - poly_2[cord_index_2][0])
        if max_x < distance_of_abs_x_point:
            max_x = distance_of_abs_x_point
            
print(max_x)