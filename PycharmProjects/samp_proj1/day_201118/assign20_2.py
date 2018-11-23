

def gen_read(fname):
    with open(fname) as file:
        f_lines = file.readlines()
        for line in f_lines:
            if line != '\n':
                a = line.strip()
                yield a

new_list = []
for i in gen_read('/home/cisco/PycharmProjects/samp_proj1/day_201118/text3.txt'):
    print(i)
    new_list.append(i)

print(new_list)

def gen_writ(fname,l):
     with open(fname,'w') as file:
         for elm in new_list:
             if len(elm) < 50:
                 file.write("\t\t%s\n" %elm)
             else:
                 i = 51
                 file.write("\t\t%s\n" %elm[:51])
                 i = 52
                 while i > 51:
                     file.write("\t\t%s\n" %elm[i:i+51])
                     i += 51
                     break

gen_writ('/home/cisco/PycharmProjects/samp_proj1/day_201118/text4.txt',new_list)
