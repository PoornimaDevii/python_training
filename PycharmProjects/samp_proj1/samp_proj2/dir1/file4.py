

import math


print("default pi:",math.pi, "with id",id(math.pi), type(math.pi))
math.pi = 1

print("defined pi:",math.pi,"with id",id(math.pi),type(math.pi))

class new1():

    def __init__(self):
        self.a = math.pi

new_obj = new1()
print(new_obj.a)

print(math.pi,id(math.pi),type(math.pi))

# di = {'a':1,'b':2,'c':3,'d':4}
# print('abcd'.translate(di))
# print(dir(str))
# print(str.translate.__doc__)

   # Required to call maketrans function.



intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)

str = "this is string example....wow!!!"
print(str.translate(trantab))