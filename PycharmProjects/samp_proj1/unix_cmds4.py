import os

# fd = os.open('output.txt', os.O_CREAT|os.O_WRONLY, 644)
# os.write(fd, b'Hello World\n')
# os.close(fd)
# print(fd)

fd = os.open('output.txt',os.O_RDONLY)
data = 1
while data:
    data = os.read(fd,1)
    os.write(1,data)
os.close(fd)

print(fd)

# os.lseek.__doc__