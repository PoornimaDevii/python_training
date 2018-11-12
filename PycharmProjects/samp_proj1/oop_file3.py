
class Sample:
    x = 23

    def increment(self):
        self.__class__.x += 1

a = Sample()
print(a.increment())
print(a.__class__.x) # or
print(Sample.x)