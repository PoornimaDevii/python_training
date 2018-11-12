# program to find out the locations/indices of 19

l = [19,-12.31, 'op',(13,'lk'),8,19,-17.9, 'oi',19,'we']
i = []
for var in range(len(l)):
    if l[var] == 19:
        i.append(var)
print("The indices where 19 is found are", i)


#print(l.count(19))

i = [var for var in range(len(l)) if l[var] == 19]
print("The indices where 19 is found are", i)


# Program to delete duplicates from a list

g = [3,22,532,27,3,9,6,5,2,1,6,6,2,1]

h = []
for elm in g:
    if elm not in h:
        h.append(elm)

print("The list without duplicates is",h)


'''h = [elm for elm in g if (elm not in h)]
print(h)'''
#print(set(g))

'''gs = set(g)
for elm in gs:
    if elm in set(g):
        h.append(elm)
        gs.remove(g[elm])
        if not gs:
            break

print(h)'''

user = {'name':'sandeep', 'pass':'sandeep','uid':5314, 'ext': 9012}
key_l = []
v = input("Enter the value whose key(s) are needed")
for (key,value) in user.items():
    if v == value:
        key_l.append(key)

print(key_l)


