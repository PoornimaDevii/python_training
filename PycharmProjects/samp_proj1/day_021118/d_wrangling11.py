# filtering out missing data

import pandas as pd
import numpy as np
from numpy import nan as NA

data = pd.Series([1,NA,3.5,NA,7])
print(data.dropna())

print(data[data.notnull()])

data1 = pd.DataFrame([[1.,6.5,3.],[1.,NA,NA],[NA,NA,NA],[NA,6.5,3.]])

print(data1.dropna(how='all'))
print(data1.dropna(how='any'))
print(data1.dropna(thresh=2)) # elements with 2 or more NA are dropped