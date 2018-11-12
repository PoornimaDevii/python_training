import pandas as pd, numpy as nd

obj = pd.Series(['pd','wh','cs'], index=[0,4,8])
print(obj.reindex(range(11),method='ffill')) #forward fill

obj = pd.Series(['pd','wh','cs'], index=[2,7,10])
print(obj.reindex(range(11),method='bfill',limit=2)) # back fill -> limit is there upto how much to bfill
print(obj.drop(2))


frame = pd.DataFrame(nd.arange(9).reshape((3,3)), index=['a','c','d'])
print(frame)

frame2 = frame.reindex(['a','b','c','d'],method='ffill') # only using method='ffill' we get a smooth df
print(frame2)



