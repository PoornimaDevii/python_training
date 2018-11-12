# # multi-dimensional list given
# # li = [[1,2],[2,[5,6]],3]
# # output = [1,2,2,5,6,3]
# # find the deep index of the list elements like li[1][1][0]
#
# final = []
# lis1 = []
# #j = []
#
# def input_fn():
#     q = input("Is it a list or element?l/e")
#     if q == 'l':
#         il = input("Enter the inner list")
#         k = [i for i in il.split(',')]
#         j.extend(k)
#     else:
#         ie = input("Enter the element")
#         j.append(ie)
lis1 = [2,3,[4,5],[2,[4,65],6,43,34]]
# for elm in range(2):
#
#     lis1.append(j)
#print(lis1)

def list_func(lis1):
    final = []
    for i in lis1:
        if type(i) is list:
            final.extend(list_func(i))
        else:
            final.append(int(i))
        #print(final)
    print('return',final)
    return final

list_func(lis1)
print(final)







