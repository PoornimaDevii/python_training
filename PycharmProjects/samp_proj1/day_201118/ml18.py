from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline



df_wdbc = pd.read_csv('wdbc.data',header=None)
print(df_wdbc)

x = df_wdbc.iloc[:,2:].values
y = df_wdbc.iloc[:,1].values

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=1)

pipe_lr = Pipeline([('scl',StandardScaler()),
                    ('pca',PCA()),
                    ('clf',LogisticRegression(random_state=1,penalty='l1'))])

pipe_lr.fit(x_train,y_train)
print('Training accuracy: %3f' % pipe_lr.score(x_train,y_train))
print('Test accuracy: %3f' % pipe_lr.score(x_test,y_test))
y_pred = pipe_lr.predict(x_test)
print("Misclassified",(y_pred!=y_test).sum())


