a1 = {'a':5, 't':3, 'c':4, 'e':7}
b1 = {'a':3, 'l':9,'e':1, 'd':6}

at_k = tuple(a1.keys())
at_v = tuple(a1.values())

bt_k = tuple(b1.keys())
bt_v = tuple(b1.values())

print(at_k)
print(at_v)

at_ks = set(at_k)
bt_ks = set(bt_k)
newset1 = (at_ks.intersection(bt_ks))

at_vs = set(at_v)
bt_vs = set(bt_v)
newset2 = (at_vs.intersection(bt_vs))
interse_set = zip(newset1,newset2 )
print(list(interse_set))


