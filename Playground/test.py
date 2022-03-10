import numpy as np
m = np.array([[3,-2],[1,0]])


w, v = np.linalg.eig(m) 
print( "Eigenvalues of the said matrix",w)
print( "Eigenvectors of the said matrix",v)

print()



