# to multiply 2 arrays, the dim must be same (both 3x2) but to multiply 2 matrices ,the dim must be compatible
# (ie if one is 3x2, other must be 2x3 and not again 3x2)
import numpy as np

a = np.array([[1,2],[3,4]])
m = np.mat(a) # convert 2-d array to matrix
m = np.matrix([[1, 2], [3, 4]])

print(a*a)
print(a**3) # power of 3 of each elm of array

print(m*m)
print(m**3) # matrix multiplication of m*m*m
print(m.T) # transpose
print(m.H) # conjugate transpose
print(m.I) # inverse matrix