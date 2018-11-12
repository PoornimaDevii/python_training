# Keywords cannot be overwritten.
# But builtins can be overwritten

# __builtins__ is a namespace which has methods like map

map = 8

#m = list(map(lambda x:x*2, [2,1,4]))

n = list(__builtins__.map(lambda x:x*2, [2,1,4]))

print(n)

print(map)

map = __builtins__.map

m = list(map(lambda x:x*2, [2,1,4]))

print(m)

