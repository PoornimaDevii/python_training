from datetime import datetime
import pandas as pd
import numpy as np


ts = pd.Series(np.random.rand(6),index=pd.date_range('1/1/2000',periods=6,freq='M'))

ts_local = ts.tz_localize('UTC')
print(ts_local)
print(ts_local.tz_convert('US/Eastern'))