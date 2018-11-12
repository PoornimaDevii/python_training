# when the depth of fn is large(fn inside a fn and so on) we use tracebacks in doctests

import doctest

def this_raises():
    '''
    This function always raises an exception.
    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error
    '''
    raise RuntimeError("here is the error")

if __name__ == '__main__':
    doctest.testmod(verbose=True)