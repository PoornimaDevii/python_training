from sklearn.datasets import load_iris # iris is flower data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

iris = load_iris()
print(iris)

x = iris.data[:150] # 2:4 are the features selected to view the misclassification (lower misclass..
y = iris.target[:150]

print(x)
print(y)

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


