
def gen_read(fname,wfname):
    with open(fname) as file:
        f_lines = file.readlines()
        for line in f_lines:
            if line != '\n':
                new_list = []
                new_list.append(line.strip())
                for elm in new_list:
                        with open(wfname,'w') as file:
                                if len(elm) < 50:
                                    file.write("\t\t%s\n" % elm)
                                else:
                                    i = 51
                                    file.write("\t\t%s\n" % elm[:51])
                                    i = 52
                                    while i > 51:
                                        file.write("\t\t%s\n" % elm[i:i + 51])
                                        i += 51
                                        continue

gen_read('/home/cisco/PycharmProjects/samp_proj1/day_201118/text5.txt','/home/cisco/PycharmProjects/samp_proj1/day_201118/text6.txt')