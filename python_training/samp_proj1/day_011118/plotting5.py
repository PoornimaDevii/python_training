#line plots

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.rand(10).cumsum(), index=np.arange(0,100,10))
s.plot()


# dataframe plot

df = pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'], index=np.arange(0,100,10))
df.plot()

plt.show()

