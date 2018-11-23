## take "A man, a plan, a canal; Panama, as input. reverse every word in the string

s = 'A man, a plan, a canal, a panama'

a = s.strip().split()

print(a)

r = []

for elm in a:
    r.append(elm[::-1])

#print(r)

print("the output is",' '.join(r))

rev = []

# To reverse the reversed sentence

for elm in reversed(r):
    rev.append(elm)

#print(rev)

print("The output is",' '.join(rev))
