
# Command line arguments

import sys

print("First name is", sys.argv[1])
print("Last name is", sys.argv[2])
print("Script Name is", sys.argv[0])


for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print("Cannot open",arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()