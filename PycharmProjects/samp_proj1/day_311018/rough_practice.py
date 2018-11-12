import re

pat1 = re.compile('^poo$')
name = input("Enter your name  ")
if pat1.search(name):
    print("It matched")
else:
    print("It did not match")