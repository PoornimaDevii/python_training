# dict to implement set functions
# intersection, union, subtraction, symm-diff, issubset
a = {'a':5, 't':3, 'c':4, 'e':7}
b = {'a':3, 'l':9,'e':1, 'd':6}
# print(set(a))
# print(set(b))
c,d = [],[]

# ad = set(a.items())
# bd = set(b.items())
# print(ad)
# print(bd)


for (k,v) in a.items():
    c.append((k,v))
#print(c)

for (k,v) in b.items():
    d.append((k,v))
#print(d)

s1 = set(c)
s2 = set(d)
print("The set 1 is",s1)
print("The set 2 is",s2)

s3 = s1.intersection(s2)
print(s3)
ds3 = dict(s3)
print("The intersection is",ds3)

s4 = s1.union(s2)
ls = list(s4)

# tem_d = {}
# for i in range(len(ls)):
#     tem_d[(i[0])] = i[1]
# print(tem_d)

ds4 = dict(s4)
print("The union is",ds4)

s5 = s1.symmetric_difference(s2)
print(s5)

s6 = s1.issubset(s2)
print(s6)

