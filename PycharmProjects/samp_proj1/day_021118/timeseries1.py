from datetime import datetime
import pandas as pd
import numpy as np

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts1 = pd.Series(np.random.randn(6), index=dates)
print(ts1)
ts2 = pd.Series(np.random.randn(6), index=dates)
print(ts2)
print(type(ts1))


