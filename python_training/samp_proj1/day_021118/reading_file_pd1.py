import pandas as pd

# if space is there in the file (other than csv), write sep='\s+', if header is needed add header=0 meaning
# 0th row is the header

df_wine = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df_wine.columns = ['Type','Alcohol','Malic Acid','Ash','Alcalinity of ash','Mg','Total phenols','Flavanoids'\
                          ,'Nonflavanoids phenols','Poranthocyanins','Color intensity','Hue','0D280/0D315 of diluted wine',
                             'Proline']

print(df_wine.head()) # will get the first five rows in data

#print(type(df_wine))
data = df_wine.loc[1:]
print(data)

data1 = df_wine.iloc[:,1:].values # loc will take index names, iloc will take the index values
print(data1)