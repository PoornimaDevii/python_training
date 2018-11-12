# To download the README from gnu.org file and scan lines containing 'the', convert to upper case and send to 'echo server',
# write to file

import re
import socket
import ftplib
import logging
import paramiko

f = ftplib.FTP('ftp.oreilly.com')
f.login()
logging.info("Logged into the site")

files = []
f.retrlines("LIST")
logging.info("Listed the files")

logging.info("Retrieving README file")
f.retrbinary('RETR README', open('README','wb').write)

logging.info("Quitting FTP")
f.quit()

def read_readme(fname):
    f = open(fname)
    f_list = f.readlines()
    return f_list

the_lines = []
def collect_the_lines(l):
    mat1 = re.compile(/^(?!the)/)
    for line in l:
        mat1.search(line)
        b = the_lines.append(mat1.search(line))
    return the_lines

def list_t_str(the_lines):
    for line in the_lines:
        jo = ','.join(line)
        return jo


read_readme('/home/cisco/PycharmProjects/samp_proj1/day_301018/README')
collect_the_lines(f_list)
lsit_t_str(the_lines)


sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock1.bind(server_address)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(100)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()




