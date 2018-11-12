# Functions in python

from functools import reduce
def some_math(x,y):

    '''some_math(float, float) -> float
       some arbitrary mathematical calculation
    '''
    if type(x) is not float:
        x = 1.5
    x = 1.9/x + 8.1*y
    y = 7.6/x + 3.2*(1/2*y)
    x = 2.3*(9/y + x/7.2)
    y = 5.6*x + 7/8*y
    return x + y
a , b = 4.63, 7.81

if __name__ == '__main__':
    ret = some_math('abc',b) # The function is called like this when the fn return some value
    print("Return value is %0.2f" %ret)  # in 0.2, 2 indicates the allowed no of digits after decimal
    print("a is",a)
    print("b is",b)


print(some_math.__doc__)

'''def some_math(x,y):

     some_math(float, float) -> float
       some arbitrary mathematical calculation
    
    if type(x) is not float:
        x = 1.5
    global a # Considers only the global value of a and only the local value of b as its not declared as global
    x = 1.9/x + 8.1*y
    y = 7.6/x + 3.2*(1/2*y)
    a = 2.3*(9/y + x/7.2)
    b = 5.6*x + 7/8*y
    return a + b
a, b = 4.63, 7.81
'''

# Create a function with a list and elm as arguments

def some_fn(l, elm):
    global x
    l.append(elm)


l = [1,2,3]

if __name__ == '__main__':
    some_fn(l,34)  # the function is called like this if the fn doesnot return anything
    print("The list after appending",l)
#some_fn([1,2,3,4],7)

def login(name, passwd="sme_pass", host="asterix"): # Default arguments to be passed always after non-default args
    print("Username is",name)
    print("Password is",passwd)
    print("Server name is",host)
login('anju','abcd123')
login('poornima',host="obelix") # The value of host alone will change by combiningly using default and keyword concepts


def samp_func(a,b,c):
    print(a-b+c)

samp_func(2,1,43)
samp_func(c=43, b=1, a=2)
samp_func(2,c=43, b =1)


def samp_func(a,b,c,d):
    print(a+b+c+d)

samp_func(2,1,4,5)
samp_func(c=4, b=1, a=2, d=5)
samp_func(a=2,d=5,c=4, b =1)


def varargs(*args):
    print(args)
varargs('s','d')
varargs(12,10,19)

def varkwargs(*args,**kwargs):
    print("Non keyword arguments are",args)
    print("Keywords arguments are",kwargs)
print("With only nonkeywords")
varkwargs('a','b')
print("With only keywords")
varkwargs(x='a',y='b')
print("With both keywords as well as nonkeywords")
varkwargs('a','b',u=1,v=2,w=3)

# Functions are first-class objects

def square(x):
    return x*x

def applier(q,x):
    return q(x)

applier(square,7)

# Create a function called double, similar to the upper one

def double(x):
    print(2*x)

def apply(q,x):
    return q(x)

apply(double,3)


def applier2(q,x,y):
    print(q(x,y))


def myadd(x,y):
    print(x+y)

print(applier2(myadd,4,5))


# Instead of the above applier function

def applier(q,x):
    return q(x)

print(applier(lambda x:x*x,5))

print(myadd.__code__.co_argcount)
print(myadd.__code__.co_nlocals)
print(myadd.__code__.co_varnames)

def myfunc1(n):
    return lambda x: n+x
f1 = myfunc1(5)
f2= myfunc1(10)
print(f1(6))
ie = myfunc1('http://')
cr = myfunc1('https://')
print(ie('myhcl.com'))
print(cr('mail.hcl.com'))

# Python's higher order functions - map and filter
# map function - accepts a manipulative function and manipulates each elm of list
#filter function - accepts a fn containing condition


def square1(x):
    return x*x

def even1(x):
    return 0 == x % 2

m = list(map(square1, range(10,20)))
print(m)
n = list(filter(even1, range(10,20)))
print(n)

sem1 = [12,11,13,9,17]
sem2 = [11,15,14,15,6]
print("The resultant list is",list(map(lambda x,y:x+y, sem1, sem2)))

print("The sum of all elms in the list",reduce(lambda x,y:x+y, sem1))
print("The sum of all elms in the list sem2", reduce(lambda x,y:x+y, sem2))

url = 'http://www.google.com'
urllist = list(url)
print(urllist)
urllist.insert(4,'s')
print(urllist)
print(reduce(lambda x,y:x+y, urllist))
print(list(zip(sem1,sem2)))
print(dict(zip(sem1,sem2)))

print(list(reversed(sem1))) # Returns an object that is reversed, the actual list remains unchanged

# list comprehensions - syntax - [expression for name in list]

li = [3,6,2,7]
m = [elem*2 for elem in li] # replacing map function
print(m)

li1 = [('a',1),('b',2),('c',7)]
p = [[n*3, x*n] for (x,n) in li1]
print(p)
#print(q)

def subtract(a,b):
    return a-b

oplist = [(6,3),(1,7),(5,5)]
q = [subtract(y,x) for (x,y) in oplist]
print("Result of a fn in a list comprehension",q)

# Filtered list comprehension - syntax - [expression for name in list if filter]

li2 = [3,6,2,7,1,9]
r = [elem*2 for elem in li2 if elem > 4]
print("The result of filtered list comprehension",r)

# Nested list comprehension - syntax - [expression for name in list]

li3 = [3,2,4,1]
s = [elem*2 for elem in [item+1 for item in li]]
print("The resultant of nested list comprehension is",s)

# empty containers

emp_list = []
emp_tuple = ()
emp_dictionary = {}

# String operations always returns only a modified string objects, and doesn't modify the actual string, but a list can be manipulated/modified in place

greet = "good morning"
print(greet.title())
print(greet.upper())
print(greet.capitalize())

# isdigit(), isalnum(), isalpha()

wage = input("Enter the hrly wage")
if wage.isdigit():
    wage = int(wage)
    print("Verified ok")
else:
    wage = 0
    print("Please enter valid wage")

# print is just a reserved word in python 2.7, and print is a function in python3

print("Hello",end=' ')
print("World")
print("Hello","World",sep=':')


x1 = 'abc'
y1 = 34

print("%s is %d"%(x1,y1))

fname, lname = 'anju','savvy'
print(":%-10s:%10s:" %(fname,lname)) # -10 means left justification with 10 characters allowed
                                    # 10 means right justification with 10 characters allowed


# Join - syntax - <separator_string>.join(<some_list)
# from a list to string

li3 = ['abc', 'def','ghi']
print(';'.join(li3))

# Split - syntax - <some_string>.split(<separator_string>)
# from a string to list

str1 = 'abc;def;ghi'
print(str1.split(';'))







