# UDP server

#from socket import * <- not be used like this
import socket # instead use like this

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost",8900))

while True:
    data, addr = s.recvfrom(20)
    resp = b"Get off the lawn!!"
    s.sendto(resp,addr)


