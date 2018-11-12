import pandas as pd, numpy as np

s1 = pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])

#print(s1+s2)
print(s1.add(s2))

d1 = pd.DataFrame({'colors':['red','yello','blue','green']},index=[2,3,42,4])
d2 = pd.DataFrame({'colors':['violet','yello','pink','maroon']},index=[43,32,343,43])

print(d1+d2)

#d3 = pd.DataFrame()