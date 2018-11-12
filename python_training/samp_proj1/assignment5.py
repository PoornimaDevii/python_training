# f = ( [11,-9,8,17,6,7], (2,3) )


r = int(input("Enter the number of rows"))
c = int(input("Enter the number of columns"))
t = (r,c)

a = input("Enter the no of elements in list")
list1 = [int(x) for x in a.split(',')]
#print(list1)

big_t = (list1,t)
#print(big_t)
out_l = []
out_l1 = []
mul = r*c # no of lists = rows; no of elements = no of columns
if len(list1) == mul:
    print("The desired output is",big_t)
    for elm in range(len(list1)):
        out_l.append(list(list1[0:c]))
        #for elm in range(len(list1[c:])):
        out_l1.append(out_l)
    print("The matrix is",out_l1)
else:
    raise AssertionError
