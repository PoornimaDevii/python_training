# Decision tree learning
# not only holds good for linearly separable classes, can be used for multi-classes, data sets not limited to
# using graphviz for viewing tree based graph
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import graphviz, pydotplus
from sklearn import tree
from IPython.display import Image, display
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


# df_wine = pd.read_csv('wine.data',header=None)
# y = df_wine.iloc[:,0].values
# x = df_wine.iloc[:,1:].values
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3) # testing data will be 30% of the training data
# print(x_train.size)
# print(x_train.shape)
#
# lln = DecisionTreeClassifier(max_depth=1)
# a = lln.fit(x_train,y_train)
# print(a)
# y_train_pred = lln.predict(x_train)
# y_pred = lln.predict(x_test)
#
# print("Misclassified in testing", (y_test-y_pred).sum())
# print("Misclassified in training", (y_train-y_train_pred).sum())
#
# dot_data = tree.export_graphviz(lln, out_file=None,
#                                 feature_names=iris.feature_names)

iris = load_iris()
print(iris)

x = iris.data[50:150] # 2:4 are the features selected to view the misclassification (lower misclass..
y = iris.target[50:150]

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3) # testing data will be 30% of the training data
print(x_train.size)
print(x_train.shape)

ppn = tree.DecisionTreeClassifier(max_depth=1)
ppn1 = ppn.fit(x,y)
#print(a)
y_train_pred = ppn.predict(x_train)

y_pred = ppn.predict(x_test)
print("Misclassified in testing", (y_test-y_pred).sum())
print("Misclassified in training", (y_train-y_train_pred).sum())

dot_data = tree.export_graphviz(ppn1, out_file=None,
                                 feature_names=iris.feature_names, class_names=iris.target_names,
                                filled=True,rounded=True)

graph = pydotplus.graph_from_dot_data(dot_data)
display(data=graph.create_png())
plt.plot()
plt.show()

# if __name__ == '__main__':
#     iris_data = load_iris()
#     decision_tree_classifier = ppn1
#     dot_data = tree.export_graphviz(decision_tree_classifier, out_file=None,
#                                     feature_names=iris.feature_names, class_names=iris.target_names,
#                                     filled=True, rounded=True)
#     graph = pydotplus.graph_from_dot_data(dot_data)
#     display(data=graph.create_png())


