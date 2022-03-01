# Calculate the sum of the major and minor diagonals of the given matrix
# A = [ [2, 0, 7],
#       [4, 1, 9],
#       [8, 1, -1], 
#      ]
# ans = 2, 16

matrix = [ 
        [2, 0, 7],
        [4, 1, 9],
        [8, 1, -1], 
     ]
length_of_matrix = len(matrix) - 1
sum_of_major = 0
sum_of_minor = 0

for i in range(len(matrix)):
    sum_of_major += matrix[i][i]
    sum_of_minor += matrix[i][length_of_matrix]
    length_of_matrix -= 1

print(sum_of_major,sum_of_minor)