import numpy as np

arr = np.arange(100,200)
select = [2,4,22,23]
print(arr[select])

arr1 = np.arange(10,20)
div_by_3 = arr1%3 == 0
print(div_by_3)

print("The number divisible by 3 are",arr1[div_by_3])

arr2 = np.arange(10,20).reshape((5,2)) # can reshape the array -> default is 1x10
print(arr2)

print(arr1.sum())
print(arr1.mean())
print(arr1.std())
print(arr1.max())
print(arr1.min())
print(arr1.nonzero())
print(div_by_3.nonzero())# returns the indices if condition satisfied
print(div_by_3.all()) # returns true if all true
print(div_by_3.any()) # returns true if any one is true

arr4 = np.array([4.5,2.3,6.7,1.2,1.8,5.5])
x = arr4.argsort()
print(x)

y = arr4.argsort()
print(y)

arr5 = np.array([[3,2],[6,4]])
print(arr5)

#a = np.linalg.inv(arr5)# To find the inverse of the matrix
                       #  determinant is 0 so its a singular matrix, no inverse
#print(a)
print(np.eye(3))
u = np.eye(2) # eye represents I (idempotent)
print(u)


#transpose