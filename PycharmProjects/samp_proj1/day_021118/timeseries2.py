from datetime import datetime
import pandas as pd
import numpy as np


ts1 = pd.Series(np.random.rand(6),index=pd.date_range('1/1/2000',periods=6,freq='Y'))# 'M' is monthly, 'D' is daily,
# 'Y' is yearly
print(ts1)
print(ts1.shift(2))
print(ts1/ts1.shift(1)-1)

ts2 = pd.Series(np.random.rand(6),index=pd.date_range('1/1/2000',periods=6,freq='M'))# 'M' is monthly, 'D' is daily,
# 'Y' is yearly
print(ts2)

ts3 = pd.Series(np.random.rand(6),index=pd.date_range('1/1/2000',periods=6,freq='D'))# 'M' is monthly, 'D' is daily,
# 'Y' is yearly
print(ts3)
