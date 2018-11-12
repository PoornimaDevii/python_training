
import numpy as np # includes functionalities for random numbers

#print(dir(np))

a1 = np.array([12,-9,10,8,-13]) # if one of elms is str or double, then a1.dtype will be the highest
                                # form of datatype( like double is higher than int)
a2 = np.array([-6,17,5,12,-9])
print(a1)
print(type(a1))
print(a1.dtype) # the elements of array must be of same data type, dtype is the datatype of individual elms

if type(a1) is 'numpy.ndarray':
    print("An array")


if a1.dtype == np.int64:
    print("An array of numbers")

print(a1*0.4)
print(a1[0]*0.4)

print(a1+a2)
print(a1-a2)
print(a1/a2)
print(a1*a2)