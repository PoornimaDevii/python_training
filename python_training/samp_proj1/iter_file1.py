# file behaves like a list, and lines can be iterated

# in case of large files, iterator can be used


ilist = iter(['some','list'])
print(next(ilist))
print(next(ilist))
#print(next(ilist))

iset = iter({'some','set'})
print(next(iset))
print(next(iset))
#print(next(iset))

istring = iter('some string')
print(next(istring))
print(next(istring))
print(next(istring))
print(next(istring))
print(next(istring))
print(next(istring))

iterator = iter('hi')
print(next(iterator))
print(next(iterator))
#print(next(iterator))
#print(next(iterator))

ituple = iter(('lion','eleph','mouse'))
print(next(ituple))


def iter_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)

iter_each({11,19,12})


class Repeater:

    def __init__(self,v):
        self.value = v
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:

    def __init__(self,s):
        self.source = s
    def __next__(self):
        return self.source.value

r1 = Repeater([12,11])
#for var in r1:
#    print(var)
#ri1 = RepeaterIterator(r1)
iter1 = r1.__iter__()
# while True:
#     item = iter1.__next__()
#     print(item)
item = iter1.__next__()
print(item)
#or
print(next(iter1))

# Combining the two

class Repeater:

    def __init__(self,v):
        self.value1 = v

    def __iter__(self):
        return self

    def __next__(self):
        return self.value1

re1 = Repeater([22,53])
for elm in re1:
    print(elm)









