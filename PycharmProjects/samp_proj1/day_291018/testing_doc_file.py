# nose fixtures (nose module)
import doctest


def my_function(a,b):
    return a * b



if __name__ == '__main__':
    doctest.testfile('testing_doc_file1.txt', verbose=True)
