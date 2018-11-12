# Creating a TCP server

import socket # socket are considered just like files in unix, and even pipes.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9001))
s.listen(5) # 5 is the size of the queue
while True:
    c, a = s.accept()
    print("Received connection from", a)
    c.send(b"Hello" + bytes(a[0], "utf-8"))
    c.close()

# To kill a port in unix -> fuser -k <port_no/protocol-name>

#print(dir(s))
# s.settimeout.__doc__ -> Sets timeout on socket operations

