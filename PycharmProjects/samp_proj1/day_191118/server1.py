# TCP server

import socket
import pickle

#socket -> bind -> listen -> accept -> recv -> send -> close


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9090))
s.listen(5) # 5 is the size of the queue
while True:
    c, addr = s.accept()
    while True:
        try:
            data = c.recv(200)
            print('received {!r}'.format(data))
            print('dataaa-rec',data)
            if data:
                print('data type',type(data))

                p = pickle.loads(data)
                print('pickkk',p)# bytes -> object
                p.name = p.name.upper()
                # m = pickle.dumps(p) #pickled -> bytes
                # print(m)
                c.send(pickle.dumps(p))

            else:
                print('no data from', addr)
                break

        finally:
            c.close()

# received data : i__main__\nStudent\np0\n(dp1\nS'age'\np2\nI24\nsS'name'\np3\nS'reena'\np4\nsS'roll'\np5\nI32453\nsb