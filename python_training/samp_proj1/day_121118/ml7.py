import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame([['green','M',10.1,'class1'],
                   ['red','L',13.5,'class2'],
                   ['blue','XL',15.3,'class1']])
df.columns = ['color','size','price','classlabel']

size_mapping = {'XL':3,'L':2,'M':1}
df['size'] = df['size'].map(size_mapping)
print(df)

inv_size_mapping = {v: k for k,v in size_mapping.items()}
print(inv_size_mapping)

class_mapping = {label: idx for idx,label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)

df['classlabel'] = df['classlabel'].map(class_mapping)
print(df)

# Label encoder

X = df[['color','size','price']].values
color_le = LabelEncoder()
X[:,0] = color_le.fit_transform(X[:,0])
print(X)

# OneHot Encoder (colors are considered as features , sparse matrix(most of elms are 0) is created)

import pandas as pd
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(categorical_features=[0])
print(ohe.fit_transform(X).toarray())
