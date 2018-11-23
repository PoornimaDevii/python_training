# To name all the files with extension .c, as .cpp (use Glob module in python)

import glob,os

#print(glob.glob('*.py'))

folder = '/home/cisco/PycharmProjects/samp_proj1/day_021118'


# for file in os.listdir(folder):
#     infiles = os.path.join(folder,file)
#     print(infiles)
#     newfiles = infiles.replace('.csv','.txt')
#     output = os.rename(infiles,newfiles)

for filename in glob.iglob(os.path.join(folder, '*.csv')):
    os.rename(filename, filename[:-4] + '.txt')

for file in glob.iglob('/home/cisco/PycharmProjects/samp_proj1/day_011118/*'):
    print("see the list",file)