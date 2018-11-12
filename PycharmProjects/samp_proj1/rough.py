li1 = [26,82,82,'dud']
li2 = li1
li3 = li1[:]

print(li1 is li2)
print(li1 is li3)
print(li1 == li2)


x = 3
while x < 5:
    print(x, "still in the loop")
    x = x + 1

x = 6
while x < 5:
    print(x, "still in the loop")


def fun(x):
    return x

print(dir(fun))
print(fun.__code__.__doc__)

url = 'http://www.google.com'
urllist = list(url)
print(urllist)

# 22.10.18
# Regular expressions, iterators, generators, exception handling

# magic functions - __getitem__, __new__, __call__, diff b/w new and init methods

class A(object):  # -> don't forget the object specified as base

    def __new__(cls):
        print("A.__new__ called")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print("A.__init__ called")

A()

# __getitem__

class Test(object):
    def __getitem__(self, items):
        print('%-15s  %s' % (type(items), items))

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]

# __call__ magic function

class Test(object):
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print('-'*80)

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)






