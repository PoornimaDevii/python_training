
import numpy as np

x,y = np.mgrid[1:6, 10:14] # like meshgrid ( to create contour ,3D plots)
print(x)
print(y)


x,y = np.mgrid[1:5, 10:14]
print(x)
print(y)

print(np.random.rand(5,5)) # the elms always lie b/w 0 and 1
print(np.random.rand(4,5))
print(np.random.randn(4))

