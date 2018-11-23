import socket
import pickle
from Student_cls import Student

#socket -> bind -> connect -> send -> close

# Class and pickling part

stu_obj = Student('reena', 24, 32453)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('localhost',9090)
s.connect(server_addr)

stu = pickle.dumps(stu_obj) # converts into a bytes-object from pickled object
s.sendall(stu)

data = s.recv(200)

print(data)
if data:
    out_data = pickle.loads(data)
    print(out_data.name)

s.close()

#-------------------------------------------------------


