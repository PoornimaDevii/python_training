
import doctest

class MyClass:
    pass

def myfunc(obj):
    '''
    >>> myfunc(MyClass()) #doctest: +ELLIPSIS
    <__main__.MyClass object at 0x...>
    '''
    return obj

if __name__ == '__main__':
    doctest.testmod(verbose=True)