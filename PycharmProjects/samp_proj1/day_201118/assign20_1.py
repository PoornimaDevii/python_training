
new_lines = []

with open('/home/cisco/PycharmProjects/samp_proj1/day_201118/text1') as file:
    f_lines = file.readlines()
    for line in f_lines:
        if line != '\n':
            a = line.strip()
            new_lines.append(a)

print(new_lines)


with open('/home/cisco/PycharmProjects/samp_proj1/day_201118/text2','w') as file:
    for elm in new_lines:
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




