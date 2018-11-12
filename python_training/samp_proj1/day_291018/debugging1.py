# Debugging - To find logical errors
# threads share the same data, processes do not share the same data ( but share only with the help of some files)
# pipe is essentially a file

# module for debugging - pdb
# command used with pdb - r (return), c (continue), h(help)

import pdb, sys

#print(dir(pdb))
def some_div(some_int):
    print("Start int", some_int)
    ret_int = 10/some_int
    print("End some int", some_int)
    return ret_int

#print(pdb.run("some_div(0)")) # returns none object when c is pressed, doesn't return the actual o/p of the program
print(pdb.runeval("some_div(2)")) # returns the actual value of the program when c is pressed
#pdb.runcall(some_div, 2) # the way of syntax differs from runeval()

# pdb.post_mortem() debugs the remaining program

if __name__ == '__main__':
    try:
        some_div(0)
    except:
        tb = sys.exc_info()[2]
        pdb.post_mortem(tb) # takes the result of the exception as argument and debugs the dead program
                             # after the exception
        