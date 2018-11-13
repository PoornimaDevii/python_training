import pandas as pd, numpy as np


ex = pd.DataFrame(np.arange(6))
print(ex)
ex[1] = (ex[0] - ex[0].mean())/ex[0].std(ddof=0)
ex[2] = (ex[0]-ex[0].min())/(ex[0].max() - ex[0].min())
ex.columns = ['input','standardized','normalized']
print(ex)
