import pandas as pd

df_sample = pd.read_csv('sample_csv.csv',header=None)
df_sample.columns = ['index1','index2','index3','index4','word']
a = df_sample.set_index('word')

print(df_sample)
print("After setting index",a)