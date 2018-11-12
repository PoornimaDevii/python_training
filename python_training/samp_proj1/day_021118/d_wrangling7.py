import pandas as pd
import numpy as np

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])

print(b)
a_and_b = pd.concat([a,b],keys=['one','two'])
print(a_and_b)
print(a_and_b.unstack(0)) # provides transposed version of a_and_b
print(a_and_b.unstack(1)) # provides actual version of a_and_b