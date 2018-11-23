from numpy import array
from sklearn.decomposition import PCA

A = array([[1,4],[3,4],[5,9]]) # no. of columns are no. of features, compare with datasets
print(A)

pca = PCA(2)
#print(help(PCA))

pca.fit(A)

print(pca.components_)
print(pca.explained_variance_)

B = pca.transform(A)
print(B)