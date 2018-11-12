

try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    #print('x =',x)
    #print('y =',y)