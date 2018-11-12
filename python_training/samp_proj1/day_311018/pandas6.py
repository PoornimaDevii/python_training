import pandas as pd, numpy as np

a34 = np.array([[12,10,-21,7],
               [-17,18,19,16],
               [13,-7,-18,10]])

obj = pd.Series(range(4), index=['d','a','b','c'])
print(obj.sort_index())

frame1 = pd.DataFrame(a34, index=['three','one','two'],columns=['d','a','b','c'])
print(frame1)

print(frame1.sort_index()) #row wise (alphabetical wise)
print(frame1.sort_index(axis=1)) # column wise

print(frame1.sort_index(by='b'))

obj1 = pd.Series([7,-5,7,4,2,0,4])
print(obj1.rank()) # first sort the series, and then if two elms are equal add their
                   # indices divided by the no of equal elms