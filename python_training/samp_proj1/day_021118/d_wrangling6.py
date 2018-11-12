import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key1': ['MH', 'MH', 'MH','TN','TN'],
                  'key2': [2000,2001,2002,2001,2002],
                  'data': [3,2,5,6,9]})
# df2 = pd.DataFrame(np.arange(12).reshape((6,2)),index=pd.Index(['TN','TN','MH','MH','MH','MH'],name='state'),
#                    columns=pd.Index(['event1','event2'],name='event'))
df2 = pd.DataFrame(np.arange(12).reshape((6,2)),index=pd.Index(['KL','TN','KA','TS','AP','MH'],name='state'),
                   columns=pd.Index(['event1','event2'],name='event'))

print(df2)
sdf2 = df2.stack() # vertical arrangement version of df2 (focusing index) is returned
print(sdf2)
print("Unstack(0)\n",sdf2.unstack(0))# same as sdf2.unstack('state')  # transposed version of the actual df2 is returned ( 1 is for column wise)
print("Unstack(1)\n",sdf2.unstack(1))# same as sdf2.unstack('event') # returns the actual df2

print(df2.rename(index=str.lower,columns=str.title))

