# Answer of Question 5

from scipy import linalg

composition_matrix = [[1,4],[2,3]]

Eigenvalue,Eigenvector = linalg.eig(composition_matrix)

print(Eigenvalue)
print(Eigenvector)


import math

C = [[1,4],[2,3]]

trace_of_c = C[0][0] + C[1][1]
# print(trace_of_c)

det_product = (C[0][0] * C[1][1]) - (C[0][1] * C[1][0])
# print(det_product)

trace_of_c = -(trace_of_c)
# print(trace_of_c)

discriminant_d = ((trace_of_c ** 2) - (4*(1)*(det_product)))
# print(discriminant_d)

Eigenvalue = []
if discriminant_d > 0:
    root_val_1 = ((-trace_of_c) + math.sqrt(discriminant_d))/2
    root_val_2 = ((-trace_of_c) - math.sqrt(discriminant_d))/2
    Eigenvalue = [root_val_1,root_val_2]
elif discriminant_d == 0:
    root_val_1 = (-(trace_of_c))/2

print(Eigenvalue)

C[0][0] = C[0][0] - Eigenvalue[0] 
C[1][1] = C[1][1] - Eigenvalue[0] 

print(C)