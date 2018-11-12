
import pandas as pd
import numpy as np


frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                    index=[['a','b','b','b'],[1,2,1,2]],
                    columns=[['Ohio','Ohio','Colorado'],
                    ['green','red','green']])

frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']

print(frame.swaplevel('key1','key2'))
print(frame.sort_index(level=0))
print(frame.sum(level='key1'))