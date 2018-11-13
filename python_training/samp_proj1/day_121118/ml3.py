# Logistic regression (usually used for binary classes)

#sigmoid function, cost fn, gradient descent

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd

df_wine = pd.read_csv('wine.data',header=None)
y = df_wine.iloc[:,0].values
x = df_wine.iloc[:,1:].values
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3) # testing data will be 30% of the training data
print(x_train.size)
print(x_train.shape)

lln = LogisticRegression(penalty='l1',C=1.0) # C=1.0 is the additional factor to increase the variance
# we need to decrease the variance. if variance dec bias inc which is not desirable. C helps in dec variance
#without affecting the bias
a = lln.fit(x_train,y_train)
#print(a)
y_train_pred = lln.predict(x_train)
y_pred = lln.predict(x_test)

print("Misclassified in testing", (y_test-y_pred).sum())
print("Misclassified in training", (y_train-y_train_pred).sum())
