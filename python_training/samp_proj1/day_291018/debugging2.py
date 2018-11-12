# set trace acts like a breakpoint. When the program hits the point,
# where set_trace is called, it enters the debugger

# for example
import pdb

def dict_wr1(filename,d1):
    f = open(filename,'w')
    pdb.set_trace()
    for (k,v) in d1.items():
        f.write(str(k)+','+str(v)+'\n')
    f.close()

dict_wr1()