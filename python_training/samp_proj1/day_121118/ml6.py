import pandas as pd

df = pd.DataFrame([['green','M',10.1,'class1'],
                   ['red','L',13.5,'class2'],
                   ['blue','XL',15.3,'class1']])
df.columns = ['color','size','price','classlabel']
print(df)

size_mapping = {'XL':3,'L':2,'M':1}
df['size'] = df['size'].map(size_mapping)
print(df)

inv_size_mapping = {v: k for k,v in size_mapping.items()}
print(inv_size_mapping)

