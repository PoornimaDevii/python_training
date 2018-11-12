from sklearn.datasets import load_iris # iris is flower data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

iris = load_iris()
print(iris)

x = iris.data[50:150,2:4] # 2:4 are the features selected to view the misclassification (lower misclass.. 
y = iris.target[50:150]

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3) # testing data will be 30% of the training data
print(x_train.size)
print(x_train.shape)

ppn = Perceptron(max_iter=10, eta0=0.1) # the eta0 i the learning rate constant, # eta0, max_iter, features can be
# modified, hence called hyper parameters
a = ppn.fit(x_train,y_train)
#print(a)
y_train_pred = ppn.predict(x_train)

y_pred = ppn.predict(x_test)
print("Misclassified in testing", (y_test-y_pred).sum())
print("Misclassified in training", (y_train-y_train_pred).sum())
import pandas as pd

new_data = pd.DataFrame([{'petal length (cm)':4.7,
                          'petal width (cm)':1.4},
                         {'petal length (cm)':5.1,
                          'petal width (cm)':1.8}])
new_data = new_data[['petal length (cm)',
                     'petal width (cm)']]
new_pred = ppn.predict(new_data)
new_data['label'] = new_pred
print(new_data)