from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

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

colors = ['blue','green','red','cyan','magenta','yellow',
          'black','pink','lightgreen','lightblue','grey',
          'indigo','orange']


weights,params = [],[]
for c in np.arange(-4.,6.):
    lln = LogisticRegression(penalty='l1',C=10**c)
    lln.fit(x_train_std,y_train) # only features can be standarized, not classes or o/ps, that's y, x_train_std,y_train
    weights.append(lln.coef_[1])
    params.append(10.**c)

#print(weights)


weights = np.array(weights)

for column,color in zip(range(weights.shape[1]), colors):
    plt.plot(params, weights[:,column],
             label=df_wine.columns[column + 1],
             color=color)

plt.axhline(0,color='black',linestyle='--',linewidth=3)
plt.xlim([10**(-5), 10**5])
#plt.ylabel('Weight coefficient')
#plt.xlabel('c')
plt.xscale('log')
plt.legend(loc='upper left')


plt.show()

print("Training accuracy",lln.score(x_train_std,y_train))
print('Test accuracy',lln.score(x_test_std, y_test))
