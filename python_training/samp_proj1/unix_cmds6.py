
import os
fname = input("Enter your first name\n")
lname = input("Enter your last name\n")
print("Your first name is:", fname)
print("Your last name is:", lname)

# python3 filename < fileinwhichinputisthere
# joining two unix commands or piping
# ls | wc -l

files = os.system('ls')
print(files)