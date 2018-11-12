# Testing whether tar file exists

import tarfile

# for filename in ['README.txt', 'example.tar',
#                  'bad_example.tar', 'notthere.tar']:
#     try:
#         print('{:>15}  {}'.format(filename, tarfile.is_tarfile(
#             filename)))
#     except IOError as err:
#         print('{:>15}  {}'.format(filename, err))


#read contents of tar file

with tarfile.open('example.tar', 'r') as t:
    print(t.getnames())

