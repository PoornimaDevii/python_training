
# see expandtabs()
def gen_f(fname):
     with open(fname) as file:
         file_lines = file.readlines()
         for each in file_lines:
             if each == '\n':
                 a = each.strip()
                 yield a


j = 0
for i in gen_f('/home/cisco/PycharmProjects/samp_proj1/day_201118/para.txt'):
    print(i)
    j += 1

print("No of paras",j)

# lis = list(map(lambda x: x ,open('para.txt').readlines()))
# print(lis)
# lis1 =0
# i =0
# count=0
#
# while i<len(lis):
#     count=0
#     if i+2  < len ( lis ) and lis[i]!='\n' and lis[i+2]=='\n' :
#         lis1+=1
#     elif  i+2  > len ( lis ) and lis[ i ]:
#         lis1+=1
#     i+=1
#
# print("The number of paras",lis1)
#
