#Write a NumPy program to compute the sum of the diagonal elements of a given array.

import numpy as np

n_array = np.array([[3, 2, 2],
					[30, 3, 2],
					[2, 5, 3]])

print(np.trace(n_array))


