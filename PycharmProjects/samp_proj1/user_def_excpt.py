
# User-defined exceptions

'''class MyExcept(Exception):

    def __init__(self):
        return
    def __str__(self):
        print("My Except Occurred")

def myfunc():
    raise MyExcept

try:
    myfunc()
except:
    print("Caught an exception")
    raise # use it when you don't know which exception to raise'''

# Use of finally

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Division by Zero!")
    else:
        print("Result is", result)

    finally:
        print("Executing finally clause")

divide(6,4)
divide(6,0)