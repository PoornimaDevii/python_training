
import pandas as pd

df = pd.DataFrame({'qty':[12,11,19,10,15,19],
                   'fg':['wh','pd','sg','pd','wh','pd'],
                   'st':['pb','tn','mh','ka','mh','wb']},index=[98,99,2001,97,2002,2005])

# print(df)
# print(df.groupby('fg').sum())
# print(df.groupby('fg').mean())
print(df['st']) # To get the column we can give like this
print("The index value",df.loc[99])# but for row,we need to use loc

#
# print("Describe",df.describe())
# print(df['st'])
# print(df.loc[2])
print(df.drop(99))
print(df.drop('fg',axis=1)) # axis=1 is column and axis=0 is row, #inplace=True - to modify the actual df
