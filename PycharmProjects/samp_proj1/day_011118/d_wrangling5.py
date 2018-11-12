
# Combining data with overlap

import pandas as pd, numpy as np

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])


b[-1] = np.nan
# print(a.combine_first(b)) # a is the main focus, and b's value is taken when 'a' has nan
# print(b.combine_first(a)) # b is the main focus, and a's value is taken when 'b' has nan

print(np.where(pd.isnull(a), b, a))
print(b[:-2].combine_first(a[2:]))


df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
print(df1.combine_first(df2))