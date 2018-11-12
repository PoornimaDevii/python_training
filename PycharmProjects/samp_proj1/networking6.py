# Echo server (with UDP)

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
#sock.listen(1)

while True:
    # Wait for a connection
    #print('waiting for a connection')
    #connection, client_address = sock.accept()
    while True:
        data = sock.recvfrom(20)
        print('received {!r}'.format(data))
        if data:
            print('sending data back to the client')
            #sendall(data)
        else:
                #print('no data from', client_address)
                break




# On the server side -- socket -> bind -> listen -> accept -> recv -> send
# On the client side -- socket -> connect -> send -> receive