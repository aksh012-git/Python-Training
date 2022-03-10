#  Write a NumPy program to compute the determinant of a given square array.

import numpy as np

array = [
    [1,2],
    [2,1]
]

#without round
print((np.linalg.det(array)))

#with round
print(round(np.linalg.det(array)))


# ---------------------------------------------------------------------------------


array = [
        [6,1,1],
        [4,-2,5],
        [2,8,7]        
    ]

print(round(np.linalg.det(array)))




# notes:
#  determinant of a given square array : https://www.mathsisfun.com/algebra/matrix-determinant.html