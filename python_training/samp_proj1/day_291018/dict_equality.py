# equality will work for dictionaries

keys = ['a','aa','aaa']
d1 = dict((k, len(k)) for k in keys)
d2 = dict((k, len(k)) for k in reversed(keys))
print("d1 :",d1)
print("d2 :",d2)
print("d1 == d2:", d1 == d2)
s1 = set(keys)
s2 = set(reversed(keys))
print("s1 :", s1)
print("s2 :",s2)
print("s1 == s2:", s1 == s2)

#print("d1 == s1", d1 == s1)
#print("d2 == s2", d2 == s2)