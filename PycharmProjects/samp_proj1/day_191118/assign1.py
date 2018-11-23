# take "A man, a plan, a canal; Panama, as input. check whether it is a palindrome or not

import itertools

s = "A man, a plan, a canal; Panama"
l = list(s)
print(l)
a = []

for x in l:
    if x != '' and x.isalpha() is True:
        a.append(x)
b = []
print("a is ",a)
for elm in a:
    b.append(elm.lower())

print("b is",b)

if b[::] == b[::-1]:
    print("The string is a Palindrome!!")
else:
    print("Its not a palindrome")


