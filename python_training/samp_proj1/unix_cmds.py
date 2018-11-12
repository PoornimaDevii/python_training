import os, time

x = 9
pid = os.fork() # Replicating the process
#print(pid)
#print("Hello World")
if pid == 0:
    time.sleep(5)
    x = x + 9
    f = open('dictout.txt', 'w')
    f.write(str(x))
    f.close()
    #os.execl('/bin/ls','ls')
    print("Hello World from child")
    print("I am the child, my pid is", os.getppid()) # os.getppid() will return the self's parent's pid
    print("I am the child, my pid is", os.getpid())
    #os.execlp('ls','ls') # will replace the previous process

    print('x is', x)
else:
    #os.wait()  # parent waiting for the child to execute first
    f = open('dictout.txt')
    read_x = f.read()
    print("The value is", read_x)
    print("Hello World from parent") # parent can track the child part using pid
    print("Child pid is", pid)
    print("My pid is", os.getpid()) # returns self's pid
    print('x is',read_x)
    f.close()
