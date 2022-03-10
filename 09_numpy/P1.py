# Write a NumPy program to compute the multiplication of two given matrices.
import numpy as np

matrix_a = [[1,2,3],[1,2,3]]
matrix_b = [[1,2],[1,2],[1,2]]

#method - 1
print(np.dot(matrix_a,matrix_b))

print('\n')
#method - 2
print(np.matmul(matrix_a,matrix_b))





#notes:
# Matrix Multiplication - https://www.studypug.com/algebra-help/multiplying-a-matrix-by-another-matrix#:~:text=The%20dot%20product%20is%20the,column%20of%20the%20second%20matrix. 