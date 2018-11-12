# Stopping Iterator

class BoundedRepeater:

    def __init__(self,v, uplim):
        self.value = v
        self.limit = uplim
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.value

br1 = BoundedRepeater("hello",4)

br_iter = br1.__iter__()
#print(next(br_iter))
#print(next(br_iter))
#print(next(br_iter))
#print(next(br_iter))
#print(next(br_iter))

for var in br1:
    print(var)

while True:
    try:
        next(br1)
    except:
        print("Done")
        break

# Use case of iterator - Fibonacci Series

class Fibnum:
    def __init__(self):
        self.fn1 = 1
        self.fn2 = 1

    def __next__(self):
        self.fn1, self.fn2, oldfn2 = self.fn1 + self.fn2, self.fn1, self.fn2
        return oldfn2

    def __iter__(self):
        return self


def main():
    f = Fibnum()
    for i in f:
        print(i)
        if i > 20:
            break

if __name__ == '__main__':
    main()

# Use case of Iterator - Hofstadter Q sequence

class qsequence(object):

    def __init__(self, s):
        self.s = s[:]

    def __next__(self):
        try:
            q = self.s[-self.s[-1]] = self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self

    def current_state(self):
        return self.s

Q = qsequence([1,1])
print([next(Q) for __ in range(10)])

















