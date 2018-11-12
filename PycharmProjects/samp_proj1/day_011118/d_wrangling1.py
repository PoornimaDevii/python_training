import pandas as pd
import numpy as np

# df1 = pd.DataFrame({'lkey':['a','d','b'],
#                     'data1':range(3)})
# df2 = pd.DataFrame({'rkey':['a','c','a','b','c','c','b'],
#                     'data2':range(7)})
#
# print(pd.merge(df1,df2,left_on='lkey',right_on='rkey')) # how='inner' by default, gives intersection
#
# print("using how=outer\n",pd.merge(df1,df2,left_on='lkey',right_on='rkey',how='outer')) # union
# print("using how=left\n",pd.merge(df1,df2,left_on='lkey',right_on='rkey',how='left'))
# print("using how=right\n",pd.merge(df1,df2,left_on='lkey',right_on='rkey',how='right'))

# on is used for fixing/making a key constant, how is used to specify the method of wrangling like intersection,
# or union, or left oriented or right oriented

left = pd.DataFrame({'st': ['KA', 'KA', 'KL'],
                  'fg': ['pd', 'wh', 'pd'],
                  'lqty': [12, 11, 14]})
right = pd.DataFrame({'st': ['KA', 'KA', 'KL','KL'],
                   'fg': ['pd', 'pd', 'pd','cn'],
                   'rqty': [5,7,6,4]})
# #pd.merge(left, right, on=['key1', 'key2'], how='outer')
# #pd.merge(left, right, on='key1')
# #pd.merge(left, right, on='key1', suffixes=('_left', '_right'))

#print(pd.merge(left,right,on='st'))
#print(pd.merge(left,right,on='fg'))
#print(pd.merge(left,right,on=('st','fg')))

#print(pd.merge(left,right,on='st',how="outer"))
#print(pd.merge(left,right,on='fg',how="outer"))
#print(pd.merge(left,right,on=('st','fg'),how="outer"))

#print(pd.merge(left,right,on='st',how="left"))
# print(pd.merge(left,right,on='fg',how="left"))
# print(pd.merge(left,right,on=('st','fg'),how="left"))
#
# print(pd.merge(left,right,on='st',how="right"))
# print(pd.merge(left,right,on='fg',how="right"))
# print(pd.merge(left,right,on=('st','fg'),how="right"))

