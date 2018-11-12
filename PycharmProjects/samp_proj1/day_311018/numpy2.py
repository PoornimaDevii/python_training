
import numpy as np

a34 = np.array([[12,10,-21,7],
               [-17,18,19,16],
               [13,-7,-18,10]])
print(a34)
print(type(a34)) # <class 'numpy.ndarray'>
print(a34.dtype) # int64

print(a34.size)  # returns the no of elms in matrix # 12
print(a34.shape) # returns the dimensions of matrix # (3,4)

print("The second row",a34[1]) # returns the first row
print("The first column", a34[:,0]) # returns the first col
print(a34.T[0]) # returns the first col, array are mutable to the extent the individual elms can be changed

print(a34[2,1:3]) # [-7 -18 10]
x = np.arange(0,11,2) # gives a list of nos
print(x)

print(np.linspace(0,10,25)) # first elm = 10/24  no of elms = start + summation from i=1 to step ((stop-start)/(step-1))

print(np.zeros(3))
print(np.zeros(3).dtype) # by default returns dtype as float
print("Here",np.zeros(3))
print(np.zeros((2,3), dtype=np.int64)) # size -> (3,3) or shape -> 9 can be specified

print(np.diag(a34)) # returns the so called diag elms
print(np.diag([1,2,3,4])) # returns a diag matrix




