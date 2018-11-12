# Adapter Pattern (client:projector vga, dell lap hdmi mac usb)
# format() similar to __repr__

class Projector:

    def __init__(self,n):
        self.name = n

    def __str__(self):
        return 'the {} projector'.format(self.name)

    def vga(self):
        return 'has VGA'

# c1 = Computer('mycomp')
# print(c1)
# print(c1.execute())

# Synthesizer class

class Dell:

    def __init__(self,n):
        self.name = n

    def __str__(self):
        return 'the {} Laptop'.format(self.name)

    def hdmi(self):
        return 'has HDMI'

# s1 = Synthesizer('googlemusic')
# print(s1)
# print(s1.play())

class Mac:

    def __init__(self,n):
        self.name = n

    def __str__(self):
        return 'the {} Laptop'.format(self.name)

    def usb(self):
        return 'has USB'

# sp1 = Human('poornima')
# print(sp1)
# print(sp1.speak())

class Adapter:
    def __init__(self,o, adapter_methods):
        self.obj = o
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)

# objects = Computer('Asus') # Client interface
# synth = Synthesizer('moog')
# human = Human('Bob')
# asy = Adapter(synth, dict(execute=synth.play))
# ahu = Adapter(human,dict(execute=human.speak))
# print(asy.execute())
# print(ahu.execute())

pro1 = Projector('myprojector')
dell1 = Dell('mydell')
mac1 = Mac('mymac')
adell = Adapter(dell1, dict(vga=dell1.hdmi))
amac = Adapter(mac1, dict(vga=mac1.usb))
print("The Dell laptop", adell.vga())
print("The Mac laptop",amac.vga())

