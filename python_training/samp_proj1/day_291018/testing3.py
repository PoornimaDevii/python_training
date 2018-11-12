# Doc test/ black box testing
import doctest

def my_function(a,b):
    '''

    >>> my_function(2,3)
    6
    >>> my_function('a',3)
    'aaa'
    '''

    return a * b

if __name__ == '__main__':
    doctest.testmod(verbose=True)

# $ python -m doctest -v doctest_simple.py
# $ python -m doctest -v <python_file_name>