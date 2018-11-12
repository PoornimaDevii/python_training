
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except:
    print("Unexpected Error:", sys.exc_info()[0])
    raise