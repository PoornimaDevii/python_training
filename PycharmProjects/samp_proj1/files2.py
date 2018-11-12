

mydict = {'pnq':[12,11,15],
          'maa':[31,29,38]}
f = open('dump_data.csv','w')
#First create the header
f.write(','.join(mydict.keys())+'\n')
i = 0

while i < len(mydict['pnq']):
    f.write(str(mydict['pnq'][i]) + ',' + str(mydict['maa'][i]) + '\n')
    i = i + 1
f.close()


f = open('dump_data.csv','r')
content = list(map(lambda x: x.strip(),f.readlines()))
content = list(map(lambda x:x.split(','),content))
print(content)

import numpy as np
content_arr = np.array(content[1:])
#print(content_arr.T)
content_list = list(content_arr.T)
#print(content_list)
content_list = list(map(lambda x:list(x),content_list))
#print(content_list)
data = dict(zip(content[0],content_list))
print(data)

# To delete a file, use os.unlink(filename)
# To copy/move files, import shutil
# list(os.stat(filename)[]