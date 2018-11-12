#Hierarchically indexed data

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'key1': ['MH', 'MH', 'MH','TN','TN'],
                  'key2': [2000,2001,2002,2001,2002],
                  'lqty': [3,2,5,6,9]})
df2 = pd.DataFrame(np.arange(12).reshape((6,2)),index=[['TN','TN','MH','MH','MH','MH'],
                                                       [2000,2000,2000,2000,2001,2002]],
                   columns=['event1','event2'])

#print(df2)
#print(df2.loc['TN']) # returns all entries under TN
#print(df2.loc['TN'].loc[2000]) # returns only those entries with TN and 2000

#print(pd.merge(df1,df2,left_on=['key1','key2'], right_index=True))