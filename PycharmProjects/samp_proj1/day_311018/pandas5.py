
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12).reshape(3,4),
                   columns=list('abcd'),
                   index=['tn','ka','kl'])

print(df1)
s1 =df1.loc['ka']
print(s1)

print(df1-s1) # subtracting s1 to all rows
print(df1+s1) # adding s1 to all rows
f = lambda x:x.max() - x.min()
print(df1.apply(f))# by default axis=0 ie for rows
print(df1.apply(f,axis=1))
