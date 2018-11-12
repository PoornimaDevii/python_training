# UDP client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = b"Hello World"
# c.send(b"Hello" + bytes(a[0], "utf-8"))
s.sendto(msg,("localhost", 8900))
data, addr = s.recvfrom(20)
print(data)

# To find the unix domain sockets - sudo find / -type s -ls 2> /dev/null
# types of sockets - raw sockets, concurrent and iterative sockets
# sockets we use - TLI ( transport layer interface) sockets