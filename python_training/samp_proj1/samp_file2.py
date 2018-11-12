alphas = 'abcdefghijklmnopqrstuvwxyz'
print(alphas[3:24:2]) # Stop place will be considered n-1, m:n
print(alphas[24:3:-1]) # Stop place will be considered n+1, m:n
print(alphas[::-1])

pal = "able was i ere i saw elba"
if pal == pal[::-1]:
    print("It's a palidrome")
else:
    print("It's not a palidrome")


pal1 = 'amanaplanacanalpanama'
if pal1 == pal1[::-1]:
    print("Palindrome")
else:
    print("Not palidrome")

# in is called membership operator

l1 = [23, ['e',24]]
print(23 in l1)
print('e' in l1)
print('e' in l1[1])

# '+ operator used for concatenation
# '*' operator used for repeition

l2 = [2,43,533]
l3 = ['elo',903, 93]
print(l2 + l3)
print(l2 * 4)

tu1 = (12, 9.12, 'in',[18,'ty'],.17, 1.21, 'rt') # The list (as an element) within the tuple can be changed
li1 = [19, -12.31, 'op', (13,'lk'), 8, -17.9, 'oi'] # The tuple (as an element) within the list cannot be changed
li1[0]  = 21
print(li1)

#tu1[0] = 232
#print(tu1)

tu1[3][0] = 20
print(tu1)

print(dir(l1)) # Returns the list of methods associated with the l1(list) datatye
print(l1.count.__doc__) # Returns the explanation for the 'count' fn

k = "Python"
print(dir(k))

l4 = [2,74,'e',843]
l4.append([23,22]) # append takes only one argument
print(l4)

l4.insert(0,'u')
print(l4)

l4.insert(2,'v')
print(l4)

print(id(li1))
li1.extend([19,'we'])  #line 62 and 64 give the same output but the memory id of the list has changed meaning, new list has been created
li1 = li1 + [19,'we']
print(id(li1))

l5 = [122,42,23,27,122,122]
print(l5.index(122))
print(l5.index(122,-1))

print("Number of times 122 occurs",l5.count(122))
l5.remove(122) # Takes value of the element to be removed as the argument
print(l5)
l5.pop() # Pops the last element by default
l5.pop(3) # Takes index of the element to be popped as the argument
print(l5)

del l5[0] # This also can be used to delete an element from the list
print(l5)

l6 = [4,3,8,2,3,2]
l6.reverse()
print(l6)

l6.sort()
print(l6)

tuX = (9) # Tuple is not created, an object of type 'int' is created
tuY = (9,) # Valid singleton tuple, comma is the tuplification operator, parantheses for a tuple is just for readability sake

print(type(tuX))
print(type(tuY))

user = {'name':'sandeep','pass':'somepass','uid': 5314, 'ext': 9012}
print(user['name']) # 'name':'sandeep' is not the first element

user['cell'] = 9384394733
print(user)

print(dir(user))
print(user.update.__doc__) # Returns the document string of the specified function

# Dic extraction funtions - keys, items, values

print(user.keys()) # user.keys returns just an object name
print(user.values())
print(user.items())

#user.pop('name') # user.pop(<key>)
print(user)

user.setdefault('a',1)
print(user)

d1 = {}
#d1.update(('a','b'))
'''k1 = input("Enter the key")
if k1 in user:
    print(k1, "has value of",user[k1])
else:
    print("No such key")'''

lis1 = [12,11,-9,12,19,-9,12,11]
lis2 = [-9, 16, 10,-9,19,19,16,16]
s1 = set(lis1)
s2 = set(lis2)
print("s1 is", s1)
print("s2 is", s2)
print(type(s1))
print(type(s2))

#print(s1[0]) # Throws error

print(dir(s1))
print("Union",s1.union(s2))
print("Intersection",s1.intersection(s2))
print("Disjoint?", s1.isdisjoint(s2))
print("Issubset?",s1.issubset(s2))
print("Issuperset?",s1.issuperset(s2))

# Extra list manipulation functions

l7 = [736,82,'loje',93.9,'oei']
print(list(range(10)))
print(len(l7))
print(list(enumerate(l7)))

#print(enumerate(l7))

x, y , z = 5,10,15
print(z<16 or x> 6 and y<9)
wage = int(input("Enter the wage"))
print("Daily wage is", wage * 8)
print("High" if wage > 2500 else "Moderate")

if x == 3:
    print("X equals 3")
elif x == 2:
    print("X equals 2")
else:
    print("X equals something else")


i = 0
while i < 10:
    #i = i + 1
    i += 1
    if i <= 4:
        print("Continue")
        continue
    print("i is",i)
    if i >= 8:
        print("Break")
        break

l8 = [19, -12.31, 'op', (13,'lk'), 8, -17.9, 'oi']
for var in range(len(l8)):
    print("var is", l8[var])


for mykey in user.keys():
    print(mykey,"=>",user[mykey])

for (k,v) in user.items():
    print(k,"=>",v)

for X in user.items():
    print(X[0],"=>",X[1])
