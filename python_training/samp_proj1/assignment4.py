''' ip address a.b.c.d problem '''

ip = input("Enter the IP address")

ip_l = [int(i) for i in ip.split('.')]
print(ip_l)


if ip_l[3] < 255:
    ip_l[3] += 1
elif ip_l[3] == 255:
    ip_l[2] += 1
    ip_l[3] = 0
else:
    if ip_l[2] < 255:
        ip_l[2] += 1
    elif ip_l[2] == 255:
        ip_l[1] += 1
        ip_l[2] = 0

print(ip_l)


if ip_l[1] < 255:
    ip_l[1] += 1
elif ip_l[1] == 255:
    ip_l[0] += 1
    ip_l[1] = 0

if ip_l[0] < 255:
    ip_l[0] += 1
elif ip_l[0] == 255:
    if ip_l[1] == 255:
        if ip_l[2] == 255:
            if ip_l[3] == 255:
                raise Exception
print(ip_l)
for elm in range(len(ip_l)):
    nxt_ip = '.'.join(str(elm))
    print("a is",nxt_ip)

print("The next IP address is",elm)

