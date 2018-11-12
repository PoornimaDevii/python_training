# My first python exercise

print("Hello World!!")

x = 15
y = 23.5
z = "Hello"

if x < 20:
    print("Okay")
    print("Yes")
print("Done")


'''if x > 20:
    print("Okay")
    print("Yes")
print("Done")'''

print("The type of x is",type(x))
print("The type of z is", type(z))

print('"Hello" he said')
#print("How's that")
print('''"Hello, how's that"''')
print(r"Hello\nWorld")

# Datatype is related only to reference and not variable

if type(x) is int:
    print("x is string")
else:
    print("Something else")


help('keywords')

w = x
print(id(x))
print(id(w))
x = "World"
w = x
print(id(x)) # Same id means referring to the same reference
print(id(w))

#Swapping

a , b = 5,10
print("a is",a)
print("b is", b)

b,a = a,b
print("a is",a)
print("b is",b)

# In tuples, objects retain their datatypes
# In string, objects change to string datatype

tu1 = (12, 9.12, 'in',[18,'ty'],.17, 1.21, 'rt')
li1 = [19, -12.31, 'op', (13,'lk'), 8, -17.9, 'oi']
greet = 'good morning'
print(li1)

print("First element is", tu1[0])
print("Last element is",tu1[-1])

# Slicing, returns a copy of a subset of the original set

print(li1[1:4])
print("Last three elements",li1[-3:])
print("First three elements",li1[:3])
print(li1[4:2]) # Returns empty list

print(li1[1:20]) # prints till the end of the list even though 20 elements are not there
#print(li1[20]) # Returns index error

print(tu1[1:4])

print("All elements except first and last",li1[1,-1])

li2 = li1 # Shallow copy
li3 = li1[:] # Deep copy

print("li1 is li2", li1 is li2)
print("li1 is li3", li1 is li3)

print("The id of li1",id(li1))
print("The id of li2",id(li2))
print("The id of li3",id(li3))

'''l1 = [1,2,3]

l2 = l1
l3 = l1[:]

print(id(l1))
print(id(l2))
print(id(l3))'''

alphas = 'abcdefghijklmnopqrstuvwxyz'
print(alphas[3:24:2])
print(alphas[24:3:-1])