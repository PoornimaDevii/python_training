# To get the total size of all files in the directory

import os

import subprocess

completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
a = completed.stdout.decode('utf-8')
b = a.strip().split('\n')
print(b)
# print('returncode:', completed.returncode)
# print('Have {} bytes in stdout:\n{}'.format(
#     len(completed.stdout),
#     completed.stdout.decode('utf-8'))

# c = list(completed.stdout.decode('utf-8'))
#
# for file in b:
#     print(type(os.stat(file)))
size = [os.stat(file).st_size for file in b]
print(size)
from functools import reduce
tot_size = reduce(lambda x,y: x+y,size)
print("The total size of the files are" ,tot_size)