# Dealing with files in python

import os
import sys

def file_wr(filename):
    if os.path.exists(filename):
        sys.stderr.write("File exists\n")
        sys.exit(2)
    f = open(filename,'w')
    f.write('aaaaaaaaaaaaaa\n')
    f.write('bbbbbbbbbbbbbb\n')
    f.write('cccccccccccccc\n')
    f.close()

def file_rd(filename):
    if not os.path.exists(filename):
        sys.stderr.write("No such file")
        sys.exit(3)
    f = open(filename)
    #print(f.read())
    print(f.readline())
    print(f.seek.__doc__)
    f.seek(9,0) # the second zero in the seek() is 0 to seek beginning, is 1 to seek middle, 2 to seek end
    print(f.readlines())
    f.close()

def list_wr(fname, lst):
    f = open(fname,'w')
    lst = list(map(lambda x: str(x)+'\n', lst))
    f.writelines(lst)
    f.close()


def list_rd(fname):
    f = open(fname)
    f_list = f.readlines()
    #print(f_list)
    o = list(map(lambda x: int(x.strip('\n')), f_list))
    print(o)
    f.close()

'''def dict_wr(fname,dct):
    f = open(fname,'w')
    dct = list(map(lambda x: (str(x.items()[0])+','+ str(x.items()[1])+'\n'),dct))
    f.writelines(dct)
    f.close()'''

def dict_wr1(filename,d1):
    f = open(filename,'w')
    for (k,v) in d1.items():
        f.write(str(k)+','+str(v)+'\n')
    f.close()

def dict_rd(filename):
    f = open(filename)
    rlis = list(map(lambda x:x.strip(),f.readlines()))
    rlis = list(map(lambda x:x.strip(),f.readlines()))
    rlis = list(map(lambda x:x.split(','),rlis))
    content = dict(map(lambda x:(x[0],int(x[1])),rlis))
    f.close()


lst1 = [12,19,17,5]
dct = {'u':1,'v':3,'w':6}
d1 = {'u':1,'v':3,'w':6}
if __name__ == '__main__':
    #file_wr('output.txt')
    #file_rd('output.txt')
    #list_wr('listout.txt',lst1)
    #list_rd('listout.txt')
    #dict_wr('dictout.txt',dct)
    dict_wr1('outdict.csv',d1)
    dict_rd('outdict.csv')
