import pandas as pd
import numpy as np

data = pd.DataFrame({'k1':['one']*3+['two']*4,  #['one','one','one','two','two','two','two']
                     'k2': [1,1,2,3,3,4,4]})
# print(data.duplicated('k1'))
# print(data.duplicated('k2'))
#
# print(data.drop_duplicates('k1')) # inplace =True means it will modify and return the actual object

# Replacing values

data1 = pd.Series([1., -999., 2., -999., -1000., 3.])
a = data1.replace(-999, np.nan)
print(a)