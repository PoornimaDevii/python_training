#Pandas

import pandas as pd
import numpy as np


d = {'a':42,'b':343,'c':3224}
se1 = pd.Series(np.random.randn(5),index=['one','two','three','four','five'])
print(se1)
print("slicing with series\n",se1[1:3])

ar1 = np.arange(8).reshape(4,2) # arange changes the variable directly into array, no need to use keywd 'array'
print(ar1)
print("slicing with array\n",ar1[1:3])

ar2 = np.array(np.arange(5))
print(ar2)
print(ar2.shape)
print("Able to reshape like this\n",ar2.reshape(5,1))


# print(1,se1)
# print(4343,se1.dtype)
# print(2,se1.name)
# print(3,se1.transform)
# print(4,se1.max)
# print(5,se1.size)
# print(6,se1.shape)
# print(7,se1.unique)
