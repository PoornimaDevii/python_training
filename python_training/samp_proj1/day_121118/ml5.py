# Imputer class

from sklearn.preprocessing import Imputer
import pandas as pd

imr = Imputer(missing_values='NaN',strategy='mean',axis=0) #mean of the column(axis=0)

df = pd.read_csv('sample_csv.csv')

imr = imr.fit(df)
imputed_data = imr.transform(df.values)
print(imputed_data)