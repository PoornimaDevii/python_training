# Text file as input, replace the alpha with alpha that is 14units away from the first alpha

s = "abcdefghijklmnopqrstuvwxyz" # output  nopqrstuvwxyzabcdefghijklm
l = []
new = []
for elm in s:
    l.append(elm)

print(l)
for elm in l:
    if ord(elm) < 110:
        i = ord(elm) + 13
        print(i)
        n = elm.replace(elm,chr(i))
        new.append(n)
    elif ord(elm) >= 110:
        i = ord(elm) - 13
        print(i)
        n = elm.replace(elm,chr(i))
        new.append(n)


print("The input string is",(''.join(l)))
print("The replaced string is",(''.join(new)))