# To create a server, allocate from port no 1025 to 6344(not sure)

# TO see the port nos - cat /etc/services
# To view the ip address of web sites - nslookup

# cisco@cisco-ThinkPad-T430:~$ nslookup
# > ns.google.com
# Server:		127.0.1.1
# Address:	127.0.1.1#53
#
# Non-authoritative answer:
# Name:	ns.google.com
# Address: 216.239.32.10
# > ns1.google.com
# Server:		127.0.1.1
# Address:	127.0.1.1#53
#
# Non-authoritative answer:
# Name:	ns1.google.com
# Address: 216.239.32.10


# cisco@cisco-ThinkPad-T430:~$ mkfifo np1
# cisco@cisco-ThinkPad-T430:~$ ls -l np1
# prw-rw-r-- 1 cisco cisco 0 Oct 26 10:02 np1
# cisco@cisco-ThinkPad-T430:~$ telnet www.python.org 80
# Trying 2a04:4e42:24::223...
# Connected to dualstack.python.map.fastly.net.
# Escape character is '^]'.
# ^]
# telnet> quit
# Connection closed.
# cisco@cisco-ThinkPad-T430:~$

# Socket programming

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.google.com', 80)) # Connect
s.send(b"GET /index.html HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response
print(data)
s.close()