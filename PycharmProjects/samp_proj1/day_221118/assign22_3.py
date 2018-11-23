# weakref module
class Samp:

    # def __init__(self,v1):
    #
    #     self.var1 = v1
    #     self.var2 = 432.232

    def f(self):
        print("Hello")

    def __del__(self):
        print("Object is destructed")

# samp1 = Samp()
# print(samp1)
# del samp1

# samp2 = Samp()
# samp22 = samp2.f
# del samp2

# samp2 = Samp()
# weakref.ref(samp2)
# samp22 = samp2.f
# del samp2

# import weakref
# sam1 = Samp()
# weakref.ref(sam1)
# Out[5]: <weakref at 0x7f32d4c6f1d8; to 'Samp' at 0x7f32d4c68d30>
# sam11 = sam1.f
# del sam1
# sam11
# Out[8]: <bound method Samp.f of <__main__.Samp object at 0x7f32d4c68d30>>





