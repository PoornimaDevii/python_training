import re

'''#pat1 = re.compile('^-?[0-9]+$') # ? considers max of the specific character ( or no specific character)
#pat1 = re.compile('ba?b') # for 'bb' returns matched
#pat1 = re.compile('^(\+91)?[0-9]{10}$')# \ is the escape character to nullify the meaning of + , * or like that
country = re.compile('(in|jp|uk)$')
pat1 = re.compile('^(\+91|\+44)?[0-9]{8,10}$') # | is a either or character in case of strings
cell = input("Enter the cell number")
mat = pat1.search(cell)
if mat:
    print("It matched")
else:
    print("No match")'''

'''\d means [0-9]
\d {10} means 10 characters
\d {8,10} means min 8 max 10 characters
\d {8, } means min 8 characters
 \d {,10} means max 8 characters'''

# To find all matches

p = re.compile('\d+')
print(p.findall('12 drummers drumming, 11 pipers pipping, 10 lords a-leaping'))

pat11 = re.compile('ba?b', re.IGNORECASE)
if pat11.search('BB'):
    print("It matched")
else:
    print("No match")







