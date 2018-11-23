# Principal component analysis(PCA) (manual method)

from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

A = array([[1,2],[3,4],[5,6]])
print(A)
print("A transpose:",A.T)

M = mean(A.T, axis=1) #mean along each row
print("M:\n",M)

C = A - M
print("C:\n",C)
print("C transpose:\n",C.T)

V = cov(C.T)
print("V:\n",V)

values,vectors = eig(V)
print(values)
print(vectors)

P = vectors.T.dot(C.T)
print("P:\n",P)
print(P.T)