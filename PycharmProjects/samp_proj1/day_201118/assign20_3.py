import os,time,subprocess

print("The child will list out files of 0 bytes size")
print("The parent will delete those listed files")

pid = os.fork()

if pid == 0:
    print("I am the child, my pid is", os.getpid())
    a = subprocess.run(['ls', '-1'],stdout=subprocess.PIPE)
    b = a.stdout.decode('utf-8')
    c = b.strip().split('\n')
    zero_size_l = [file for file in c if os.stat(file).st_size == 0]
    with open("/home/cisco/PycharmProjects/samp_proj1/day_201118/file_list.txt",'w') as file:
        for each in zero_size_l:
            file.write(each)
else:
    print("I am the parent, my pid is", os.getpid())
    time.sleep(10)
    print("My child's pid is",pid)
    with open("/home/cisco/PycharmProjects/samp_proj1/day_201118/file_list.txt") as file:
        file_lines = file.readlines()
        for each in file_lines:
            #print(each)
            os.unlink(each)