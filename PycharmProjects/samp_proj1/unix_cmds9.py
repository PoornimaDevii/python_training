import os, time,sys

print("The child will write text to a pipe and")
print("The parent will read the text written by child")

r, w = os.pipe()

x = 9
pid = os.fork() # Replicating the process
#print("Hello World")
if pid == 0:
    time.sleep(5)
    x = x + 9
    f = open('dictout.txt', 'w')
    f.write(str(x))
    f.close()
    w = os.fdopen(w,'w')
    print("Child writing")
    w.write("Text written by child")
    w.close()
    print("Child closing")
    sys.exit(0)
    #os.execl('/bin/ls','ls')
    print("Hello World from child")
    print("I am the child, my pid is", os.getppid()) # os.getppid() will return the self's parent's pid
    print("I am the child, my pid is", os.getpid())
    #os.execlp('ls','ls') # will replace the previous process

    print('x is', x)
else:
    os.wait()  # parent waiting for the child to execute first
    f = open('dictout.txt')
    read_x = f.read()
    print("The value is", read_x)
    print("Hello World from parent") # parent can track the child part using pid
    print("Child pid is", pid)
    print("My pid is", os.getpid()) # returns self's pid
    print('x is',read_x)
    f.close()
    r = os.fdopen(r)
    print("Parent reading")
    mstr = r.read()
    print("Text:", mstr)
    sys.exit(0)

# pipe is always unidirectional and called unnamed pipe if the commands belong to a shell (called siblings)
# named pipe (executed using mkfifo)