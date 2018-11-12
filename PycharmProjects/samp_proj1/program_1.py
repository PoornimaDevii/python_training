'''time = int(input("Enter the time"))
x = input("Enter if its morning or evening m/e")

if x == 'm':
    print("The time is", time+ 'a.m')
elif x == 'e':
    print("The time is",time+'p.m')'''


#condition if true condition else


# x = int(input("Enter the time"))
# print(str(x)+'a.m' if x <= 12 else str(x-12)+'p.m')

with open('outdict.txt')as file:
    f = file.readline()
    print(f)
    a = f.split(':')
    c = list(map(lambda x: x.strip('\n'), a))
    print(c)