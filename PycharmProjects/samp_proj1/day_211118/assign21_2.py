#https://www.journaldev.com/19002/python-zipfile-zip

import sys
import zipfile,os

if __name__ == '__main__':
    zf = zipfile.PyZipFile('zipfile_1.zip', mode='w')
    try:
        zf.write('/home/cisco/PycharmProjects/samp_proj1/day_201118/assign20_1.py')
        zf.write('/home/cisco/PycharmProjects/samp_proj1/day_201118/assign20_2.py')
        zf.write('/home/cisco/PycharmProjects/samp_proj1/day_201118/assign20_3.py')
        zf.write('/home/cisco/PycharmProjects/samp_proj1/day_201118/empty1.txt')
        zf.write('/home/cisco/PycharmProjects/samp_proj1/day_201118/empty2.txt')
    finally:
        zf.close()
    for name in zf.namelist():
        print(name)

#new_l = []
new_l = zipfile.ZipFile('zipfile_1.zip')
for file in new_l.infolist():
    print(file.file_size)

zero_size_l = [file.filename for file in new_l.infolist() if file.file_size == 0]
print("The files with zero bytes size",zero_size_l)