#Regular expressions

import re
#pat1 = re.compile('(?hello)[a-z0-9A-Z]*(hello)')
pat1 = re.compile('[hello]*')
text = input("Enter the text ")
if pat1.search(text):
    print("It matched")
else:
    print("It did not match")

# '^' denotes the beginning of string

'''pat1 = re.compile('^san')
name = input("Enter your name  ")
if pat1.search(name):
    print("It matched")
else:
    print("It did not match")'''

# '$' denotes the end of string

'''pat1 = re.compile('san$')
name = input("Enter your name  ")
if pat1.search(name):
    print("It matched")
else:
    print("It did not match")'''


'''pat1 = re.compile('^san$') # Exactly matching words
name = input("Enter your name  ")
if pat1.search(name):
    print("It matched")
else:
    print("It did not match")'''


'''pat1 = re.compile('^[0-9]+$') # find any numbers from 0-9 and one or more digits
num = input("Enter your cell number")
if pat1.search(num):
    print("It matched")
else:
    print("It did not match")'''

# regular expressions are eager ( fast to start and fast to stop) for eg. that hat is my hat( stops when 'hat' in 'that' is found)
# but if condition specified, RE is greedy ( starts and continues till as much matches are found)
# for eg: [0-9]+ in ab957c93kli39 returns 957

'''pat1 = re.compile('[0-9]+')
target = 'ab956c87kli92'
mat = pat1.search(target)
if mat:
    print("It matched :", mat.group(0))
else:
    print("No match")'''

'''pat1 = re.compile('(.+)([0-9]+)') # (.+) or (.*) checks the string from reverse
target = 'ab956c87kli92'
mat = pat1.search(target)
if mat:
    print("It matched :", mat.group(0))
    print("It matched : ", mat.group(1))
    print("It matched :", mat.group(2))
else:
    print("No match")'''

'''pat1 = re.compile('([a-z 0-9]+)(.+)') # to match from right to left put (.*) or (.+) at the beginning
target = 'poornimadevi@gmail.com'
mat = pat1.search(target)
if mat:
    print("It matched :", mat.group(0)) # matches the whole thing
    print("It matched: ",mat.group(1)) # matches the condition in 1st parentheses
    print("It matched : ", mat.group(2)) # matches the condition in 2nd parentheses
else:
    print("No match")'''


'''pat1 = re.compile('^[0-9]{10}$') # {10} specifies exactly ten digits
target = '8634732322'
mat = pat1.search(target)
if mat:
    print("It matched :", mat.group(0))
else:
    print("No match")'''






