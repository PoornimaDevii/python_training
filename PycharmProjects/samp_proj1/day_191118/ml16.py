from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df_wine = pd.read_csv('wine.data',header=None)
df_wine.columns = ['Class Label','Alcohol','Malic Acid','Ash','Alcalinity of ash','Mg','Total phenols','Flavanoids'\
                          ,'Nonflavanoids phenols','Poranthocyanins','Color intensity','Hue','0D280/0D315 of diluted wine',
                             'Proline']
print(df_wine)

y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3) # testing data will be 30% of the training data
print(x_train.size)
print(x_train.shape)

sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)
x_test_std = sc.transform(x_test)

pca = PCA(n_components=5)
print("Standardised data",x_train_std)
x_train_pca = pca.fit_transform(x_train_std)
x_test_pca = pca.transform(x_test_std)
print("Principal data",x_train_pca)

lln = LogisticRegression(penalty='l1',C=1.0)
lln.fit(x_train_pca,y_train)
y_train_pred = lln.predict(x_train_pca)
y_test_pred = lln.predict(x_test_pca)

print("Misclassified in testing", (y_test-y_test_pred).sum())
print("Misclassified in training", (y_train-y_train_pred).sum())

# print("Training accuracy",lln.score(x_train_std,y_train_pred))
# print('Test accuracy',lln.score(x_test_std, y_test_pred))
