# Decorator

class myDecorator:

    def __init__(self,f):
        print("A logging is about to start")
        f()

    def __call__(self):
        print("Done")

@myDecorator
def myfunct():
    print("The function called")
myfunct()

@myDecorator
def myfunct():
    print("The function called differently")
myfunct()

# Using functions as Decorators

def entryExit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f()

@entryExit
def myfunct():
    print("The function is being called")

entryExit()
