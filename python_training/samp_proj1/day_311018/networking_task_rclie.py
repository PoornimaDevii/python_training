# Client code

import ftplib, socket,paramiko

def download_file(site,file):

    f = ftplib.FTP(site)
    f.login('anonymous','dave@dabeaz.com')
    f.retrlines(file)
    f.retrbinary('RETR ' + file, open(file,'wb').write)
    return read_file(file)

lines_list = []
def read_file(fname):
    for line in fname.readlines():
        if 'the' in line:
            final_str = ''.join(line)

    return receive_from(final_str)


def receive_from(string):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost',10000)
    sock.connect(server_address)
    sock.send(bytes(string,'utf-8'))
    data, addr = sock.recvfrom(200)
    data = data.decode("utf-8")
    return w_file(data)

def w_file(d):
    f = open('the_lines.txt','w')
    f.writelines(d)
    f.close()
    return transfer_file('the_lines.txt')


def transfer_file(file):

    def printTotals(transferred, tobeTransferred):
        print("Transferred: {0}\tout of : {1}".format(transferred, tobeTransferred))

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='127.0.0.1', username='cisco', password='cisco', port='22')
    sftp = ssh.open_sftp()
    localpath = file
    remotepath = '/home/Downloads/Transfered_data.txt'
    sftp.put(localpath, remotepath, callback=printTotals)
    sftp.close()
    ssh.close()

