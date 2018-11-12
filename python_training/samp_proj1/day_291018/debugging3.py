
import pdb

def f1(some_arg):
    some_other = some_arg + 1
    print(some_other)
    myadd(some_arg, some_other)
    return f2(some_other)

def f2(some_arg):
    some_other = some_arg + 1
    some_other = 2 * some_other - 17
    some_arg = 3 * (some_other + 12)
    myadd(some_arg, some_other)
    some_other = some_other + some_arg
    print(some_other)
    return f3(some_other)

def f3(some_arg):
    some_other = some_arg + 1
    print(some_other)
    return f4(some_other)

def f4(some_arg):
    some_other = some_arg + 1
    some_other = 2 * some_other - 17
    some_arg = 3 * (some_other + 12)
    some_other = myarith(some_other, some_arg)
    print(some_other)
    return some_other

def myadd(x,y):
    print("x is", x)
    print(x+y)

def myarith(x,y):
    x = 9/x + 1.8*y
    y = 7.8*(x/9 + 2.3*y)
    return x + y

pdb.run("f1(1)")
# These are debugging functions
# s for single stepping <- debugger commands ( will step into a function if function call is there)
# p for print
# n is another cmd for single stepping ( will not step into a function)
# b for breakpoint( at function or a line)
# values of variables can be updated using !<variable_name> = <new_value>
# disable <breakpt_no> ( disables the break point) or to enable <breakpt_no>
# clear <breakpt_no> to delete the breakpt
# j ( used to jump to any line only within a specific function)