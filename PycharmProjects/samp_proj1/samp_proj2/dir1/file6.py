# Numpy

import pandas as pd
import numpy as np

a1 = np.array([[1,2],[6,5]])
a2 = np.arange(4).reshape(2,2)
print(a1)
print(a2)

mul = a1 * a2
print(mul)

mat = a1 @ a2 # matrix product
print(mat)

mat_other = a1.dot(a2)
print(mat_other)

li = np.linspace(0,10,5)
print(li)

three_d_ar = np.array([[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                        [ 10, 12, 13]],
                       [[100,101,102],
                        [110,112,113]]])
print(three_d_ar)

#print("random\n",10*np.random.random((2,2)))
samp = np.floor(10*np.random.random((2,2)))
print(type(samp))
print(samp)

