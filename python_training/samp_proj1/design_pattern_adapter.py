# Adapter Pattern
# format() similar to __repr__
class Computer:

    def __init__(self,n):
        self.name = n

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'

# c1 = Computer('mycomp')
# print(c1)
# print(c1.execute())

# Synthesizer class

class Synthesizer:

    def __init__(self,n):
        self.name = n

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'can play a song'

# s1 = Synthesizer('googlemusic')
# print(s1)
# print(s1.play())

class Human:

    def __init__(self,n):
        self.name = n

    def __str__(self):
        return 'the {} speaker'.format(self.name)

    def speak(self):
        return 'can speak'

# sp1 = Human('poornima')
# print(sp1)
# print(sp1.speak())

class Adapter:
    def __init__(self,o, adapter_methods):
        self.obj = o
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)

objects = Computer('Asus') # Client interface
synth = Synthesizer('moog')
human = Human('Bob')
asy = Adapter(synth, dict(execute=synth.play))
ahu = Adapter(human,dict(execute=human.speak))
print(asy.execute())
print(ahu.execute())

