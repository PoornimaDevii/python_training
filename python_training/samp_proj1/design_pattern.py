# Gang of four (GOF) design pattern - periodic table

#Creational, structural, behavioural patterns

# Singleton design pattern


import gc
print(dir(gc))
from copy import deepcopy
class Singleton(object):

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)
s3 = deepcopy(s1)
print(s3)

# Monostate singleton

class Borg:

    __shared_state = {"1":"2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4
print("Borg object 'b': ", b)
print("Borg object 'b1' : ", b1)
print("Object State of 'b' :", b.__dict__)
print("Object State of 'b1' :", b1.__dict__)

# Metaclass

class MyInt(type):

    def __call__(cls, *args, **kwds):

        print("*****Here's my int*****", args)
        print("Now do whatever you want with these objects")
        return type.__call__(cls, *args, **kwds)

class int(metaclass=MyInt):
    def __init__(self,x,y):
        self.x = x
        self.y = y
i = int(4,5)

# Factory method

