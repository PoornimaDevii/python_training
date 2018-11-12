import re

'''greet = "hello\nworld"
pat1 = re.compile('hello$', re.MULTILINE)
print(pat1.search(greet))

pat2 = re.compile('.+', re.DOTALL)
print(pat2.search(greet))'''

p = re.compile(r'\W+')
print(p.split('This is a test, short and sweet, of split().'))

print(p.split('This is a test, short and sweet, of split().', 3)) # the first three strings are split
print(p.split('This is a test, short and sweet, of split().', 4))

q = re.compile('(blue|white|red)')
print(q.sub('colour', 'blue socks and red shoes')) # substitute
print(q.sub('colour', 'blue socks and red shoes', count=1))