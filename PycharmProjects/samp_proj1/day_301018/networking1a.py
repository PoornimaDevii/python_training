# automating the sending of file using secure control protocol(SCP)

import os
import paramiko

def printTotals(transferred, toBeTransferred):
    print("Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred))


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='127.0.0.1', username="cisco", password='cisco', port='22')
sftp = ssh.open_sftp()
localpath = '/home/cisco/PycharmProjects/samp_proj1/hello.py' #source
remotepath = '/home/cisco/Downloads/hello1.py'#destin
# sftp.put(localpath, remotepath)
sftp.put(localpath,remotepath,callback=printTotals)
sftp.close()
ssh.close()