# TASK 1:
# ETA 40 mins - 11.41 AM
# Now, let's imagine a rectangle of height 1 and length 2. The four corner points of the rectangle are:
# a = (0, 0)
# b = (2, 0)
# c = (2, 1)
# d = (0, 1)
# Now, apply the shearing transformation to these four points. Can you imagine the rectangle turning into a parallelogram.
# Shear matrix = [[1, 1], [0, 1]]
# Now the origin has been shifted to (1, 3)
# What will be the output points: - Solve using 2 approaches
# Without using numpy or 2D list
# Use numpy for matrix computation



import matplotlib.pyplot as plt
import numpy as np


# With numpy --------------------------------------------------------
print('With numpy:')
x_cord_of_ract = np.array([0,2,2,0])
y_cord_of_ract = np.array([0,0,1,1])

Shear_matrix = np.array([[1, 1], [0, 1]])

new_cord_of_ract = []
for cord_index in range(0,len(x_cord_of_ract)):
    # print(np.dot(Shear_matrix,[x_cord_of_ract[cord_index],y_cord_of_ract[cord_index]]))
    new_cord_of_ract.append((Shear_matrix @ np.array([x_cord_of_ract[cord_index],y_cord_of_ract[cord_index]])).tolist())

new_origin = np.array([1,3])
print(new_cord_of_ract)

chnaged_cord = []
for cord in new_cord_of_ract:
    chnaged_cord.append((new_origin+cord).tolist())

print(chnaged_cord,'\n\nWithout numpy:')




#without numpy ------------------------------------------------------

rectangle_cord = [[0,0],[2,0],[2,1],[0,1]]

Shear_matrix = [[1, 1], [0, 1]]

new_cord_of_ract = []

new_origin = [1,3]
chnaged_cord = []

for cord in rectangle_cord:
    new_cord_of_ract.append([(Shear_matrix[0][0] * cord[0]) + (Shear_matrix[0][1] * cord[1]),(Shear_matrix[1][0] * cord[0]) + (Shear_matrix[1][1] * cord[1])])
    chnaged_cord.append([(Shear_matrix[0][0] * cord[0]) + (Shear_matrix[0][1] * cord[1]) + new_origin[0],(Shear_matrix[1][0] * cord[0]) + (Shear_matrix[1][1] * cord[1]) + new_origin[1]])
    
print(new_cord_of_ract)
print(chnaged_cord)





