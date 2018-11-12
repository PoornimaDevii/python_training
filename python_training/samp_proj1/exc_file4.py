
import sys

def divide():
    x = int(input("Enter divisor"))
    y = int(input("Enter dividend"))
    return y/x

try:
    divide()
except:
    print(sys.exc_info()[0])