# Write a NumPy program to compute the eigenvalues and eigenvectors of a given square array
import numpy as np

array = np.array( [[2,3], [-2,7]])

Eigenvalue,Eigenvector = np.linalg.eig(array)

print(Eigenvalue)
print()
print(Eigenvector)



# check
# v1 = np.dot(m,v[:,0])
# print(v1)
# v2 = np.dot(w[0],v[:,0])
# print(v2)

# https://www.emathhelp.net/en/calculators/linear-algebra/eigenvalue-and-eigenvector-calculator/?i=%5B%5B3%2C-2%5D%2C%5B1%2C0%5D%5D