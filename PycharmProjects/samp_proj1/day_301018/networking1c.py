# To automate connection to a site using ftp

import ftplib # Module for interacting with FTP servers

f = ftplib.FTP('ftp.gnu.org','anonymous','dave@dabeaz.com')
files = []

f.retrlines("LIST",files.append)

print(len(files))
print(files[0])
print(files[1])

