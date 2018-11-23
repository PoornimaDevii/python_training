# linear regression is used when definite classes (yes or no) are not available.
# Involves find the best fit line

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

df = pd.read_csv('housing.data',header=None, sep='\s+')

df.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX',
              'PTRATIO','B','LSTAT','MEDV']
print(df.head())

sns.set(style='whitegrid',context='notebook')
cols = ['RM','TAX','PTRATIO','LSTAT','MEDV']

sns.pairplot(df[cols], size=2.5)
plt.tight_layout()
#plt.show()

cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.3f',
                 annot_kws={'size':15},
                 yticklabels=cols,
                 xticklabels=cols)

plt.tight_layout()
#plt.show()

# To find the best fit line

X = df[['RM']].values
y= df[['MEDV']].values

def lin_regplot(feature,target,model):
    plt.scatter(feature,target,c='blue')
    plt.plot(feature,model.predict(feature),color='red')
    plt.show()
    return None

slr = LinearRegression()
slr.fit(X,y)
print("Slope: %.3f" % slr.coef_[0])
print("Intercept: %.3f" % slr.intercept_)
lin_regplot(X,y,slr)
plt.xlabel('No of Rooms')
plt.ylabel('Price')
#plt.show()

# calculating error for multiple classes/sections

X = df.iloc[:,:-1].values
y = df['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
ridge = Ridge(alpha=1.0) # just like penalty ( ridge is quad, lasso is linear and elastic net for large size data
slr = LinearRegression()

slr.fit(X_train, y_train)
y_train_pred = slr.predict(X_train)
y_test_pred = slr.predict(X_test)

print("MSE train: %.3f, test: %.3f" % (
    mean_squared_error(y_train,y_train_pred),
    mean_squared_error(y_test,y_test_pred)))
print("R^2 train: %.3f, test: %.3f" %(
    r2_score(y_train,y_train_pred),
    r2_score(y_test,y_test_pred)))
plt.scatter(y_train_pred, y_train_pred - y_train,
            c='blue',marker='o',label='Training data')
plt.scatter(y_test_pred,y_test_pred - y_test,
            c='red',marker='o',label='Testing data')
plt.show()