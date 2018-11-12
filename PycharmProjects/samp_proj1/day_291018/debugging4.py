# can jump out of the loop but not into for loop
import pdb

print("The program is yet to begin")
#l = [19,-12.31, 'op',(13,'lk'),8,19,-17.9, 'oi',19,'we']
i = []

def for_fn(l):
    print("beginning")
    for var in range(len(l)):
        if l[var] == 19:
            i.append(var)
print("The indices where 19 is found are", i)


print("l for reference")

pdb.run("for_fn([19,23,342,19])")
# can invoke an arbitrary fn using !pdb.run(<fn_name>)